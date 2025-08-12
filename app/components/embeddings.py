from langchain_huggingface import HuggingFaceEmbeddings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)  # Initialize logger

def get_embedding_model():
    try:
        logger.info("Loading HuggingFace embedding model.")
        model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        logger.info("Embedding model loaded successfully.")
        return model
    except Exception as e:
        logger.error(f"Error loading embedding model: {e}")
        raise CustomException(f"Failed to load embedding model: {e}")