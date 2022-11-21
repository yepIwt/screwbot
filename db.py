import os
import sqlite3

connection = sqlite3.connect(os.path.join("db", "config.db"))
cursor = connection.cursor()


def add_new(admin_id: int, chat_id: int):
	cursor.execute(f"INSERT INTO data VALUES({admin_id}, {chat_id})")
	connection.commit()


def find_chat_id(chat_id: int) -> bool:
	admind_id = cursor.execute(f"SELECT admin_id FROM data WHERE chat_id = {chat_id}").fetchall()
	if admind_id:
		return True
	return False