import pandas as pd

import mysql.connector as connection


mydb = connection.connect(host="localhost", database="tasksql", user="root", passwd="Sinjo@123")
cursor = mydb.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS tasksql.dresssales (Dress_ID int(20), Style VARCHAR(20), Price VARCHAR(10), Rating FLOAT(5), SIZE VARCHAR(10),Season VARCHAR(15), NeckLine VARCHAR(20), SleeveLength VARCHAR(20), waiseline VARCHAR(20),Material VARCHAR(20), FabricType VARCHAR(20), Decoration VARCHAR(20),PatternType VARCHAR(20), Recommendation VARCHAR(20))")

df = pd.read_csv("fo.csv")
# Iterate over DataFrame rows and insert into MySQL table
for index, row in df.iterrows():
    cursor.execute("INSERT INTO dresssales (Dress_ID, Style, Price, Rating, SIZE, Season, NeckLine, SleeveLength, waiseline, Material, FabricType, Decoration, PatternType, Recommendation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   tuple(row))

# Commit changes and close connection
mydb.commit()
mydb.close()

print("Data inserted successfully.")