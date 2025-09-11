from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Página Inicial</title>
        </head>
        <body>
            <h1>Curso Desenvolvedor Back-end</h1>
            <p>Luiz Carlos</p>
            <p>DATA: 08/09/2025 </p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
