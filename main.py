from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from url import get_url_dict
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
ckeditor = CKEditor(app)
Bootstrap5(app)


class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
@app.route('/index.html')
def home():
    url_dict = get_url_dict()
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template('index.html',url=url_dict,blog_posts=posts)

@app.route('/post/<int:blog_id>.html')
def post(blog_id):
    url_dict = get_url_dict()
    requested_blog_post = db.get_or_404(BlogPost,blog_id)
    print(requested_blog_post.body)
    return render_template('post.html',url=url_dict,blog_post=requested_blog_post)


@app.route('/post/new-post',methods=["GET","POST"])
def create_new_post():
    url_dict = get_url_dict()
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=form.author.data,
            date=date.today().strftime("%B %d, %Y")
        )
        print(new_post.date)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template('make-post.html',url=url_dict,form=form)

@app.route("/post/edit/<int:post_id>", methods=["GET", "POST"])

@app.route('/about.html')
def about():
    url_dict = get_url_dict()
    return render_template('about.html',url=url_dict)

@app.route('/contact.html')
def contact():
    url_dict = get_url_dict()
    return render_template('contact.html', url=url_dict)



if __name__ == '__main__':
    app.run(debug=True,port=5001)
