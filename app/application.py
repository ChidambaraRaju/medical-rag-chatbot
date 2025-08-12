from flask import Flask, render_template, request, session, redirect, url_for
from app.components.retriever import create_retrieval_chain
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Set a secret key for session management

from markupsafe import Markup
def nl2br(text):
    """Convert newlines to <br> tags for HTML rendering."""
    return Markup(text.replace('\n', '<br>\n'))

app.jinja_env.filters['nl2br'] = nl2br

@app.route('/', methods=['GET', 'POST'])
def index():
    if "message" not in session:
        session["message"] = []
    if request.method == 'POST':
        user_input = request.form.get('prompt')
        if user_input:
            message = session["message"]
            message.append({"role": "user", "content": user_input})
            session["message"] = message
            
            try:
                qa_chain = create_retrieval_chain()
                response = qa_chain.invoke({"query": user_input})
                result = response.get("result", "No answer found.")
                message.append({"role": "assistant", "content": result})
                session["message"] = message
            except Exception as e:
                error_message = f"An error occurred: {str(e)}"
                return render_template('index.html', messages=session["message"], error=error_message)
                
        return redirect(url_for('index'))
    return render_template('index.html', messages=session.get("message", []))

@app.route('/clear')
def clear():
    session.pop('message', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False) # Ensure debug=False for production, use_reloader=False to avoid double execution
    