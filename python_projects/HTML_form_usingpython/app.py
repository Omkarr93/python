
import mysql.connector
from flask import Flask , render_template, request


db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Pass@123",
    database="omkar_db"
)


# @app.route('/')
# def index():
#     return render_template('form.html')
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        emp_name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        age = request.form['age']
        department = request.form['department']
        
        
        cursor = db.cursor()
        cursor.execute("INSERT INTO employees ( emp_name, email, phone, age, department) VALUES (%s, %s, %s,%s, %s)", (emp_name, email, phone, age, department))
        db.commit()
        
        return "Message submitted successfully!"
    
    return render_template('form1.html')

if __name__ == '__main__':
    app.run(debug=True)



