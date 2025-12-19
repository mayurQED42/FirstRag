import os
from uuid import uuid4
from dotenv import load_dotenv
from pinecone import Pinecone
from openai import OpenAI

load_dotenv()

# OpenAI client
openai_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY").strip()
)

# Pinecone client
pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")
)

index = pc.Index(os.getenv("PINECONE_INDEX_NAME"))

documents = [
    "FastAPI is a modern Python web framework for building APIs.",
    "Pinecone is a vector database for similarity search.",
    "RAG combines retrieval with large language models."
]

def embed(text: str) -> list[float]:
    response = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

vectors = []
for doc in documents:
    vectors.append({
        "id": str(uuid4()),
        "values": embed(doc),
        "metadata": {"text": doc}
    })

index.upsert(vectors=vectors)

print("✅ Documents ingested successfully")

