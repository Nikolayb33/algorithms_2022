"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
import random


def task_6(a=random.randint(0, 100), n=10):
    b = int(input("Угадайте число от 0 до 100: "))
    if b == a:
        return print("Вы угадали")
    elif n == 1:
        return print("Закончились попытки")
    elif b > 100 or b < 0:
        return print("Введите корректное число, попытка не засчитана"), task_6(a, n)
    elif b > a:
        n -= 1
        return print(f"Загаданное число меньше, количество попыток {n}"), task_6(a, n)
    elif b < a:
        n -= 1
        return print(f"Загаданное число больше, количество попыток {n}"), task_6(a, n)
    return print(a)


if __name__ == "__main__":
    task_6()
