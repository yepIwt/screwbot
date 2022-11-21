import os
import sqlite3

connection = sqlite3.connect(os.path.join("db", "config.db"))
cursor = connection.cursor()


def add_new(admin_id: int, chat_id: int):
	cursor.execute(f"INSERT INTO data VALUES({admin_id}, {chat_id})")
	connection.commit()
