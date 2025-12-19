from rag import ask_rag

while True:
    q = input("Ask a question (or 'exit'): ")
    if q.lower() == "exit":
        break
    print("\nAnswer:")
    print(ask_rag(q))
    print("-" * 40)

