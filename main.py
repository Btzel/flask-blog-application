from flask import Flask, render_template
from url import get_url_dict
import requests
response = requests.get("https://api.npoint.io/6bb4aea2f25211b762cd")
response.raise_for_status()
blog_data_json = response.json()

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def home():
    url_dict = get_url_dict()
    return render_template('index.html',url=url_dict,blog_posts=blog_data_json)

@app.route('/post/<int:blog_id>.html')
def post(blog_id):
    url_dict = get_url_dict()
    for blog in blog_data_json:
        if blog['id'] == blog_id:
            return render_template('post.html',url=url_dict,blog_post=blog)

@app.route('/about.html')
def about():
    url_dict = get_url_dict()
    return render_template('about.html',url=url_dict)

@app.route('/contact.html')
def contact():
    url_dict = get_url_dict()
    return render_template('contact.html', url=url_dict)



if __name__ == '__main__':
    app.run(debug=True)
