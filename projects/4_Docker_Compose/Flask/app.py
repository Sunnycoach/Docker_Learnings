from flask import Flask
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Sunny, Welcome to Flask"

@app.route('/insertdata')
def insert_data():
    
    #connect to database
    connection = pymysql.connect(
        host='mysqlcontainer',
        user='root',
        password='demopassword',
        database='demodb'
    )

    #cursor object
    cursor = connection.cursor()

    insert_query = "INSERT INTO customers (Name,city) VALUES (%s, %s)"

    data = ("Sunny","Bangalore")

    cursor.execute(insert_query,data)

    connection.commit()
    cursor.close()
    connection.close()

    return "Data inserted Successfully!"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)





