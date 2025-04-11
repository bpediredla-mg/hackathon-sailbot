from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.llms import LlamaCpp
import os

def load_documents_from_dir(directory):
    docs = []
    file_path = Path(directory)
    with open(file_path, "r", encoding="utf-8") as f:
        docs.append(f.read())

    return docs

def build_qa_chain():
    documents = load_documents_from_dir("output.json")
    splitter = CharacterTextSplitter(chunk_size=750, chunk_overlap=100)
    texts = splitter.create_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(texts, embeddings)
    retriever = db.as_retriever()

    llm = LlamaCpp(
        model_path="backend/models/tinyllama-gguf/tinyllama.gguf",
        n_ctx=1024,
        temperature=0.7,
        verbose=False
    )

    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain
