import os
from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.common.logger import get_logger
from app.common.custom_exception import CustomException
from app.config.config import DATA_PATH, CHUNK_SIZE, CHUNK_OVERLAP

logger = get_logger(__name__) # Initialize logger

def load_pdf_files():
    try:
        if not os.path.exists(DATA_PATH):
            raise CustomException(f"Data path '{DATA_PATH}' does not exist.")
        logger.info(f"Loading PDF files from {DATA_PATH}")
        loader = DirectoryLoader(
            path= DATA_PATH,
            glob="*.pdf",
            loader_cls=PyPDFLoader
        )
        documents = loader.load()
        if not documents:
            logger.warning("No PDF files found in the specified directory.")
        else:
            logger.info(f"Loaded {len(documents)} PDF files.")
            
        return documents
    except Exception as e:
        logger.error(f"Error loading PDF files: {e}")
        raise CustomException(f"Failed to load PDF files: {e}")
    
    
def create_chunks(documents):
    try:
        if not documents:
            raise CustomException("No documents to chunk.")
        logger.info(f"Splitting {len(documents)} documents into chunks.")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )
        chunks = text_splitter.split_documents(documents)
        logger.info(f"Created {len(chunks)} chunks from documents.")
        
        return chunks
    except Exception as e:
        logger.error(f"Error creating chunks: {e}")
        raise CustomException(f"Failed to create chunks: {e}")