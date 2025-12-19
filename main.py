from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from rag import ask_rag

app = FastAPI()

# Simple in-memory chat history (per server, not persistent)
chat_history = []

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>RAG Chat</title>
    <style>
        body {{ font-family: Arial; margin: 40px; }}
        textarea {{ width: 100%; height: 60px; }}
        .chat {{ max-width: 800px; }}
        .user {{ background: #daf1ff; padding: 10px; margin-top: 10px; }}
        .bot {{ background: #f1f1f1; padding: 10px; margin-top: 5px; }}
    </style>
</head>
<body>
    <div class="chat">
        <h2>RAG Chat</h2>

        {chat_messages}

        <form method="post">
            <textarea name="question" placeholder="Ask something..."></textarea><br><br>
            <button type="submit">Send</button>
        </form>
    </div>
</body>
</html>
"""

def render_chat():
    html = ""
    for msg in chat_history:
        html += f"<div class='user'><b>You:</b> {msg['question']}</div>"
        html += f"<div class='bot'><b>Bot:</b> {msg['answer']}</div>"
    return html

@app.get("/", response_class=HTMLResponse)
def home():
    return HTML_PAGE.format(chat_messages=render_chat())

@app.post("/", response_class=HTMLResponse)
def chat(question: str = Form(...)):
    answer = ask_rag(question)

    chat_history.append({
        "question": question,
        "answer": answer
    })

    return HTML_PAGE.format(chat_messages=render_chat())

