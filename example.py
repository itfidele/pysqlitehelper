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

# select all datas and display it via console like this
for r in db.selectAll(table_name='tasks'):
    print(r)