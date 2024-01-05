import sqlite3

conn = sqlite3.connect('./src/data/database.sqlite3')
cursor = conn.cursor()


def create_database():
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS tasks
        (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, status TEXT)""")


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

    status_options = ['resigned', 'pending', 'in progress', 'completed']

    for i, option in enumerate(status_options):
        print(f"{i+1}. {option}")

    status_index = int(input("Enter the index of the status: ")) - 1

    update_status = status_options[status_index]

    cursor.execute(
        "UPDATE tasks SET status = ? WHERE id = ?", (
            update_status, update_task_id)
    )

    conn.commit()


def delete_task(id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()


def clear_database():
    cursor.execute("DELETE FROM tasks")
    conn.commit()


def main_menu():
    while True:
        print("Main menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task status")
        print("4. Delete task")
        print("5. Clear database")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            tasks = get_tasks()
            print("Tasks:")
            for task in tasks:
                print(f"ID: {task[0]}, Task: {task[1]}, Status: {task[2]}")
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '3':
            update_task_status()
        elif choice == '4':
            id = int(input("Enter the ID of the task you want to delete: "))
            delete_task(id)
        elif choice == '5':
            clear_database()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    create_database()
    main_menu()
