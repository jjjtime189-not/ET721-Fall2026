from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)
db_config = {
    'host': '127.0.0.1',
    'user':'root',           
    'password':'password',
    'database': 'employee_data'
}
@app.route('/', methods=['GET', 'POST'])
def index_joseph():
    final_salary = None
    
    if request.method == 'POST':
        name = request.form.get('name')
        id = request.form.get('id')
        salary = float(request.form.get('salary'))
        final_salary = salary * 1.05        
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            
            # Parameterized SQL query placeholder to protect against SQL Injection
            insert_query = """
                INSERT INTO employee_salary (employee_name, employee_id, salary) 
                VALUES (%s, %s, %s)
            """
            data = (name, id, salary)
            
            cursor.execute(insert_query, data)
            conn.commit()
            
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()
                
    # Display the HTML form when page opens (GET) or when re-rendered with results (POST)
    return render_template('index_joseph.html', final_salary=final_salary)

if __name__ == '__main__':
    app.run(debug=True)