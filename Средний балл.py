def student_ocean(student, predmet):
    slovar = {
        'Иванов': {
            'Математика': [5, 4, 3, 4, 5],
            'Изо': [3, 5, 4, 5, 3],
            'Физкультура': [4, 5, 4, 5, 5],
            'Русский язык': [5, 5, 4, 5, 5],
        },
        'Саньков': {
            'Математика': [3, 5, 3, 2, 4],
            'Изо': [5, 3, 3, 4, 5],
            'Физкультура': [4, 2, 5, 2, 4],
            'Русский язык': [4, 4, 4, 4, 4],
        },
        'Васильков': {
            'Математика': [5, 5, 5, 5, 5],
            'Изо': [5, 5, 5, 5, 5],
            'Физкультура': [5, 5, 5, 5, 5],
            'Русский язык': [5, 5, 5, 5, 5],
        }
    }

    if student not in slovar:
        return f"Ученик с фамилией {student} не найден."

    if predmet not in slovar[student]:
        return f"Предмет '{predmet}' не найден для ученика {student}."

    print("Выберите действие:")
    print("1 - Вывести все оценки по предмету")
    print("2 - Вывести средний балл по предмету")
    choice = input("Введите номер действия (1 или 2): ")

    predmet_slovar = slovar[student][predmet]

    if choice == "1":
        return f"Оценки по предмету '{predmet}' у ученика {student}: {predmet_slovar}"

    elif choice == "2":
        srball = sum(predmet_slovar) / len(predmet_slovar)
        return f"Средний балл по предмету '{predmet}' у ученика {student}: {srball:.2f}"

    else:
        return "Неверный выбор. Введите 1 или 2."

student = input("Введите фамилию ученика (Иванов, Саньков, Васильков): ")
predmet = input("Введите предмет (Математика, Изо, Физкультура, Русский язык): ")

result = student_ocean(student, predmet)
print(result)
