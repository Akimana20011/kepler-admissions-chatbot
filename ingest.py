# ingest.py

import pandas as pd
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def create_vector_db(file_path="kepler_data/Chatbot Questions & Answers.xlsx", db_path="faiss_index"):
    # Load Excel data
    df = pd.read_excel(file_path)

    # Turn each row into a Document object with Q&A
    docs = [
        Document(page_content=f"Q: {row['Questions']}\nA: {row['Answers']}")
        for _, row in df.iterrows()
    ]

    # Split large texts into manageable chunks
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(docs)

    # Create and save the vector database
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(split_docs, embeddings)
    db.save_local(db_path)
    print("✅ Vector DB created and saved at", db_path)

# Run the function
if __name__ == "__main__":
    create_vector_db()
