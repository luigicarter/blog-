from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
api_url = "https://api.npoint.io/deaf557de3ea833c4e57"
blog_objects = requests.get(api_url).json()


blog_list = []
for n in blog_objects:
    blog_stuff = Post(n["id"], n["title"], n["subtitle"], n["body"])
    blog_list.append(blog_stuff)



@app.route('/')
def home():
    post = requests.get(api_url).json()
    return render_template("index.html", all_post=post)

@app.route('/blog/<int:blog_post>')
def get_blog(blog_post):
    requested_post = None
    for g in blog_list:
        if g.id == blog_post:
            requested_post = g
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
