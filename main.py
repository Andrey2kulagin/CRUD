FILENAME = "tasks.txt"


def clear_file(file_name):
    file = open(file_name, "w")
    file.write("")
    file.close()


def create(file_name, add_str):
    tasks = open(file_name, "a")
    tasks.write(add_str)
    tasks.close()


def read(file_name, str_num=None):
    tasks_file = open(file_name, "r")
    tasks = tasks_file.readlines()
    if str_num is None:
        count = 1
        for line in tasks:
            print(count, line, end="")
            count += 1
    else:
        str_num = int(str_num)
        if str_num > len(tasks):
            raise Exception(f"Такой строки нет, введите число до {len(tasks)}")
        print(tasks[str_num + 1], end="")
    tasks_file.close()


def update(file_name, new_text, str_num=None):
    if str_num is None:
        tasks_file = open(file_name, "a")
        tasks_file.write(new_text)
        tasks_file.close()
    else:
        str_num = int(str_num)
        new_text += "\n"
        tasks_file = open(file_name, "r")
        tasks = tasks_file.readlines()
        if str_num > len(tasks):
            raise Exception(f"Такой строки нет, введите число до {len(tasks)}")
        tasks[str_num - 1] = new_text
        tasks_file.close()
        clear_file(file_name)
        tasks_file = open(file_name, "a")
        for line in tasks:
            tasks_file.write(line)
        tasks_file.close()


def delete(file_name, str_num):
    str_num = int(str_num)
    tasks_file = open(file_name, "r")
    tasks = tasks_file.readlines()
    if str_num > len(tasks):
        raise Exception(f"Такой строки нет, введите число до {len(tasks)}")
    tasks.pop(str_num - 1)
    tasks_file.close()
    clear_file(file_name)
    tasks_file = open(file_name, "a")
    for line in tasks:
        tasks_file.write(line)
    tasks_file.close()


def menu():
    solution = input("""Выберите, что вы хотите сделать
    1. Добавить задачу
    2. Вывести список задач
    3. Удалить задачу
    4. Выйти из программы
    """)
    if solution == '1':
        print("Список ваших задач:\n")
        read(FILENAME)
        solution = input("""Выберите, что вы хотите сделать
            1. Изменить задачу по номеру
            2. Добавить новую задачу в конец списка
            3. Выйти из программы
            """)
        if solution == "1":
            input_str = input("""Введите текст дли изменения и номер задачи, которую хотите изменить
            Пример: купить молоко 7
            """)
            change_str = input_str[:input_str.rfind(" ")]
            str_num = input_str[input_str.rfind(" "):]
            update(FILENAME, change_str, str_num)
            print("Теперь ваш список задач выглядит так:")
            read(FILENAME)
        elif solution == '2':
            input_str = input("Введите текст новой задачи")
            update(FILENAME, input_str)
            print("Теперь ваш список задач выглядит так:")
            read(FILENAME)
        elif solution == '3':
            exit()
    elif solution == '2':
        solution = input("""Выберите, что вы хотите сделать
                    1. Вывести задачу по номеру
                    2. Вывести все задачи
                    3. Выйти из программы
                    """)
        if solution == "1":
            input_str = input("Введите номер задачи")
            str_num = input_str[input_str.rfind(" "):]
            read(FILENAME,  str_num)
        elif solution == '2':
            read(FILENAME)
        elif solution == '3':
            exit()
    elif solution == '3':
        print("Список ваших задач:\n")
        read(FILENAME)
        str_num = input("Введите номер задачи для удаления")
        delete(FILENAME, str_num)
        print("Теперь ваш список задач выглядит так:")
        read(FILENAME)

menu()
