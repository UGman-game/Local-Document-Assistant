Local RAG assistant that retrives information from a PDF File.

Run command in the VS terminal : 

py -3.13 -m venv rag_env
pip install shiny langchain langchain-community chromadb ollama pymupdf
rag_env\Scripts\activate
python -m shiny run --reload rag_app.py