import sqlite3
import os


def get_hash(login):
    connection = sqlite3.connect('data/database.db')
    request='''
               SELECT hash FROM users
                WHERE login="'''+login+'"'
    cursor = connection.execute(request)
    for x in cursor:
        hash=x[0]
    
    connection.commit()
    connection.close()
    return hash

def add_user(login,password):
    stream = os.popen('./hachage '+password)
    hash = stream.read()
    connection = sqlite3.connect('data/database.db')
    
    request='''
    INSERT INTO users (login,hash)
       VALUES ("'''+login+'", '+hash+')'
    print(request)
       
    cursor = connection.execute(request)
    connection.commit()
    connection.close()
    
add_user('admin','admin')
    
