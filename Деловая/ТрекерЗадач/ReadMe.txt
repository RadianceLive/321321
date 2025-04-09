Программа позволяет добавлять, завершать и удалять задачи. Все данные хранятся в JSON-файле.
Трекер задач в терминале с хранением данных в JSON-файле.
Зависимости:
pip install tabulate
Использование

- Добавить:

python todo_cli.py --add "Сделать домашку"
Список:

python todo_cli.py --list
Завершить:

python todo_cli.py --done 1
Удалить:


python todo_cli.py --delete 1