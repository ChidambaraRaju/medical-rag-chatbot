import os
from app.components.pdf_loader import load_pdf_files, create_chunks
from app.components.vector_store import save_vector_store
from app.config.config import DB_FAISS_PATH
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)  # Initialize logger

def process_and_store_pdfs():
    try:
        logger.info("Creating vector store from PDF files...")
        documents = load_pdf_files()
        chunks = create_chunks(documents)
        vector_store = save_vector_store(chunks)
        logger.info("Vector store created and saved successfully.")
        return vector_store
    except Exception as e:
        logger.error(f"Error processing and storing PDF files: {e}")
        raise CustomException(f"Failed to process and store PDF files: {e}")
    
if __name__ == "__main__":
    process_and_store_pdfs()