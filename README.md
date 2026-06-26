# 🧠 Enterprise Private RAG Assistant (Local LLaMA + Qdrant)

A fully local **Retrieval-Augmented Generation (RAG)** system for querying scientific documents using **LLaMA 3.2**, **Qdrant**, and **semantic vector retrieval**.

This project enables natural-language question answering over large PDF documents (e.g., textbooks, research papers, technical manuals) while grounding responses in retrieved document context.

Built with:

- **LLaMA 3.2 3B Instruct** (4-bit quantized)
- **Qdrant Vector Database**
- **BAAI/bge-small-en-v1.5 Embeddings**
- **BAAI/bge-reranker-base**
- **PyTorch + Transformers**
- **Docker**
- **Gradio UI**

---

## 🚀 Features

✅ Fully local inference (no OpenAI API required)  
✅ PDF → chunk → embed → vector database pipeline  
✅ Semantic retrieval using vector similarity search and reranking
✅ Quantized LLaMA inference (4-bit NF4) for reduced VRAM usage  
✅ Context-grounded responses to minimize hallucination  
✅ Source-aware answers from retrieved document chunks  
✅ Interactive chatbot interface (Gradio)

---

## 🏗️ System Architecture

```text
PDF Document
      ↓
 Text Extraction
      ↓
 Chunking + Overlap
      ↓
 Embedding Model
 (BAAI/bge-small-en-v1.5)
      ↓
 Vector Storage
    (Qdrant)
      ↓
 Semantic Retrieval (top k + reranking)
      ↓
 Prompt Construction
      ↓
 LLaMA 3.2 (4-bit)
      ↓
 Grounded Answer
```
## 📂 Project Structure
```
Enterprise-Private-RAG-Assistant/
│── app/
│   ├── rag_pipeline.py
│   ├── retriever.py
│   ├── llm.py
│   ├── prompt.py
│   ├── settings.py
│   └── embeddings.py
│──ingest_pdf.py
│── app_ui.py
│── main.py
│── requirements.txt
│── .env.example
│── README.md

```



## ⚙️ Installation
1. Clone repository
```python
git clone <your_repo_url>
cd Enterprise-Private-RAG-Assistant
```
2. Create virtual environment
```python
python -m venv .venv
```
Activate:

Windows
```python
.venv\Scripts\activate
```
Mac/Linux
```python
source .venv/bin/activate
```
3. Install dependencies

```python
pip install -r requirements.txt
```
5. Start Qdrant (Docker)

```python
docker run -d --name qdrant -p 6333:6333 -p 6334:6334 qdrant/qdrant
```
Qdrant dashboard:

```python
http://localhost:6333/dashboard
```
5. Configure environment

Create a .env file:

```python
QDRANT_HOST=localhost
QDRANT_PORT=6333
COLLECTION_NAME=scientific_rag

EMBEDDING_MODEL=BAAI/bge-small-en-v1.5
```
## 📚 Document Ingestion

Place a PDF inside:

```python
data/  (a sample .pdf file is contained in the folder)
```
Then run:

```python
python scripts/ingest_pdf.py
```
This will:

1. Extract PDF text
2. Split into chunks
3. Generate embeddings
4. Store vectors in Qdrant
   
## 💬 Run Chatbot (CLI)
```python
python main.py
```
Example:
```python
You: who is the author

Bot:
Paul Wilmott

Sources:
[1] Page 4
Copyright © 2007 Paul Wilmott...
```
## 🌐 Run Web UI (Gradio)

```python
python app_ui.py
```
Open:
```python
http://127.0.0.1:7860
```
## 📉 RAG Chat Interface (Gradio + LLaMA + Qdrant)

![RAG UI](RAG_UI.png)

## 🧪 Model Configuration
#LLM
* Model: LLaMA 3.2 3B Instruct
* Quantization: 4-bit NF4
* Inference: Local GPU execution
#Embeddings
* BAAI/bge-small-en-v1.5
* Lightweight semantic embedding model optimized for retrieval tasks.
#Vector Database
* Qdrant
* Cosine similarity search

##🔬 Example Use Cases
* Financial docunent
* Research paper exploration
* Technical manual querying
* Literature review assistance
* Domain-specific knowledge retrieval

## 🔮 Future Improvements
* Multi-turn conversational memory
* Hybrid retrieval (keyword + vector search)
* Citation-aware answers with page references
* Multi-document knowledge base
* Streaming responses
* Reranking for retrieval quality
* Research-paper summarization
  
## 🛠️ Technologies Used
* Python
* PyTorch
* Hugging Face Transformers
* BitsAndBytes
* Qdrant
* Docker
* Gradio
* Sentence Transformers
## 👤 Author

Tian Zhao, Ph.D.

AI/ML Engineer | Computer Vision | Scientific AI Systems

Focused on:

Vision Transformers (ViTs)
Scientific machine learning
Autonomous microscopy
Retrieval-Augmented Generation (RAG)
Local LLM systems

## License

MIT License.
