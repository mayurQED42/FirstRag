## 🔐 Environment Variables

Create a `.env` file (do NOT commit this):

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
PINECONE_API_KEY=xxxxxxxxxxxxxxxx
PINECONE_INDEX_NAME=simple-rag
PINECONE_ENV=us-east-1

Create and activate a virtual environment:

python -m venv .venv
source .venv/bin/activate


Install dependencies:

pip install fastapi uvicorn python-dotenv pinecone-client openai

Run the Application

Start FastAPI:

uvicorn main:app --reload


Open in browser:

http://127.0.0.1:8000


You should see:

A text box

Send button

Chat-style responses
