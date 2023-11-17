# PySQLite-Helper 🧤
![](https://img.shields.io/github/issues/fidele000/PySQLite-Helper)  ![](https://img.shields.io/github/forks/fidele000/PySQLite-Helper) [![GitHub stars](https://img.shields.io/github/stars/fidele000/PySQLite-Helper)](https://github.com/fidele000/PySQLite-Helper/stargazers)  [![GitHub license](https://img.shields.io/github/license/fidele000/PySQLite-Helper)](https://github.com/fidele000/PySQLite-Helper/blob/master/LICENSE)  

Python SQLiteHelper is a python package that help you to create sqlite databases,tables and interacting with sqlite database without have to worry about writing any SQL query.


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
    'description':'Drinking coffee instead',
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
