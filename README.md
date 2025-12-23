## 🔐 Environment Variables

Create a `.env` file (do NOT commit this):

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
PINECONE_API_KEY=xxxxxxxxxxxxxxxx
PINECONE_INDEX_NAME=simple-rag
PINECONE_ENV=us-east-1

Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate


Install dependencies:

pip install fastapi uvicorn python-dotenv pinecone openai python-multipart

Run the Application

Start FastAPI:

uvicorn main:app --reload


Open in browser:

http://127.0.0.1:8000


You should see:

A text box

Send button

Chat-style responses

// To stop
enter "deactivate" on terminal.

🌍 Expose App Using Ngrok

1️⃣ Install ngrok (once)
brew install ngrok


Authenticate:

ngrok config add-authtoken YOUR_NGROK_TOKEN

2️⃣ Start ngrok

In a new terminal:

ngrok http 8000


You’ll get a public URL like:

https://abcd-1234.ngrok-free.app


👉 Open this URL to access your RAG app publicly.