import numpy as np
import pandas as pd
import mysql.connector

df = pd.read_csv('https://drive.google.com/file/d/1mcHccwN__a5Il3VnhyuArNqozPDJny6y/view?usp=sharing')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="BabylonXX3007",
    database='bank')

print(mydb)

cur = mydb.cursor()
cur.execute('DROP TABLE IF EXISTS products')
cur.execute('CREATE TABLE products (Name varchar(50), sku varchar(50), description text, PRIMARY KEY(sku))')
mydb.commit()
for row in df.itertuples():
    sql = f"""INSERT INTO products(name, sku, description) VALUES {row[1:]} ON DUPLICATE KEY UPDATE name='{row[1:][0]}', description='{row[1:][2]}'"""
    cur.execute(sql)
    mydb.commit()


