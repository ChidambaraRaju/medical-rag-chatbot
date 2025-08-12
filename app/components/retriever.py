from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

from app.components.llm import load_groq_model
from app.components.vector_store import load_vector_store

from app.config.config import MODEL, GROQ_API_KEY
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)  # Initialize logger

CUSTOM_PROMPT_TEMPLATE = """
You are a medical information assistant. Answer the following medical question in 2-3 sentences maximum, 
using only the information provided in the context below.

If the context does not contain enough information to answer fully, respond with:
"I could not find sufficient information in the provided medical references to answer your question."

Do not add any information from outside the context. Do not speculate. Keep your language clear and factual.

Context:
{context}

Question:
{question}

Answer:
"""

def set_custom_prompt():
    """Set the custom prompt template for the RetrievalQA chain."""
    return PromptTemplate(
        input_variables=["context", "question"],
        template=CUSTOM_PROMPT_TEMPLATE
    )
    
def create_retrieval_chain():
    """Create a RetrievalQA chain with the custom prompt and Groq model."""
    try:
        logger.info("Loading vector store...")
        vector_store = load_vector_store()
        if not vector_store:
            raise CustomException("Vector store is empty or not found.")
        
        logger.info("Loading Groq model...")
        model = load_groq_model(MODEL, GROQ_API_KEY)
        if not model:
            raise CustomException("Failed to load Groq model.")
        
        logger.info("Setting up RetrievalQA chain with custom prompt...")
        prompt = set_custom_prompt()
        
        retrieval_chain = RetrievalQA.from_chain_type(
            llm=model,
            chain_type="stuff", # Using 'stuff' chain type for simplicity
            retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
            return_source_documents=False,
            chain_type_kwargs={"prompt": prompt}
        )
        
        logger.info("RetrievalQA chain created successfully.")
        return retrieval_chain
    except Exception as e:
        logger.error(f"Error creating RetrievalQA chain: {e}")
        raise CustomException(f"Failed to create RetrievalQA chain: {e}")
