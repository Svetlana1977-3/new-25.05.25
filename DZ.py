#print("Svetlana")

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
#print(s)  # Выведет вс слитно

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

CONS = u"бвгджзклмнпрстфхцчшщ"
VOV = u"аеёиоуыэюя"
text = u'Привет мир! Это тестовая строка для анализа'

cons = sum(1 for t in text.lower() if t in CONS)
vov = sum(1 for t in text.lower() if t in VOV)

print(cons, vov)

#Подсчитать длину слова в тексте
sentense = "Привет мир! Это тестовая строка для анализа"
words = dict()
for word in sentense.split(" "):
  words[len(word)] = word

biggest_word = words[max(words)]
print(biggest_word)

#Подсчитать количество одинаковых слов в тексте
def count_occurences(s,word):

    count = 0
    for i in range(len(s)):
        if s[i:i+len(word)] == word:
            count += 1
    return count

mystring = "Привет мир! Это тестовая строка для анализа."
myword = "мир"
print(count_occurences(mystring,myword))




























