from flask import Flask, request, render_template, redirect, url_for
import json

app = Flask(__name__)



@app.route('/')
def index():
    """
    This function displays the blog posts from the JSON file.
    """
    with open('data/my_blog_posts.json', 'r', encoding="utf-8") as posts_file:
        blog_posts = json.load(posts_file)
    return render_template('index.html', posts=blog_posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    This function handles adding a new blog post.
    """
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')

        with open('data/my_blog_posts.json', 'r', encoding="utf-8") as posts_file:
            blog_posts = json.load(posts_file)

        # Generate a new ID
        if blog_posts:
            new_id = None
            for post in blog_posts:
                if post.get("id") == None:
                    new_id = 1
                else:
                    new_id = post.get("id") + 1
        else:
            new_id = 1

        new_post = {
            'id': new_id,
            'author': author,
            'title': title,
            'content': content
        }

        blog_posts.append(new_post)
        with open('data/my_blog_posts.json', 'w', encoding="utf-8") as posts_file:
            json.dump(blog_posts, posts_file, indent=4)

        return redirect(url_for('index'))

    return render_template('add.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
