# All the  operations should be done with mongodb as well using api
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)
# connect to mongodb
uri = ("mongodb+srv://vaibhavthaplidoon:Singhthapli@vaibhav.w1yhlwd.mongodb.net/?retryWrites=true&w=majority&appName"
       "=vaibhav")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# create database
database = client['tasktb']
# create table
collection = database['taskcollection']


@app.route("/insert", methods=["POST"])
def insert():
    if request.method == "POST":
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({"name": name, "number": number})
        return jsonify("Record inserted successfully")


if __name__ == "__main__":
    app.run(port=5000)