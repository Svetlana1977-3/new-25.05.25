#print("Svetlana")
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

# #08.06.2025
# #Задача 4. Напишите функцию, которая вычисляет среднее арифметическое пяти целых чисел.
# numbers = [4, 9, 7, 5, 2]
# average = sum(numbers) / len(numbers)
# print(average)
#
#
# #Задача 7. Найти периметр треугольника, заданного координатами своих вершин.  (Определить функцию
# # для расчета длины отрезка по координатам его вершин.)
# a = 0
# b = []
# triangle = {
# 'v1': [input('Write the coordinates for the first vector: ') for x in range(2)],
# 'v2': [input('Write the coordinates for the second vector: ') for x in range(2)],
# 'v3': [input('Write the coordinates for the third vector: ') for x in range(2)]
# }
# for z, y in triangle.items():
#     for x in y:
#         a = int(x)**2 + a
#     b.append(a**(1/2))
#     a = 0
# print(sum(b))
#
# #2-й способ
# import math
# def distance2D(xA,yA,xB,yB):
#     return math.sqrt((xA-xB)*(xA-xB)+(yA-yB)*(yA-yB))
#
# def trianglePerimeter(xA,yA,xB,yB,xC,yC):
#     return distance2D(xA,yA,xB,yB)+distance2D(xA,yA,xC,yC)+distance2D(xC,yC,xB,yB)
#
# print(trianglePerimeter(3,8,6,2,7,6))
#
# #Задача 5. Напишите функцию, которая находит количество цифр в десятичной записи числа.
# def count_digits(number):
#     number = abs(number)
#     count = 0
#     while number > 0:
#         count += 1
#         number //= 10
#     return count if count > 0 else 1
#
# num = int(input("Введите число: "))
# print("Количество десятичных цифр:", count_digits(num))

# def calculate_perimeter(side1, side2, side3):
#     perimeter = side1 + side2 + side3
#     return perimeter
#     side1 = float(input("Введите длину первой стороны: "))
#     side2 = float(input("Введите длину второй стороны: "))
#     side3 = float(input("Введите длину третьей стороны: "))
#     perimeter = calculate_perimeter(side1, side2, side3)
#     print("Периметр треугольника равен:", perimeter)
#     perimeter = calculate_perimeter(2, 4, 3, 2, 2, 4)

















