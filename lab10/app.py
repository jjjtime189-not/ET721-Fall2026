"""Joseph Ali-Shaw
October 13 2026
lab 10, intro to flask"""
from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)
@app.route('/')
def index():
    name = "JOSEPH ALI-SHAW"
    fruits =['apple','orange','grapes']
    return render_template('index.html', username=name, listfruits=fruits)
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/quotes')
def quotes():
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
