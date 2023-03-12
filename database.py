import sqlite3

class Database:
    def __init__(self):
        pass

    def connect(self):
        return sqlite3.connect("webapp.db")