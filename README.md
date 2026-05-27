# 🧠 Scientific RAG Assistant (Local LLaMA + Qdrant)

A fully local **Retrieval-Augmented Generation (RAG)** system for querying scientific documents using **LLaMA 3.2**, **Qdrant**, and **semantic vector retrieval**.

This project enables natural-language question answering over large PDF documents (e.g., textbooks, research papers, technical manuals) while grounding responses in retrieved document context.

Built with:

- **LLaMA 3.2 3B Instruct** (4-bit quantized)
- **Qdrant Vector Database**
- **BAAI/bge-small-en-v1.5 Embeddings**
- **PyTorch + Transformers**
- **Docker**
- **Gradio UI**

---

## 🚀 Features

✅ Fully local inference (no OpenAI API required)  
✅ PDF → chunk → embed → vector database pipeline  
✅ Semantic retrieval using vector similarity search  
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
 Semantic Retrieval
      ↓
 Prompt Construction
      ↓
 LLaMA 3.2 (4-bit)
      ↓
 Grounded Answer
