import os
import google.generativeai as genai
from dotenv import load_dotenv
from flask import Flask, request, render_template

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)

def api_para_girias(prompt) -> str: 
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        giria = request.form.get("giria")
        resposta = api_para_girias(giria)
        return render_template("resultado.html",resposta=resposta)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)