# 📄 PDF Information Extractor

A high-performance, web-based PDF analysis tool that combines traditional text parsing with advanced local vision-language AI models to perform Optical Character Recognition (OCR), document summarization, and embedded image description.

---

## ✨ Features

- **⚡ Fast Standard Extraction**: Uses `PyMuPDF` to instantly extract and index native text content and structure from digital PDFs.
- **👁️ AI-Powered OCR**: Automatically processes scanned PDFs or page images using `Ollama` with `gemma3` to perform local, private OCR.
- **📝 Document Summarization**: Leverages AI to read the opening pages and generate a concise general description and summary of the document.
- **🖼️ Embedded Image Analysis**: Automatically extracts images from the PDF, passes them to a local vision model, and returns descriptions of their visual content.
- **💻 Simple Web Interface**: Clean, responsive frontend designed with HTML5, CSS3, and JavaScript for seamless drag-and-drop file upload and structured results visualization.

---

## 🛠️ Technical Stack

- **Backend**: FastAPI (Python 3.10+), Uvicorn ASGI Server
- **Text & Media Processing**: PyMuPDF (fitz)
- **AI Inference Engine**: Ollama (Running the multimodal `gemma3` model locally)
- **Frontend**: Vanilla HTML5, CSS, and ES6 Javascript

---

## 📋 Prerequisites

Before running the application, make sure you have:
1. **Python 3.10+**
2. **Ollama** installed on your system (Download from [ollama.ai](https://ollama.ai))

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/AnupamKhurana/pdf-onformation-extractor.git
cd pdf-onformation-extractor
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Pull the Local Multimodal AI Model
Ensure Ollama is running in the background, then pull the `gemma3` model:
```bash
ollama pull gemma3
```

### 4. Run the Application
```bash
uvicorn main:app --reload
```
Open your browser and navigate to [http://localhost:8000](http://localhost:8000).

---

## 📂 Project Structure

```
pdf-onformation-extractor/
├── main.py               # FastAPI backend app & Ollama interface
├── requirements.txt      # Python dependencies
├── static/
│   └── style.css         # Styling for the web dashboard
├── templates/
│   └── index.html        # HTML layout for upload & display
└── README.md             # This guide
```
