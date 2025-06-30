#print("Svetlana")
import sys

from unicodedata import normalize

#ДЗ 18.05.2025 Найдите число фибоначи (сумма чисел)
#a, b = 0, 1
#for _ in range(10):
#    print(a)
#a, b = b, a + b

# Выведите числа в обратном порядке
#for i in range(10, 0 - 1):
#    print(i)

# Подсчет гласных букв в строке
#text = input("Ведите любой текст: ").lower()
#vowels = ['а', 'о', 'у', 'ы', 'и', 'э', 'е', 'ё', "ю", "я"]
#count = 0
#for i in text:
#    if i in vowels:
#        count += 1
#print(count)
#
#Вывести таблицу умножения
#for i in range(1, 11):
#    for j in range(1, 11):
#        print(f"{i} * {j} = {i * j}")
#        print()

#Вывести сумму цифр заданного числа
#x = input("Введите число: ")
#total = 0
#for digit in x:
#    total += int(digit)
#print(f"Сумма чисел: {total}")
#
#ДЗ 24.05.2025
#Задача 11
#letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
#result = ''
#for letter in letters:
#    if letter.islower():
#       result += letter
#print(result)
#
# Здача 12
#secret_list = ["Мавпродош", "Лорнектиф", "Древерол", "Фиригарпиг", 'Клодобродыч']
#while True:
#    nickname = input("Введите свой никнейм: ")
#    if nickname in secret_list:
#        print(f"Ты – свой. Приветствую, любезный {nickname}!")
#        break
#    else:
#        print("Тут ничего нет. Еще есть вопросы?")
#
#31.05.2025
#Задача 6
#s = input("Введите строку: ")
#s = s.replace("", "")
#print(s)  # Выведет все слитно

#Задача 7
#input_string = input("Введите строку: ")
#words = input_string.split()
#longest_word = ""
#for word in words:
#    if len(word) > len(longest_word):
#        longest_word = word
#        print(f"Самое длинное слово в строке: {longest_word}")

#ДЗ от 01.06.2025
#Получить текст от пользователя, подсчитать количество гласных и согласных букв.
#Найти самое длинное слово, подсчитать количество данных слов в тексте

# CONS = u"бвгджзклмнпрстфхцчшщ"
# VOV = u"аеёиоуыэюя"
# text = u'Привет мир! Это тестовая строка для анализа'
#
# cons = sum(1 for t in text.lower() if t in CONS)
# vov = sum(1 for t in text.lower() if t in VOV)
#
# print(cons, vov)
#
# #Подсчитать длину слова в тексте
# sentense = "Привет мир! Это тестовая строка для анализа"
# words = dict()
# for word in sentense.split(" "):
#   words[len(word)] = word
#
# biggest_word = words[max(words)]
# print(biggest_word)
#
# #Подсчитать количество одинаковых слов в тексте
# def count_occurences(s,word):
#
#     count = 0
#     for i in range(len(s)):
#         if s[i:i+len(word)] == word:
#             count += 1
#     return count
#
# mystring = "Привет мир! Это тестовая строка для анализа."
# myword = "мир"
# print(count_occurences(mystring,myword))
#
# #2 способ
# text = input("Введите текст: ").upper()
# vovels = "АЕЁИОУЫЭЮЯ"
# vowel_count = 0
# consonant_count = 0
#
# for char in text:
#     if char.isalpha():
#         if char in vovels:
#             vowel_count += 1
#         else:
#             consonant_count += 1
# print("Количество гласных букв:", vowel_count)
# print("Количество согласных букв:", consonant_count)
#
# words = text.split()
# max_word = ""
# for word in words:
#     clean_word = "".join([c for c in word if c.isalpha()])
#     if len(clean_word) > len(max_word):
#         max_word = clean_word
# print("Самое длинное слово:", max_word)
# search_word = input("Введите слово для поиска: ")
# normalize_words = []
# for word in words:
#     clean = "".join([c for c in word if c.isalpha()])
#     normalize_words.append(clean)
# print("Количество одинаковых вхождений слова:", normalize_words.count(search_word))

#07.06.2025
# user_name = input("Введите имя: ")
# string = input("Введите строку: ")
# count = 0
# for letter in user_name:
#     count += string.count(letter)
# if count > 0:
#     print(f"Количество букв вашего имени в строке: {count}")
# else:
#     print("Букв вашего имени нет в строке")
#
# #08.06.2025
# #Задача 4. Напишите функцию, которая вычисляет среднее арифметическое пяти целых чисел.
# numbers = [4, 9, 7, 5, 2]
# average = sum(numbers) / len(numbers)
# print(average)
#
#
# #Задача 7. Найти периметр треугольника, заданного координатами своих вершин.  (Определить функцию
# # для расчета длины отрезка по координатам его вершин.)
# def calculate_perimeter(side1, side2, side3):
#     perimeter = side1 + side2 + side3
#     return perimeter
# side1 = float(input("Введите длину первой стороны: "))
# side2 = float(input("Введите длину второй стороны: "))
# side3 = float(input("Введите длину третьей стороны: "))
# perimeter = calculate_perimeter(side1, side2, side3)
# print("Периметр треугольника равен:", perimeter)
#
# #Задача 5. Напишите функцию, которая находит количество цифр в десятичной записи числа.
# def count_digits(number):
#      number = abs(number)
#      count = 0
#      while number > 0:
#          count += 1
#          number //= 10
#      return count if count > 0 else 1
#
# num = int(input("Введите число: "))
# print("Количество десятичных цифр:", count_digits(num))

# #Задача 7 второй вариант
# def distas(x1, y1, x2, y2):
#     return (((x2 - x1)**2) + ((y2 - y1)**2))**0.5
# def triangle_perimetr(x1, y1, x2, y2, x3, y3):
#   a = distas(x1, y1, x2, y2)
#   b = distas(x2, y2, x3, y3)
#   c = distas(x3, y3, x1, y1)
#   return a + b + c
#
# print(triangle_perimetr(x1: 1, y1: 2, x2: 4, y2: 5, x3: 6, y3: 7))

#14.06.2025
#Задача 11 Поменять местами значения
# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))
# d = int(input('d: '))
#
# a = a + b
# b = a - b
# a = a - b
# c = c + d
# d = c - d
# c = c - d
# print('a =', a)
# print('b =', b)
# print('c =', c)
# print('d =', d)
#
# # Задача 12 Даны стороны двух треугольников. Найти сумму их периметров и площадей
# def per(a, b, c):
#     return a + b + c
# def area(a, b, c):
#     p = per(a, b, c) / 2
#     return (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print (per(3, 4, 5))
# print(area(3, 4, 5))

#15.06.2025
#Задача 20. Найти периметр и площадь треугольника и определить где находиться вхождение точки

# def side_length(x1, y1, x2, y2):
#     return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
#
# def heron_triangle_area(a, b, c):
#     p = (a + b + c) / 2
#     return (p *(p - a) * (p - b) * (p - c))**0.5
#
# def pointInTriangle(x1, y1, x2, y2, x3, y3):
#     a = side_length(x1, y1, x2, y2)
#     b = side_length(x2, y2, x3, y3)
#     c = side_length(x3, y3, x1, y1)
#     area_abc = heron_triangle_area(a, b, c)
#
#     a1 = side_length(px, py, x1, y1)
#     b1 = side_length(px, py, x2, y2)
#     c1 = side_length(x1, y1, x2, y2)
#     area_pab = heron_triangle_area(a1, b1,c1)
#
#     a2 = side_length(px, py, x2, y2)
#     b2 = side_length(px, py, x3, y3)
#     c2 = side_length(x2, y2, x3, y3)
#     area_pbc = heron_triangle_area(a2, b2, c2)
#
#     a3 = side_length(px, py, x1, y1)
#     b3 = side_length(px, py, x1, y1)
#     c3 = side_length(x3, y3, x1, y1)
#     area_pca = heron_triangle_area(a3, b3, c3)
#     total_area = area_pab + area_pbc + area_pca
#     return area_abc == total_area
# print(pointInTriangle(1, 1, 0, 0, 4, 4,))


#Задача 18. Найти средний балл для спортсменов

# m = sorted(map(int, input('Введите оценки экспертов через пробел').split()))
# print(m[0], m[-1])
# print(round(sum(m[1:4]) / 3, 2))

#Задача 19. Найти периметр и площадь прямоугольника и вхождение точки
# def pointInRect(x, y, x1, y1, x2, y2):
#     return x1 <= x <= x2 and y2 <= y <= y1
# x = int(input("Введите координаты х исходной точки: "))
# y = int(input("Введите координаты y исходной точки: "))
#
# x1 = int(input("Введите координаты х нижней точки: "))
# y1 = int(input("Введите координаты y верхней точки: "))
# x2 = int(input("Введите координаты х нижнего угла: "))
# y2 = int(input("Введите координаты y верхнего угла: "))
# print(pointInRect(x, y, x1, y1, x2, y2))

#21.06.2025 OOP Practic
#Задача 2 Что вернется при вызове F(4)
# class Person:More actions
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def introduce(self):
#         print(f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}")
#
# class Employee(Person):
#     def __init__(self, name, age, gender, salary, position):
#         super().__init__(name, age, gender)
#         self.salary = salary
#         self.position = position
#
#     def work(self):
#         print(f"{self.name} работает в качестве {self.position} с ЗП {self.salary} рублей.")
#
#
# person = Person("Алиса", 30, "женский")
# person.introduce()
#
# employee = Employee("Алексей", 28, "мужской", "200 тыс.", "QA Senior")
# employee.introduce()
# employee.work()


#Задача №1
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#     def perimetr(self):
#         return 2 * (self.width + self.height)
#     class Square(Rectangle):
#
# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
#
#     def area(self):
#         return self.side ** 2
#
#     def perimetr(self):
#         return 4 * self.side
# rect = Rectangle(4, 5)
# print("Площадь прямоугольника: ", rect.area())
# print("Площадь прямоугольника: ", rect.perimetr())
#
# sq = Square(3)
# print("Площадь квадрата: ", sq.area())
# print("Площадь квадрата: ", sq.perimetr())









