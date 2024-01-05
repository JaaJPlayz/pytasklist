import sqlite3

conn = sqlite3.connect('./src/data/database.sqlite3')
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


def main_menu():
    while True:
        print("1. Add task")
        print("2. Update task status")
        print("3. Delete task")
        print("4. Clear database")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            update_task_status()
        elif choice == '3':
            task_id = int(input("Enter task ID: "))
            delete_task(task_id)
        elif choice == '4':
            clear_database()
        elif choice == '5':
            print("Exiting...")
            break


create_database()
