from langchain.vectorstores import pinecone
from langchain import HuggingFaceHub
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceHub(repo_id = 'google/flan-t5-large')

pinecone.init(
                api_key='b2664173-eaee-4800-b14e-db17bd33c2a5',
              )