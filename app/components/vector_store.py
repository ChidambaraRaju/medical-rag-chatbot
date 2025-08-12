from langchain_community.vectorstores import FAISS
from app.components.embeddings import get_embedding_model
from app.common.logger import get_logger
from app.common.custom_exception import CustomException
from app.config.config import DB_FAISS_PATH

import os

logger = get_logger(__name__)  # Initialize logger

def load_vector_store():
    try:
        embedding_model = get_embedding_model()
        if os.path.exists(DB_FAISS_PATH):
            logger.info(f"Loading vector store from {DB_FAISS_PATH}")
            vector_store = FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)
            logger.info("Vector store loaded successfully.")
            return vector_store
        else:
            logger.warning(f"Vector store path '{DB_FAISS_PATH}' does not exist.")
       
    except Exception as e:
        logger.error(f"Error loading vector store: {e}")
        raise CustomException(f"Failed to load vector store: {e}")
    
def save_vector_store(text_chunks): # Creating a new vector store
    try:
        if not text_chunks:
            raise CustomException("No text chunks to save.")
        logger.info("Generating new vector store.")
        embedding_model = get_embedding_model()
        db = FAISS.from_documents(text_chunks, embedding_model)
        db.save_local(DB_FAISS_PATH)
        logger.info("Vector store saved successfully.")
        return db
    except Exception as e:
        logger.error(f"Error saving vector store: {e}")
        raise CustomException(f"Failed to save vector store: {e}")
