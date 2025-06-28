#31.05.2025
#string = "Привет мир, Как у тебя дела?"
#print(string.join(". Еще одно предложение"))
#words = ["Привет", "мир"]
#result = " ".join(words)
#print(result)
#
#nums = [1, 2, 3]
#print("".join(nums))#ошибка по типу данных
#print("-".join(map(str, nums)))
#print(string.split(" "))
#print(string.partition("?"))# чтобы преобразовать в список пишем так:(List(string.partition("?")))
#
#print(string.startswith("Привет мир"))
#print(string.endswith("Вторая"))
#print(string.find("Привет"))#ищет начало слова и пишет цифрами, считая пробел и поиск зависит от регистра, мал буква или большая
#print(string.find("и"))#ищет первое значение 2, т.к начинаются буквы с 0-п, 1-р, и-2 и т.д
#print(string.find("и", 5))#поиск начинается с 5 индекса для букви и (получится 8)
#print(string.find("и", 3, 5))# поиск с 3 по 5 индексы, не найдет и ответ будет -1
#print(string.replace("мир", "Россия"))#замена слова, чуствительность к регистру
import string
from ctypes import HRESULT
from itertools import permutations
from operator import index
from typing import final


#Практика строки
#1. Напишите программу, которая принимает строку от пользователя и выводит ее в обратном порядке.
#n = input("Введите строку: ")
#print(n[::-1])

#2.Напишите программу, которая принимает 2 строки и проверяет, являются ли они анаграммами
#s1 = input("Введите 1 строку: ").lower()
#s2 = input("Введите 2 строку: ").lower()
#print(sorted(s1) == sorted(s2))

#3.Напишите программу, которая принимает строку и подсчитывает количество гласных и согласных букв в ней
#s = input("Введите строку: ").upper()
#vowels = "УЕЫАОЭЯИЮ"
#consonants = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
#v = c = 0
#for char in vowels:
#    if char in vowels:
#        v += 1
#    elif char in consonants:
#        c += 1
#        print("Гласных:", v)
#        print("согласных:", c)
#
#4.Напишите программу, которая принимает строку и проверяет, является ли она палиндромом (т.е. одинаково читается в обоих направлениях)
#s = input("Введите строку: ").lower().replace(" ", "")
#if s == s[::-1]:#s оригинальный = s перевернутый
#    print("Палиндром")
#else:
#    print("Не палиндром")

#01.06.2025

#Задача 5
#Напишите программу, которая принимает строку и выводит на экран все перестановки ее символов
#def permute(s, s2):
#    if len(s) == 0:
#        print(s2, end=' ')
#        return
#    for i in range(len(s)):
#        char = s[i]
#        left_s = s[0:i]
#        right_s = s[i + 1:]
#        rest = left_s + right_s
#        permute(rest, s2 + char)
#s1 = "слон"
#s2 = ""
#permute(s1, s2) #Рекурсия - функция переставляет буквы в слове и генерирует ответ

#Решение 2
#s = input("Введите строку: ")
#a = list(s)
#n = len(a)
#index = 0
#stack = [(a, 0)]
#while index < len(stack):
#    current, l = stack[index]
#    index += 1
#    if l == n - 1:
#        print("".join(current))
#    else:
#        i = n - 1
#        while i >= l:
#            temp = current[:]
#            temp[l], temp[i] = temp[i], temp[l]
#            stack.append((temp, l + 1))
#            i -= 1

#решение 3 короткое через permutations
#s = input("Введите слово: ")
#perms = permutations(s)
#for p in perms:
#    print("".join((p)))

#Задача 8
#Напишите программу, которая принимает строку и заменяет каждое вхождение опр слова на другое слово
#s = input("Введите слово: ")
#old = input("какое слово заменить?")
#new = input("На какое слово заменить?")
#print(s.replace(old, new))

#задача 9
#Напишите программу, которая принимает строку и проверяет ее явл ли она панграммой
#Решение 1
#s = input("Введите строку: ")
#for letter in string.ascii_lowercase:
#    if s.lower().count(letter) == 0:
#        print("False")
#    break
#else:
#    print("True")
#Решение 2
#s = input("Введите строку: ").lower()
#alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
#letters_in_s = set()
#for char in s:
#    if "".join(sorted(letters_in_s)) == alphabet:
#        print("Панграмма")
#else:
#    print("Не панграмма")

#Задача 14 Перечислить все положительные делители с сортировкой по возрастанию 360457890232, 23436, 190187200
#number = int(input("Введите число: "))
#divisors  = set()
#for i in range(1, int(number**0.5)+1):
#    if number % i == 0:
#        divisors.add(i)
#        divisors.add(number // i)
#result = sorted(divisors)
#print(result)

#08.06.2025 Функции - глобальные, локальные
#если переменная внутри, то функция локальная
#def f(b):
#   b += 0
#    print(b)
#    b = 5
#    f(b)

#если глобальная, то обращение идет в F
#def f(a):
#    global  b
#    b += 3
#    print(a + b)
#    b = 2
#    f(b)

#глобальная функция:
#def f():
#    global  a
#    b = 2
#    a, b = b, a
#    print(a, b, end = " ")
#a = 1
#b = 2
#f()
#print(a, b, end = " ")

#def f():
#    global a
#    global b
#    b, c = a, b
#def g():
#        global a
#        global d
#        c = '0'
#        a = d + c
#        a = '2'
#        b = '3'
#        c = '5'
#        d = '7'
#        f()
#        g()
#        f()
#        print(a + b + c + d)
#ответ должен быть 707057
#
#Задача 1
# def print_lines(n):
#     print('-' * n)
#     print('-' * n)
# n = int(input("введите количество символов в строке: "))
# print_lines(n) # выведет столько тире, сколько мы зададим

#Здача 2 вывести в виде трех строк квадрат
# def print_rectangle(n):
#     if n < 2:
#         print("ширина должна быть не менее 2: ")
#     print("-" * n)
#     print("-" + " " * (n - 2) + "-")
#     print("-" * n)
#
# n = int(input("введите ширину квадрата: "))
# print_rectangle(n) # выведет тире в виде квадрата
#Задача 3
# выводит в виде треугольника
# def print_triangle(n):
#    for i in range(1, n * 1):
#        print("+" * i)
#
# n = int(input("введите сторону треугольника: "))
# print_triangle(n) # выведет звездочки в виде треугольника

#14.06.2025 Найдите простое трехзначное число (определить функцию)
# def is_prime(n):
#     if n < 2: return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return  False
#     return True
# primes = []
# for i in range(100, 1000):
#     if is_prime(i):
#         primes.append(i)
# print(primes)

#Получить все шестизначные счастливые номера. Определить функцию для расчета суммы цифр трехзначноо числа
#Шестизначное число в котором сумма первых трех равна сумме последних.
# def sum_digits(n):
#     summa = 0
#     for d in str(n):
#         summa += int(d)
#         return summa
# def is_lucky(n):
#     s = str(n)
#     if sum_digits(s[:3]) == sum_digits(s[3:]):
#         print("Число счастливое")
#     else:
#         print("Число не счастливое")
# is_lucky(123456)

#Даны шесть различных чисел. Определить максим. (Опр функцию находящую макс из двух разн чисел)
# def max6(a, b, c, d, e, f):
#     return max(a, b, c, d, e, f)
#
# print(max6(2, 4, 5,6, 89, 9))

#15.06.2025
#Задача 13. Даны основания и высоты равнобедренных трапеций. Найти сумму их периметров и сумму площадей.
# Определить процедуру для расчетов.

# def trapezoid_perimetr_area(a, b, h):
#    side = (((a - b) / 2)**2 + h**2) ** 0.5
#    p = a + b + 2 * side
#    area = (a + b) / 2 * h
#    return p, area
# trapezoid1 = trapezoid_perimetr_area(4, 10, 3)
# trapezoid1 = trapezoid_perimetr_area(6, 15, 5)
# print("Сумма периметров трапеций: {trapezoid[0] + trapezoid[0]}")
# print("Сумма площадей трапеций: {trapezoid[1] + trapezoid[1]}")

#Задача 14. Вычислить площадь круга, прямоугольника или треугольника.
#Определить функции для площади каждой фигуры

# def circle_area(r):
#    return 3.14 * r ** 2
# def rect_area(a, b):
#    return a * b
# def triangle_area(a, h):
#    return (a * h) / 2
#
# print("1 - Круг")
# print("2 - Треугольник")
# print("3 - Прямоугольник")
# figure = input("Выберите фигуру, площадь которой вы хотите найти:")
# if figure == "1":
#    r = float(input("Введите радиус круга: "))
#    print("Площадь круга:", circle_area(r))
# elif figure == "2":
#    a = float(input("Введите сторону а у прямоугольника: "))
#    b = float(input("Введите сторону b у прямоугольника: "))
#    print("Площадь прямоугольника:", rect_area(a, b))
#elif figure == "3":
#a = float(input("Введите сторону треугольника: "))
#b = float(input("Введите высоту треугольника: "))
#    print("Площадь треугольника:", triangle_area(a, h))

#Задача 16
# Напишите процедуру с параметрами n и s, которая выводит квадрат размером n x n из символов которы вводятся с клавиатуры.
#Используя эту процедуру напишите программу которая запрашивает два значения - сторону квадрата и символ, и вызывает процедуру рисования требуемого квадрата
# def draw_square(n, s):
#    for _ in range(n):
#       print(n * s)
#
# side = int(input("Введите сторону квадрата: "))
# symbole = input("Введите символ: ")
# draw_square(side, symbole)

#Задача 17
#напишите процедуру, которая выводит на экран все делители числа N в одну строку через пробел.
#Используя данную процедуру, составьте программу, которая для всех введенных натуральных чисел выводит делители текущего числа
# def print_divisors(n):
#    for i in range(1, n + 1):
#       if n % i == 0:
#          print(i, end=' ')
#    print()
# while True:
#    x = int(input("Введите число (0 для выхода из программы): "))
#    if x == 0:
#       break
#    print_divisors(x)

#Рекурсия
# def F(n):
#     print(n)
#     if n > 1:
#         F(n - 1)
#         F(n - 3)
# F(6)

#Классы
# class Contact:
#     def __init__(self, name, phone, email):
#         self.name = name
#         self.phone = phone
#         self.email = email
#     def __str__(self):
#         return f"{self.name} Телефон: {self.phone} Email: {self.email}"
#
# class ContactManager:
#     def __int__(self):
#         self.contacts = []
#     def add_contact(self, contact):
#         self.contacts.append(contact)
#         print(f"Контакт '{contact.name}' добавлен")
#
# contact1 = Contact("Иванов Иван", "1234567890", "ivanov@test.ru")
# print(contact1)

# #1 - я задача:
# def fnod(a, b):
#     nod = max(a, b)
#     while nod >= 2:
#         if a % nod == 0 and b % nod == 0:
#             break
#         nod -= 1
#     return nod if min([a, b]) > 1 else 1
#
# [a, b] = [int(i) for i in input("Введите два числа: ").split(" ")]
# print(fnod(a, b))
#
# #2 - я задача:
#
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# start = int(input("Введите начало диапазона: "))
# end = int(input("Введите конец диапазона: "))
#
# for i in range(start, end + 1):
#     if is_prime(i):
#         print(i)



















