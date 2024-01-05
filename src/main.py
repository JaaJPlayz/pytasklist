import sqlite3
import subprocess

conn = sqlite3.connect('./src/data/database.sqlite3')
cursor = conn.cursor()


def line(length):
    print('-' * length)


def create_database():
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS tasks
        (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, status TEXT)""")


def add_task(task):
    if not task:
        print("No task provided.")
        return

    cursor.execute("INSERT INTO tasks(task, status) VALUES(?, ?)",
                   (task, 'pending'))
    conn.commit()


def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return tasks


def update_task_header():
    tasks = cursor.fetchall()

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(f"ID: {task[0]}, Task: {task[1]}, Status: {task[2]}")

    line(50)

    update_task_id = int(
        input("Enter the ID of the task you want to update: "))

    update_task = input("Enter the new task: ")

    cursor.execute(
        "UPDATE tasks SET task = ? WHERE id = ?", (update_task, update_task_id)
    )

    conn.commit()


def update_task_status():
    tasks = cursor.fetchall()

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(f"ID: {task[0]}, Task: {task[1]}, Status: {task[2]}")

    line(50)

    update_task_id = int(
        input("Enter the ID of the task you want to update: "))

    status_options = ['resigned', 'pending', 'in progress', 'completed']

    for i, option in enumerate(status_options):
        print(f"{i+1}. {option}")

    line(50)

    status_index = int(input("Enter the index of the status: ")) - 1

    update_status = status_options[status_index]

    cursor.execute(
        "UPDATE tasks SET status = ? WHERE id = ?", (
            update_status, update_task_id)
    )

    conn.commit()


def delete_task(id):
    if not id:
        print("No tasks found.")
        return

    cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()


def clear_database():
    cursor.execute("DELETE FROM tasks")
    conn.commit()


def main_menu():
    while True:
        line(50)
        print("Main menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Update task status")
        print("5. Delete task")
        print("6. Clear database")
        print("7. Exit")

        line(50)

        choice = input("Enter your choice: ")

        line(50)

        if choice == '1':
            subprocess.call(['clear'], shell=True)
            line(50)
            tasks = get_tasks()
            print("Tasks:")
            for task in tasks:
                print(f"ID: {task[0]}, Task: {task[1]}, Status: {task[2]}")

        elif choice == '2':
            subprocess.call(['clear'], shell=True)
            task = input("Enter the task: ")
            add_task(task)

        elif choice == '3':
            subprocess.call(['clear'], shell=True)
            update_task_header()

        elif choice == '4':
            subprocess.call(['clear'], shell=True)
            update_task_status()

        elif choice == '5':
            subprocess.call(['clear'], shell=True)
            id = int(input("Enter the ID of the task you want to delete: "))
            delete_task(id)

        elif choice == '6':
            subprocess.call(['clear'], shell=True)
            clear_database()

        elif choice == '7':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    create_database()
    main_menu()
