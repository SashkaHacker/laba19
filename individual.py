#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
from datetime import datetime

from validation import ListWorkers


# вариант - 11


def add(lst):
    # Запросить данные о работнике.
    surname = input("Фамилия: ")
    name = input("Имя: ")
    phone = input("Номер телефона: ")
    date = input("Дата рождения (число:месяц:год): ").split(":")

    # Создать словарь.
    dct = {"surname": surname, "name": name, "phone": phone, "date": date}
    lst.append(dct)

    # Сортировка списка словарей
    lst.sort(key=lambda x: datetime.strptime("-".join(x["date"]), "%d-%m-%Y"))


def phone(lst):
    numbers_phone = input("Введите номер телефона")
    fl = True
    for i in lst:
        if i["phone"] == numbers_phone:
            print(
                f"Фамилия: {i['surname']}\n"
                f"Имя: {i['name']}\n"
                f"Номер телефона: {i['phone']}\n"
                f"Дата рождения: {':'.join(i['date'])}"
            )
            fl = False
            break
    if fl:
        print("Человека с таким номером телефона нет в списке.")


def instruction():
    print(
        "add - добавление нового работника\n"
        "phone - данные о работнике по его номеру телефона\n"
        "exit - завершение программ\n"
        "list - список работников\n"
        "save filename - сохранить данные в json файл\n"
    )


def save_workers(file_name, staff):
    """
    Сохранить всех работников в файл JSON.
    """
    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(staff, fout, ensure_ascii=False, indent=4)


def load_workers(file_name):
    """
    Загрузить всех работников из файла JSON.
    """
    with open(file_name, "r", encoding="utf-8") as fin:
        data = json.load(fin)

    try:
        valid_data = ListWorkers(lst=data)
        return valid_data
    except Exception:
        print("Invalid JSON")


def workers(lst):
    """
    Отобразить список работников.
    """
    # Проверить, что список работников не пуст.
    if lst:
        # Заголовок таблицы.
        line = "+-{}-+-{}-+-{}-+-{}-+-{}-+".format(
            "-" * 4, "-" * 30, "-" * 20, "-" * 15, "-" * 15
        )
        print(line)
        print(
            f'| {"№":^4} | {"Фамилия":^30} | {"Имя":^20} | '
            f'{"Номер телефона":^15} | {"Дата рождения":^15} |'
        )

        print(line)
        # Вывести данные о всех сотрудниках.
        for idx, worker in enumerate(lst, 1):
            print(
                f'| {idx:>4} | {worker.get("surname", ""):<30} | '
                f'{worker.get("name", ""):<20}'
                f' | {worker.get("phone", 0):>15}'
                f' | {":".join(worker.get("date", 0)):>15} |'
            )

        print(line)
    else:
        print("Список работников пуст.")


def main():
    # sample = ["surname", "name", "phone", "date"]
    lst = []
    # ввод данных
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        match command.split():
            case ["exit"]:
                break
            case ["add"]:
                add(lst)
            case ["phone"]:
                phone(lst)
            case ["help"]:
                instruction()
            case ["list"]:
                workers(lst)
            case ["save", filename]:
                print(lst)
                save_workers(filename, lst)
            case ["load", filename]:
                new_info = load_workers(filename)
                if new_info:
                    lst = new_info

            case _:
                print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == "__main__":
    main()
