"""
This is a simple blog application that allows users to create, update, and delete blog posts.
"""
from flask import Flask, json, request, render_template, redirect, url_for

app = Flask(__name__)

class DBase:
    """
    This class is used to read and write data from a JSON file.
    """
    def __init__(self, path):
        """
        Initialize the database with the path to the JSON file.
        """
        self.path = path

    def read(self):
        """
        Read data from the JSON file.
        """
        with open(self.path, "r", encoding="utf-8") as file:
            return json.load(file)

    def write(self, data):
        """
        Write data to the JSON file.
        """
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def next_id(self):
        """
        Get the next ID for a new post.
        """
        posts = self.read()
        return max((post.get("id", 0) for post in posts), default=0) + 1

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
    """
    This function handles deleting a blog post.
    """
    posts = db.read()
    deleted = [p for p in posts if p.get("id") != post_id]
    db.write(deleted)
    return redirect(url_for('index'))

def fetch_post_by_id(post_id):
    """
    This function handles fetching a blog post by ID.
    """
    posts = db.read()
    found_post = None
    for post in posts:
        if post.get("id") == post_id:
            found_post = post
            break
    return found_post

@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """
    This function handles updating a blog post.
    """
    # Fetch the blog posts from the JSON file
    if post is None:
        # Post not found
        return "Post not found", 404

    if request.method == 'POST':
        # Update the post in the JSON fil
        posts = db.read()

        for post in posts:
            if post.get("id") == post_id:
                post["title"] = request.form.get("title")
                post["author"] = request.form.get("author")
                post["content"] = request.form.get("content")
                break
        # Redirect back to index
        db.write(posts)
        return redirect(url_for('index'))
    # So display the update.html page
    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
