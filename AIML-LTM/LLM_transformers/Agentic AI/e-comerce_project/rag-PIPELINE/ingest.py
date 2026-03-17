from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
def load_data():
    docs = []
    
    import json
    
    with open('data/faq.json') as f:
        faq = json.load(f)
        for item in faq:
            docs.append(f"Q: {item['question']} A: {item['answer']}")

    with open('data/policies.txt') as f:
        docs.append(f.read())

    with open('data/products.json') as f:
        products = json.load(f)
        for p in products:
            docs.append(f"{p['name']} costs {p['price']}")

    return docs

docs = load_data()

splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)
texts = splitter.split_text("\n".join(docs))

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

db = FAISS.from_texts(texts, embeddings)
db.save_local("vector_store")

print("Vector store created")
