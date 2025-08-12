# RAG Medical Chatbot

This is a RAG (Retrieval-Augmented Generation) based medical chatbot developed on top of LangChain. The chatbot uses a large language model (LLM) to answer medical questions based on a given context. The context is retrieved from a vector store of medical documents.

## Description

The RAG Medical Chatbot is a web-based application that allows users to ask medical questions and receive answers from a large language model. The chatbot is designed to be used by medical professionals and students, and it can be used to answer questions about a wide range of medical topics.

The chatbot works by first retrieving relevant medical documents from a vector store. The vector store is a database of medical documents that have been indexed and stored in a way that makes them easy to search. Once the relevant documents have been retrieved, they are passed to a large language model, which then generates an answer to the user's question.

The chatbot is designed to be accurate and informative, and it can be used to answer a wide range of medical questions. However, it is important to note that the chatbot is not a substitute for professional medical advice, and it should not be used to diagnose or treat any medical conditions.

## Tech Stack

*   **Backend:** Flask
*   **LLM:** Groq
*   **Embeddings:** HuggingFace
*   **Vector Store:** FAISS
*   **PDF Loader:** PyPDFLoader
*   **Text Splitter:** RecursiveCharacterTextSplitter
*   **Dependencies:**
    *   langchain
    *   langchain_community
    *   langchain_huggingface
    *   langchain_groq
    *   faiss-cpu
    *   pypdf
    *   huggingface_hub
    *   flask
    *   python-dotenv
    *   sentence-transformers

## Architecture

The RAG Medical Chatbot has a simple architecture that consists of the following components:

*   **Frontend:** The frontend is a web-based interface that allows users to interact with the chatbot.
*   **Backend:** The backend is responsible for handling user requests, retrieving relevant documents from the vector store, and generating answers using the large language model.
*   **Vector Store:** The vector store is a database of medical documents that have been indexed and stored in a way that makes them easy to search.
*   **Large Language Model:** The large language model is responsible for generating answers to user questions.

## Installation

To install the RAG Medical Chatbot, you will need to have the following installed on your system:

*   Python 3.13 or higher
*   pip

Once you have installed the prerequisites, you can install the chatbot by following these steps:

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/rag-medical-chatbot.git
    ```
2.  Install the dependencies:
    ```bash
    pip install -e .
    ```
3.  Create a `.env` file in the root directory of the project and add the following environment variables:
    ```
    GROQ_API_KEY="your-groq-api-key"
    ```
4.  Run the application:
    ```bash
    python app/application.py
    ```

## Usage

To use the RAG Medical Chatbot, you will need to have a web browser installed on your system. Once you have installed the chatbot, you can access it by opening the following URL in your web browser:

```
http://localhost:5000
```

Once you have opened the chatbot, you can start asking medical questions. The chatbot will then generate an answer to your question based on the information in the vector store.

## Project Structure

The RAG Medical Chatbot has the following project structure:

```
.
├── app
│   ├── __init__.py
│   ├── application.py
│   ├── common
│   │   ├── __init__.py
│   │   ├── custom_exception.py
│   │   └── logger.py
│   ├── components
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   ├── embeddings.py
│   │   ├── llm.py
│   │   ├── pdf_loader.py
│   │   ├── retriever.py
│   │   └── vector_store.py
│   ├── config
│   │   ├── __init__.py
│   │   └── config.py
│   └── templates
│       └── index.html
├── custom_jenkins
│   └── Dockerfile
├── data
│   └── The_GALE_ENCYCLOPEDIA_of_MEDICINE_SECOND.pdf
├── logs
├── RAG_Medical_Chatbot.egg-info
├── vector_store
│   └── db_faiss
│       ├── index.faiss
│       └── index.pkl
├── .gitignore
├── Dockerfile
├── requirements.txt
└── setup.py
```

## Customization

The RAG Medical Chatbot can be customized in a number of ways. For example, you can change the large language model that is used to generate answers, or you can change the vector store that is used to store medical documents.

To change the large language model, you will need to modify the `app/components/llm.py` file. To change the vector store, you will need to modify the `app/components/vector_store.py` file.

## Troubleshooting

If you are having trouble with the RAG Medical Chatbot, you can try the following:

*   Make sure that you have installed all of the dependencies correctly.
*   Make sure that you have created a `.env` file and added your Groq API key.
*   Make sure that you have run the application correctly.

If you are still having trouble, you can open an issue on the GitHub repository.

## Future Scope

The RAG Medical Chatbot can be extended in a number of ways. For example, you could add a feature that allows users to upload their own medical documents to the vector store. You could also add a feature that allows users to ask questions in different languages.

## License

The RAG Medical Chatbot is licensed under the MIT License.


