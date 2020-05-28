#!/usr/bin/python3.6
import sqlite3
db = sqlite3.connect("bus_route")
cursor=db.cursor()

def create_db():
    query="""
    CREATE TABLE student (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        gender TEXT NOT NULL
    );
"""
    cursor.execute(query)

    query="""
    CREATE TABLE bus_stand (
        bus_stand_name TEXT PRIMARY KEY,
        x INTEGER NOT NULL,
        y INTEGER NOT NULL
    );
"""
    cursor.execute(query)

    query="""
    CREATE TABLE bus (
        bus_name TEXT NOT NULL,
        route TEXT NOT NULL,
        time TEXT NOT NULL,
        info TEXT NOT NULL
    );
"""
    cursor.execute(query)


def insert_into_student(id,name,email,password,gender):
    print(f"'{id}', '{name}', '{email}', '{password}', '{gender}'")

    query=f"""
    INSERT INTO student
    (id,name,email,password,gender)
    VALUES ('{id}','{name}','{email}','{password}','{gender}');
"""
    try:
        cursor.execute(query)
        db.commit()

    except:
        print("Error inserting in student")
        db.rollback()


def insert_into_bus_stand(bus_stand_name,x,y):

    query=f"""
    INSERT INTO bus_stand
    (bus_stand_name,x,y)
    VALUES ('{bus_stand_name}',{x},{y});
"""
    try:
        cursor.execute(query)
        db.commit()
    except:
        print("Error insering in bus_stand")
        db.rollback()


def insert_into_bus(bus_name,route,time,info):
    query=f"""
    INSERT INTO bus
    (bus_name,route,time,info)
    VALUES ('{bus_name}','{route}','{time}','{info}');
"""
    #print(f" name: {bus_name}, time = {time}, {route},  {info}")
    try:
        cursor.execute(query)
        db.commit()
        return True
    except:
        print("Error inserting in bus")

        db.rollback()
        return False


def passcheck(id,password):
    if(id=="" or password==""):
        return False

    query=f"SELECT password FROM student WHERE id = '{id}'"
    cursor.execute(query)

    result =cursor.fetchone()
    if(result==None):
        return False
    elif (result[0]==''  or result[0] != password):
        return False
    else:
        return True
def isIdExists(id):
    query=f"SELECT name FROM student WHERE id = '{id}'"
    cursor.execute(query)
    result =cursor.fetchone()
    print(result)
    if(result==None):
        return False
    else:
        return True

def locationPoint(str):
    query=f"SELECT x,y FROM bus_stand WHERE bus_stand_name = '{str}'"
    try:
        cursor.execute(query)
        result=cursor.fetchone()
        return result
    except:
        print("Failed to find stand location point")
