# chatbot.py
from dotenv import load_dotenv
load_dotenv()

from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings

def load_chatbot(db_path="faiss_index"):
    # Load the saved vector DB
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.load_local(db_path, embeddings)
    
    # Make the retriever and chatbot
    retriever = vectorstore.as_retriever()
    llm = ChatOpenAI(temperature=0)
    
    # Create a retrieval-based chatbot
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain
