
import base64
import io
import fitz  # PyMuPDF
import httpx
from httpx import TimeoutException
import uvicorn
import os
import markdown2
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# --- Setup: Base directories and static files ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# --- Ollama Configuration ---
OLLAMA_API_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "gemma3:latest"
OLLAMA_TIMEOUT = 120.0

def get_ollama_response(data: bytes | str, prompt: str) -> str:
    try:
        payload = {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
        }
        if isinstance(data, bytes):
            encoded_image = base64.b64encode(data).decode("utf-8")
            payload["images"] = [encoded_image]
        else:
            payload["prompt"] = f"{prompt}\n\n{data}"

        with httpx.Client(timeout=OLLAMA_TIMEOUT) as client:
            response = client.post(OLLAMA_API_URL, json=payload)
            response.raise_for_status()
            raw_response = response.json().get("response", "").strip()
            return markdown2.markdown(raw_response)
    except TimeoutException:
        return "<p>Ollama request timed out. The model might be taking too long to respond or is too large for your system.</p>"
    except httpx.RequestError as e:
        return f"<p>An error occurred while requesting Ollama: {e}</p>"
    except Exception as e:
        return f"<p>An unexpected error occurred: {e}</p>"

@app.get("/", response_class=HTMLResponse)
async def read_root():
    index_path = os.path.join(TEMPLATES_DIR, "index.html")
    with open(index_path, "r") as f:
        return HTMLResponse(content=f.read())

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        return JSONResponse(
            content={"error": "Invalid file type. Please upload a PDF."},
            status_code=400,
        )

    try:
        pdf_bytes = await file.read()
        pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")

        pdf_b64 = base64.b64encode(pdf_bytes).decode("utf-8")
        initial_text = ""
        page_count = len(pdf_document)

        for page_num in range(page_count):
            page = pdf_document.load_page(page_num)
            blocks = page.get_text("blocks")
            for b in blocks:
                text_block = b[4].strip()
                if text_block:
                    initial_text += f"<p>{text_block}</p>"

        if not initial_text.strip():
            initial_text = """
            <div class='alert'>
                <strong>No standard text found.</strong>
                <p>This PDF appears to be image-based or has complex formatting.</p>
                <p>Relying on the AI model for Optical Character Recognition (OCR) to extract the text content.</p>
            </div>
            """

        return JSONResponse(content={
            "pdf_b64": pdf_b64,
            "initial_text": initial_text,
            "page_count": page_count
        })

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/process_ai/")
async def process_ai(file: UploadFile = File(...)):
    try:
        pdf_bytes = await file.read()
        pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")

        general_description = ""
        ocr_text = ""
        image_interpretations = []

        # Generate general description from the first page's text
        if len(pdf_document) > 0:
            first_page = pdf_document.load_page(0)
            first_page_text = first_page.get_text("text")
            if first_page_text.strip():
                desc_prompt = "Provide a concise general description of this document based on the following text. Focus on its type, main content, and purpose. Do not ask follow-up questions or offer additional assistance."
                general_description = get_ollama_response(first_page_text, desc_prompt)
            else:
                # Fallback to image if no text is found on the first page
                pix = first_page.get_pixmap()
                img_data = pix.tobytes("png")
                desc_prompt = "Provide a concise general description of this document based on its first page image. Focus on its type, main content, and purpose. Do not ask follow-up questions or offer additional assistance."
                general_description = get_ollama_response(img_data, desc_prompt)

        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)

            pix = page.get_pixmap()
            img_data = pix.tobytes("png")
            ocr_prompt = "Directly extract all text from this image. Preserve original formatting. Do not add any commentary or introductory text."
            ocr_text += f"<h3>Page {page_num + 1} (Ollama OCR)</h3><div>{get_ollama_response(img_data, ocr_prompt)}</div>"

            image_list = page.get_images(full=True)
            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = pdf_document.extract_image(xref)
                image_bytes = base_image["image"]
                img_b64 = base64.b64encode(image_bytes).decode("utf-8")
                interp_prompt = "Directly describe the content and information in this image. Do not ask follow-up questions or offer additional assistance."
                interpretation = get_ollama_response(image_bytes, interp_prompt)
                image_interpretations.append({
                    "page": page_num + 1,
                    "index": img_index + 1,
                    "src": f"data:image/png;base64,{img_b64}",
                    "interpretation": interpretation
                })

        return JSONResponse(content={
            "general_description": general_description,
            "ocr_text": ocr_text,
            "image_interpretations": image_interpretations
        })
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
