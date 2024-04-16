# Write a program to insert a record in sql table via api
# Write a program to update a record in sql table via api
# Write a program to delete a record in sql table via api
# All the above operations should be done with mongodb as well

from flask import Flask, request, jsonify
import mysql.connector as connection

app = Flask(__name__)
# connection to mysql
mydb = connection.connect(host="localhost", user="root", passwd="Sinjo@123")
cursor = mydb.cursor()


# cursor.execute("create database if not exists tasksql")
# cursor.execute("CREATE TABLE IF NOT EXISTS tasksql.mysqltable (name VARCHAR(30), number INT(10))")
@app.route("/insert", methods=["POST"])
def insert():
    if request.method == "POST":
        name = request.json['name']
        number = request.json['number']
        cursor.execute(f"INSERT INTO tasksql.mysqltable VALUES ('{name}', {number})")
        mydb.commit()
        return jsonify("Record inserted successfully")


@app.route("/update", methods=["POST"])
def update():
    if request.method == "POST":
        name = request.json['name']
        number = request.json['number']
        cursor.execute(f"UPDATE tasksql.mysqltable SET number = {number} WHERE name = '{name}'")
        mydb.commit()
        return jsonify("Record updated successfully")


@app.route("/delete", methods=["POST"])
def delete():
    if request.method == "POST":
        name = request.json['name']
        cursor.execute(f"DELETE FROM tasksql.mysqltable WHERE name = '{name}'")
        mydb.commit()
        return jsonify("Record deleted successfully")


@app.route("/fetch", methods=["POST"])
def fetch():
    if request.method == "POST":
        name = request.json['name']
        cursor.execute(f"SELECT * FROM tasksql.mysqltable WHERE name = '{name}'")
        data = cursor.fetchall()
        return jsonify(data)


if __name__ == "__main__":
    app.run()
