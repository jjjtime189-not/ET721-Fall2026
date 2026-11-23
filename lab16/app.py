import os
from flask import Flask, render_template, request, jsonify
import mysql.connector
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.config['upload_folder'] = 'static/uploads'
app.config['max_content_length'] = 16 * 1024 * 1024
allowed_extensions = {'png','jpg','jpeg','gif'}
db_config = {
    'host':'localhost',
    'user':'flaskuser',
    'password':'password123',
    'database':'image_app'
}
def get_db_connection():
    return mysql.connector.connect(**db_config)
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in allowed_extensions
@app.route('/')
def index():
    return render_template('index.html')
    #conn = get_db_connection()
    #cursor = conn.cursor(dictionary=True)
    #cursor.execute("select * from images order by uploaded_at desc")

if __name__ =='__main__':
    app.run(debug=True)