import json
import os
import argparse
from tabulate import tabulate

DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)
    print("✅ Задача добавлена.")

def list_tasks():
    tasks = load_tasks()
    table = [[i + 1, t["description"], "✅" if t["done"] else "❌"] for i, t in enumerate(tasks)]
    print(tabulate(table, headers=["ID", "Задача", "Статус"]))

def mark_done(task_id):
    tasks = load_tasks()
    try:
        tasks[task_id - 1]["done"] = True
        save_tasks(tasks)
        print("✔️ Задача отмечена как выполненная.")
    except IndexError:
        print("❌ Неверный ID задачи.")

def delete_task(task_id):
    tasks = load_tasks()
    try:
        removed = tasks.pop(task_id - 1)
        save_tasks(tasks)
        print(f"🗑️ Удалена: {removed['description']}")
    except IndexError:
        print("❌ Неверный ID задачи.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Task Tracker")
    parser.add_argument('--add', help='Добавить задачу')
    parser.add_argument('--list', action='store_true', help='Показать задачи')
    parser.add_argument('--done', type=int, help='Отметить задачу выполненной')
    parser.add_argument('--delete', type=int, help='Удалить задачу')

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        list_tasks()
    elif args.done:
        mark_done(args.done)
    elif args.delete:
        delete_task(args.delete)
    else:
        parser.print_help()
