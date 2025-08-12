from langchain_groq import ChatGroq
from config.config import GROQ_API_KEY, MODEL

from common.logger import get_logger
from common.custom_exception import CustomException

logger = get_logger(__name__)  # Initialize logger

def load_groq_model(model_name:str=MODEL, api_key:str=GROQ_API_KEY):
    try:
        logger.info(f"Loading Groq model: {model_name}")
        model = ChatGroq(model=model_name, api_key=api_key, temperature=0.4)
        logger.info("Groq model loaded successfully.")
        return model
    except Exception as e:
        logger.error(f"Error loading Groq model: {e}")
        raise CustomException(f"Failed to load Groq model: {e}")