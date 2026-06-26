import gradio as gr
import time

from app.rag_pipeline import RAGPipeline


# ===================================
# LOAD RAG
# ===================================
print("Loading Scientific RAG...")

rag = RAGPipeline()

print("RAG Ready")


# ===================================
# CHAT
# ===================================
def chat(user_input, history):

    if history is None:
        history = []

    if not user_input.strip():
        yield "", history
        return

    try:
        # -------------------------
        # Run RAG
        # -------------------------
        result = rag.ask(user_input)

        answer = result["answer"]
        sources = result["sources"]

        # -------------------------
        # Format sources
        # -------------------------
        source_text = "\n\n📚 Sources:\n"

        if len(sources) == 0:
            source_text += "\nNo relevant chunks found."

        else:
            for i, s in enumerate(sources):

                payload = s.get("payload", s) if isinstance(s.get("payload"), dict) else s
                source_file = payload.get("source", "Unknown File")
                page = payload.get(
                    "page",
                    "Unknown"
                )

                text = payload.get(
                    "text",
                    ""
                )

                preview = (
                    text[:200]
                    .replace("\n", " ")
                    .strip()
                )

                source_text += (
                    f"\n[{i+1}] {source_file} | Page {page}\n"
                    f'"{preview}..."\n'
                )

        full_response = answer + source_text

    except Exception as e:

        full_response = f"❌ Error:\n{str(e)}"

    # -------------------------
    # MESSAGE FORMAT
    # -------------------------
    history.append({
        "role": "user",
        "content": user_input
    })

    history.append({
        "role": "assistant",
        "content": ""
    })

    partial = ""

    for word in full_response.split():

        partial += word + " "

        history[-1]["content"] = partial

        time.sleep(0.01)

        yield "", history
# ===================================
# CLEAR
# ===================================
def clear():
    return []


# ===================================
# UI
# ===================================
with gr.Blocks() as demo:

    gr.Markdown(
        "# 🧠 Scientific RAG Assistant"
    )

    gr.Markdown(
        "Query PDFs using "
        "Local LLaMA + Qdrant"
    )

    chatbot = gr.Chatbot(
        height=600,
        value=[],
    )

    user_input = gr.Textbox(
        label="Message",
        placeholder="Ask a question about your PDF..."
    )

    clear_btn = gr.Button(
        "Clear Chat"
    )

    user_input.submit(
        chat,
        inputs=[
            user_input,
            chatbot
        ],
        outputs=[
            user_input,
            chatbot
        ]
    )

    clear_btn.click(
        clear,
        outputs=chatbot
    )


# ===================================
# RUN
# ===================================
if __name__ == "__main__":

    demo.launch(
        inbrowser=True
    )
