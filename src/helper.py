from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

# Extract data from the pdf loader
def loadPdfFile(data):
    loader = DirectoryLoader(data,
                             glob="*pdf",
                             loader_cls=PyPDFLoader)
    documents = loader.load()

    return documents

# split the Data into text chunks
def text_split(extracted_data):
    text_spliter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap =20)
    text_chunks = text_spliter.split_documents(extracted_data)
    return text_chunks

# download the embedding from hugging face

def download_hugging_face_embedding():
    embedding = HuggingFaceEmbeddings(model_name ='sentence-transformers/all-MiniLM-L6-v2')
    return embedding
