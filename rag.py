import os
from dotenv import load_dotenv
from pinecone import Pinecone
from openai import OpenAI

load_dotenv()

openai_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY").strip()
)

pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")
)

index = pc.Index(os.getenv("PINECONE_INDEX_NAME"))

def embed(text: str) -> list[float]:
    response = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def ask_rag(question: str) -> str:
    query_embedding = embed(question)

    results = index.query(
        vector=query_embedding,
        top_k=3,
        include_metadata=True
    )

    context = "\n".join(
        match["metadata"]["text"] for match in results["matches"]
    )

    completion = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Answer using the context below."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{question}"}
        ]
    )

    return completion.choices[0].message.content

