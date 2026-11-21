from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    "host": "127.0.0.1",
    "user": "flaskuser",
    "password": "password123",
    "database": "todo_db",
}


def get_db_connection():
    return mysql.connector.connect(**db_config)


@app.route("/")
def index():
    try:
        with get_db_connection() as db:
            with db.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id, task FROM task")
                tasks = cursor.fetchall()
    except mysql.connector.Error:
        tasks = []
    return render_template("index.html", tasks=tasks)


@app.route("/get_tasks", methods=["GET"])
def get_tasks():
    try:
        with get_db_connection() as db:
            with db.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id, task FROM task")
                tasks = cursor.fetchall()
        return jsonify(tasks)
    except mysql.connector.Error as e:
        return jsonify({"error": str(e)}), 500


@app.route("/add_task", methods=["POST"])
def add_task():
    data = request.get_json(silent=True) or {}
    task = data.get("task", "").strip()
    if task:
        try:
            with get_db_connection() as db:
                with db.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO task (task) VALUES (%s)",
                        (task,),
                    )
                    db.commit()
            return jsonify({"status": "success"})
        except mysql.connector.Error as e:
            return jsonify({"error": str(e)}), 500
    return jsonify({"status": "error"}), 400


@app.route("/delete_task", methods=["POST"])
def delete_task():
    data = request.get_json(silent=True) or {}
    task_id = data.get("id")
    if not task_id:
        return jsonify({"status": "error"}), 400

    try:
        with get_db_connection() as db:
            with db.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM task WHERE id = %s",
                    (task_id,),
                )
                db.commit()
        return jsonify({"status": "deleted"})
    except mysql.connector.Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)