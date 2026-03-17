from langchain_community.vectorstores import FAISS
from ingest import embeddings

# NOTE: FAISS stores its index in a pickle file, which can be a security risk if the file is untrusted.
# Set allow_dangerous_deserialization=True only when you trust the source of the index (e.g., it was created by you).
db = FAISS.load_local("vector_store", embeddings, allow_dangerous_deserialization=True)

query = "Can I return a laptop?"
results = db.similarity_search(query, k=2)

for r in results:
    print(r.page_content)
