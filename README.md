# 📄 AI PDF Information Extractor & OCR Analyzer

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PyMuPDF](https://img.shields.io/badge/PyMuPDF-fitz-2E8555?style=for-the-badge)](https://pymupdf.readthedocs.io/)
[![Ollama](https://img.shields.io/badge/Ollama-Gemma_3-000000?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

A high-performance, privacy-first web application combining native PDF text parsing with local vision-language AI models. Extract text, perform offline OCR on scanned documents, auto-generate executive summaries, and analyze embedded charts/images using **PyMuPDF**, **FastAPI**, and **Ollama (Gemma 3)**.

---

## ✨ Key Features & Capabilities

- ⚡ **High-Speed Native Parsing**: Extracts digital text, structural metadata, and page layouts in milliseconds via `PyMuPDF`.
- 👁️ **100% Offline AI OCR**: Seamlessly transcribes scanned documents and handwritten forms using local vision-language inference with zero data leakage to cloud servers.
- 📝 **Automated Document Summaries**: Synthesizes multi-page reports, research papers, and invoices into concise executive briefings.
- 🖼️ **Visual Content & Diagram Description**: Extracts embedded figures, diagrams, and photos from PDFs and produces contextual captions.
- 🖥️ **Drag-and-Drop Web Interface**: Clean, responsive frontend with real-time analysis progress indicators and tabbed inspection views.

---

## 🛠️ Architecture & Tech Stack

| Layer | Component | Description |
| :--- | :--- | :--- |
| **API Server** | [FastAPI](https://fastapi.tiangolo.com/) | Asynchronous request processing and streaming endpoints |
| **Parsing Engine** | [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/) | High-speed C-backed PDF parsing and rasterization |
| **Vision & Reasoning** | [Ollama](https://ollama.ai) + `gemma3` | Local multimodal vision-language model for OCR and image comprehension |
| **Frontend** | Vanilla JS + Modern CSS | Lightweight zero-dependency user interface |

---

## 📂 Project Structure

```text
pdf-information-extractor/
├── main.py               # FastAPI backend, upload handler & Ollama client
├── requirements.txt      # Python dependencies
├── static/
│   └── style.css         # Responsive UI styling
├── templates/
│   └── index.html        # Interactive upload & analysis dashboard
└── README.md             # Documentation
```

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.10+**
- **Ollama** installed ([download instructions](https://ollama.ai))

### 1. Clone Repository
```bash
git clone https://github.com/AnupamKhurana/pdf-onformation-extractor.git
cd pdf-onformation-extractor
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Pull Local Vision AI Model
Start the Ollama daemon and pull the multimodal `gemma3` model:
```bash
ollama pull gemma3
```

### 4. Launch the Web Application
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```
Open your browser at: **`http://localhost:8000`**

---

## 💡 How It Works

```
  [ Upload PDF ]
        │
        ├──▶ Digital PDF? ──▶ [ PyMuPDF Fast Extract ] ──▶ Structured Text
        │
        └──▶ Scanned / Images? ─▶ [ Rasterize Page ] ──▶ [ Ollama Gemma 3 Vision ] ──▶ AI Transcribed Text
                                                                 │
                                                                 └──▶ [ Executive Summary & Captions ]
```

---

## 🔒 Privacy & Security

All PDF processing, rasterization, and AI vision inference run **completely on your local machine**. No proprietary documents, personal files, or scan data are ever transmitted to third-party APIs.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests to improve extraction accuracy, support additional models, or enhance UI features.

---

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.
