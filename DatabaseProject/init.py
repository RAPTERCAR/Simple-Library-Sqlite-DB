import sqlite3
import bcrypt

def sys_init():
    #connect to database
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

   # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT,
            first_name TEXT,
            last_name TEXT,
            role TEXT
        )
    ''')
    cursor.execute('''
         CREATE TABLE IF NOT EXISTS items (
            item_id INTEGER PRIMARY KEY,
            title TEXT UNIQUE,
            format TEXT,
            author TEXT,
            borrower INTEGER,
            FOREIGN KEY(borrower) REFERENCES users(id)
        )             
    ''')
    
    #hashpw creates a hashed version of password to store
    password1_hash = bcrypt.hashpw(b'secret1', bcrypt.gensalt())
    password2_hash = bcrypt.hashpw(b'secret2', bcrypt.gensalt())
    # Insert some dummy data with hashed passwords
    cursor.execute(
       "INSERT OR IGNORE INTO users (username, password, first_name, last_name, role) VALUES (?, ?, ?, ?, ?)",
       ('user1', password1_hash, 'John', 'Doe', 'patron'))
    cursor.execute(
       "INSERT OR IGNORE INTO users (username, password, first_name, last_name, role) VALUES (?, ?, ?, ?, ?)",
       ('user2', password2_hash, 'Jane', 'Smith', 'librarian'))
    cursor.execute(
        "INSERT OR IGNORE INTO items (title, format, author) VALUES (?, ?, ?)",
        ('Hobbit','book','Tolkian'))
    cursor.execute(
        "INSERT OR IGNORE INTO items (title, format, author) VALUES (?, ?, ?)",
        ('MobyDick','book','Mellvile'))
    cursor.execute(
        "INSERT OR IGNORE INTO items (title, format, author) VALUES (?, ?, ?)",
        ('Avengers','Movie','Marvel'))

   # Commit the changes
    conn.commit()

   # Close the connection
    conn.close()