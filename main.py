from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
response.raise_for_status()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", articles_json=response.json())

@app.route('/post/<int:article_id>')
def post(article_id):
    for article in response.json():
        print(article_id)
        print(article['id'])
        if article_id == article['id']:
            return render_template("post.html",article_json=article)

if __name__ == "__main__":
    app.run(debug=True)
