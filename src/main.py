import sqlite3
import json

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def create_database():
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, status TEXT)")


