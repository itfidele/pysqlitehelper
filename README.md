# PySQLite-Helper 🧤
![](https://img.shields.io/github/issues/fidele000/PySQLite-Helper)  ![](https://img.shields.io/github/forks/fidele000/PySQLite-Helper) [![GitHub stars](https://img.shields.io/github/stars/fidele000/PySQLite-Helper)](https://github.com/fidele000/PySQLite-Helper/stargazers)  [![GitHub license](https://img.shields.io/github/license/fidele000/PySQLite-Helper)](https://github.com/fidele000/PySQLite-Helper/blob/master/LICENSE)  

Python 💩💩 SQLiteHelper is a python package i created for my own needs, for repetition while accessing sqlite, it can help you to create database,tables accessing tables without needing any query 💩

# Example 💽
I'm sure if you know to to import python module, that's all you need on this or visit this link to learn more <a href='https://www.geeksforgeeks.org/import-module-python/#:~:text=Import%20in%20python%20is%20similar,is%20not%20the%20only%20way.'>Here</a> 
```python
# import the module from helper folder
from helper.sqlitehelper import SQLiteHelper

# creating the database called todo_app using our SQLiteHeper module 
db=SQLiteHelper('todo_app')
# After this like the file todo_app.db will be created in your directory

# Specify the structure of table you want to create using dictionary like this
columns = {
    'title': 'text',
    'description':'text',
    'completed':'boolean',
}

# create table using create_table function, and pass table name and of course the columns in the table 
db.create_table('tasks',columns)

# you want to insert data in your table right let's kee going
# specify values to be inserted in your table like this, column name then the value in dictionary format

values={
    'title':'Coding in the morning',
    'description':'Get up and code bro 😉',
    'completed':False,
}

# then to execute the insert method call this fuction and pass table name and it's value

db.insert('tasks',values)
# after this line, you are now inserted your data in your table 

# select data by ID , here i'm going to select todo with id of 2
todo=db.selectWhereId('tasks',2)
print(todo)
# you can display selected column like this print(todo['title'])

# select all datas and display it via console like this
for r in db.selectAll(table_name='tasks'):
    print(r)
```
