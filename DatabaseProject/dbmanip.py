import sqlite3
import bcrypt
from flask import Flask, jsonify
def viewAllUsers():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    query = "SELECT id, username, first_name, last_name, role FROM users"
    cursor.execute(query)
    out = cursor.fetchall()
    s = 'id uName fName lName role<br>'
    for all in out:
        s = s + str(all) + "<br>"
    conn.close()
    return s

def viewIdUser(id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    query = "SELECT id, username, first_name, last_name, role FROM users WHERE id = ?"
    cursor.execute(query,id)
    out = cursor.fetchall()
    s = 'id uName fName lName role<br>'
    for all in out:
        s = s + str(all) + "<br>"
    conn.close()
    return s

def viewChecked(id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    query = "SELECT title, format, author FROM items WHERE borrower = ?"
    cursor.execute(query,(id,))
    out = cursor.fetchall()
    s = "Title  Format  Author<br>"
    for all in out:
        s = s + str(all) + "<br>"
    conn.close()
    return s

def addUser(uN,pss,fN,lN,role):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    byte =pss.encode('utf-8')
    password1_hash = bcrypt.hashpw(byte, bcrypt.gensalt())
    cursor.execute(
       "INSERT INTO users (username, password, first_name, last_name, role) VALUES (?, ?, ?, ?, ?)",
       (uN, password1_hash, fN, lN, role))
    #cursor.execute(query,id)
    s = 'User added'
    conn.commit()
    conn.close()
    return s

def addItem(title,format,author):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (title, format, author) VALUES (?, ?, ?)",
        (title,format,author))
    #cursor.execute(query,id)
    s = 'item added'
    conn.commit()
    conn.close()
    return s

def searchItem(title):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    query = "SELECT title, format, author FROM items WHERE title = ?"
    cursor.execute(query,(title,))
    out = cursor.fetchone()
    s = "Title  Format  Author<br>" +str(out)
    conn.close()
    return s

def browseItem():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    query = "SELECT title, format, author FROM items"
    cursor.execute(query)
    out = cursor.fetchall()
    s = "Title  Format  Author<br>"
    for all in out:
        s = s + str(all) + "<br>"
    conn.close()
    return s

def checkOut(title,id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM items WHERE borrower = ?"
    cursor.execute(query,(id,))
    out = cursor.fetchone()
    check = sum(out)
    s = ''
    if (check >= 5):
        s = 'You have hit your limit of 5 items checked out, you may no longer check any out'
        conn.close()
        return s
    query = "SELECT borrower FROM items WHERE title = ?"
    cursor.execute(query,(title,))
    out = cursor.fetchone()
    check = str(out)
    print(check)
    if (check != "(None,)"):
        s = 'This book has already been checked out by another user'
        conn.close()
        return s
    query = "UPDATE items SET borrower = ? WHERE title = ?"
    cursor.execute(query,(id,title,))
    s = "you have successfully checked out your item"
    conn.commit()
    conn.close()
    return s
