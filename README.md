# Local-Document-Assistant -  Realtime Document Q&A with PDF, DOCX, and TXT
A lightweight local Retrieval-Augmented Generation (RAG) application built with Python, Shiny for Python, and Ollama using the Phi-3 Mini model. Upload a document, extract a preview, and ask natural language questions to get real-time answers grounded in your file content.

## Features
* Upload and preview PDF, DOCX, or TXT files

* Automatic OCR fallback for scanned PDFs (via Tesseract)

* Semantic search with ChromaDB + LangChain

* Fast local generation via Ollama + Phi-3 Mini

* Simple, interactive Shiny-based UI

* Completely offline, privacy-friendly assistant

## Quickstart Guide

Follow these steps to install and run the app in your own system without internet access.
Run these from your VS terminal.

*  Clone this repository :
```
git clone https://github.com/your-username/local-rag-assistant.git
cd local-rag-assistant
```
*  Create and activate a virtual environment :
```
py -3.13 -m venv rag_env
rag_env\Scripts\activate
```
* Install dependencies :
```
pip install -r requirements.txt
```
If requirements.txt is missing, you can use:
```
pip install shiny langchain langchain-community chromadb ollama pymupdf pillow tesseract python-docx
```
* Install and run Ollama (for Phi-3 Mini) :
If not already installed:
Download Ollama and install from [here](https://ollama.com/download)
Open terminal and run:
```
ollama run phi3:mini
```
### Supported File Types - pdf – Including scanned documents (OCR), docx – Word files and txt – Plain text

## Model: Phi-3 Mini
Phi-3 Mini is a 3.8B parameter model optimized for reasoning and instruction following. This app uses the Ollama runtime to serve it locally.

## Tips & Troubleshooting
 * Ask questions after uploading a document and seeing ✅ Document processed....
 * For OCR to work, [Tesseract](https://github.com/tesseract-ocr/tesseract) must be installed and in your system path.
 * Use the Reset button before every new query to clear the state.

## Example Use Cases
*Extract key data from research papers or reports
*Ask questions about legal, medical, or policy documents
*Summarize or find answers in scanned physical forms

## License
MIT – Use it freely, privately, and locally.



