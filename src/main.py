import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


def create_database():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, status TEXT)")


def add_task(task):
    cursor.execute("INSERT INTO tasks(task, status) VALUES(?, ?)",
                   (task, 'pending'))
    conn.commit()


def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return tasks


def update_task_status():
    tasks = cursor.fetchall()

    for task in tasks:
        print(f"ID: {task[0]}, Task: {task[1]}, Status: {task[2]}")

    update_task_id = int(
        input("Enter the ID of the task you want to update: "))
    update_status = input("Enter the new status: ")

    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?",
                   (update_status, update_task_id))

    conn.commit()


def delete_task(id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()


def clear_database():
    cursor.execute("DELETE FROM tasks")
    conn.commit()


create_database()
