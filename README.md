# PDF Information Extractor

This project is a web-based application that allows users to upload PDF files and extract information from them using a combination of traditional text extraction and advanced AI-powered analysis. It can process both text-based and image-based PDFs, providing a comprehensive overview of the document's content.

## Features

- **PDF Upload:** Users can upload PDF files through a simple web interface.
- **Text Extraction:** The application uses `PyMuPDF` to quickly extract and display any standard text found in the PDF.
- **AI-Powered OCR:** For image-based PDFs or pages with complex formatting, the application utilizes the `Ollama` with the `gemma3` model to perform Optical Character Recognition (OCR) and extract text from images.
- **Document Description:** The AI model generates a concise general description of the PDF's content based on the first page.
- **Image Interpretation:** The application identifies and extracts images from the PDF, and the AI model provides a description of each image's content.
- **Web Interface:** The frontend is built with `HTML`, `CSS`, and `JavaScript`, providing a user-friendly experience for uploading files and viewing the extracted information.
- **Backend:** The backend is built with `FastAPI`, a modern, fast (high-performance) web framework for building APIs with Python.

## How It Works

1.  **Upload:** The user selects a PDF file and clicks the "Upload and Process" button.
2.  **Initial Processing:** The backend receives the PDF and uses `PyMuPDF` to extract any easily accessible text. This text is immediately displayed to the user.
3.  **AI Processing:** The application then sends the PDF to the `Ollama` for more advanced analysis. This includes:
    -   **General Description:** The AI model analyzes the first page (either text or an image) to generate a summary of the document.
    -   **OCR:** The AI model processes each page as an image to extract text, which is particularly useful for scanned documents.
    -   **Image Interpretation:** The application extracts any embedded images from the PDF and sends them to the AI model for a description of their content.
4.  **Display Results:** The extracted information, including the general description, OCR text, and image interpretations, is displayed on the web page.

## Technologies Used

-   **Backend:**
    -   [FastAPI](https://fastapi.tiangolo.com/): A modern, fast web framework for building APIs.
    -   [Uvicorn](https://www.uvicorn.org/): An ASGI server for running the FastAPI application.
    -   [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/): A Python library for accessing and modifying PDF documents.
    -   [Ollama](https://ollama.ai/): A tool for running large language models locally.
    -   [gemma3](https://huggingface.co/google/gemma-2-9b-it): The large language model used for OCR, document description, and image interpretation.
    -   [python-multipart](https://pypi.org/project/python-multipart/): A streaming multipart parser for Python.
    -   [httpx](https://www.python-httpx.org/): A fully featured HTTP client for Python.
    -   [markdown2](https://pypi.org/project/markdown2/): A fast and complete implementation of Markdown in Python.
-   **Frontend:**
    -   HTML
    -   CSS
    -   JavaScript

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/pdf-information-extractor.git
    cd pdf-information-extractor
    ```
2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Install and run Ollama:**
    -   Follow the instructions on the [Ollama website](https://ollama.ai/) to download and install Ollama.
    -   Pull the `gemma3` model:
        ```bash
        ollama pull gemma3
        ```
5.  **Run the application:**
    ```bash
    uvicorn main:app --reload
    ```
6.  **Open your web browser and navigate to `http://127.0.0.1:8000`**

## Usage

1.  Open the web application in your browser.
2.  Click the "Choose File" button to select a PDF file from your computer.
3.  Click the "Upload and Process" button.
4.  The application will display the extracted text and AI-powered analysis of the PDF.

### Example Scenarios

-   **Scanned Document:** You have a scanned PDF of a contract. The application will use OCR to extract the text, allowing you to search for specific clauses or terms.
-   **Financial Report:** You upload a PDF of a financial report. The application will extract the text and tables, and the AI can provide a summary of the report's key findings.
-   **Academic Paper:** You upload a research paper. The application will extract the text, and the AI can help you understand the paper's main arguments and conclusions.

## What to Expect

-   **Accuracy:** The accuracy of the text extraction and AI analysis depends on the quality of the PDF. Clear, high-resolution documents will produce the best results.
-   **Performance:** The initial text extraction is very fast. The AI processing time will vary depending on the size and complexity of the PDF, as well as the performance of your computer running the Ollama model.
-   **Limitations:** The application is designed for general-purpose PDF analysis. It may not be suitable for highly specialized or complex documents, such as those with intricate diagrams or non-standard layouts.

## Project Structure

```
.
├── main.py               # The main FastAPI application
├── requirements.txt      # The Python dependencies
├── static
│   └── style.css         # The CSS styles for the web interface
├── templates
│   └── index.html        # The HTML template for the web interface
└── README.md             # This file
```
