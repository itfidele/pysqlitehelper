import sqlite3
import logging

class SQLiteHelper(object):
    def __init__(self,db_name:str):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name+'.db')
        self.c=self.conn.cursor()
        
    def create_table(self,table_name:str,columns:str):
        """
            create 
        """
        query='('
        query+='id INTEGER PRIMARY KEY'
        for key, value in columns.items():
            query+=','+key+' '+value
        query+=')'
        self.c.execute("CREATE TABLE IF NOT EXISTS " + table_name+' '+query)
        self.conn.commit()

    
    def selectAll(self,table_name:str)->list:
        query="SELECT * FROM "+table_name
        return self.c.execute(query).fetchall()

    def getColumns(self,table_name:str)->list:
        cursor = self.c.execute('select * from '+table_name)
        return list(map(lambda x: x[0], cursor.description))

    def selectWhereId(self,table_name:str,id:int)->dict:
        query="SELECT * FROM "+table_name
        query+=' where id='+str(id)
        cursor=self.c.execute(query).fetchone()
        columns=self.getColumns(table_name)
        data={}
        
        if len(columns) > 0:
            for i in range(0,len(columns)):
                data[columns[i]]=cursor[i]
        return data

    def insert(self,table_name,values)->bool:
        try:
            query='('
            query+='id'
            values_="("
            values_+='NULL'
            for key,value in values.items():
                values_+=",'"+str(value)+"'"
                query+=','+key
            query+=')'
            values_+=")"
            self.c.execute("INSERT INTO "+table_name+query+"VALUES"+values_)
            self.conn.commit()
            return True
        except Exception as e:
            logging.exception(e)
            return False
    

    def table_exists(self,table_name):
        query="SELECT count(name) FROM sqlite_master WHERE type='table' AND name='"+table_name+"'"
        self.c.execute(query)
        if self.c.fetchone()[0]==1:
            return True
        return False
    
