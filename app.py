from flask import Flask, request, render_template, redirect, url_for
import json

app = Flask(__name__)

class DBase:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def write(self, data):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def next_id(self):
        posts = self.read()
        return max((p.get("id", 0) for p in posts), default=0) + 1

db = DBase("data/my_blog_posts.json")


@app.route('/')
def index():
    """
    This function displays the blog posts from the JSON file.
    """
    return render_template('index.html', posts=db.read())

@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    This function handles adding a new blog post.
    """
    if request.method == 'POST':
        posts = db.read()

        new_post = {
            "id": db.next_id(),
            "title": request.form.get("title"),
            "author": request.form.get("author"),
            "content": request.form.get("content")
        }

        posts.append(new_post)
        db.write(posts)

        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/delete/<int:post_id>')
def delete(post_id):
   posts = db.read()
   updated = [p for p in posts if p.get("id") != post_id]
   db.write(updated)
   return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
