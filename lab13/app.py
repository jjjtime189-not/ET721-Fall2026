from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
# Display blogs

@app.route('/blogs')
def blogs():
    cursor.execute("SELECT blog.id,
    users.username, blog.title,
    blog.content, blog.created_at FROM blog JOIN users ON
    blog.user_id = users.userid")
    # get all the data and store them in 'data'
    data = cursor.fetchall()
    return render_template('blogs.html', blogs = data)
@app.route('/add_blog', methods =['get', 'post'])
def add_blog():
    username = request.form['username']
    email = request.form['email']
    title = request.form['title']
    content = request.form['content']
    cursor.execute("INSERT INTO users(username, email) VALUES(%s, %s)",(username,email))
    db.commit()
    user_id = cursor.lastrowid
    cursor.execute("INSERT INTO blog(user_id, title, content) VALUES(%s, %s, %s)", (user_id,title,content))
    db.commit()
    return redirect('/blogs')