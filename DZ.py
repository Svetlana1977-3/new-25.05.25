print("Svetlana")

#ДЗ 18.05.2025 Найдите число фибоначи (сумма чисел)
a, b = 0, 1
for _ in range(10):
    print(a)
a, b = b, a + b

# Выведите числа в обратном порядке
for i in range(10, 0 - 1):
    print(i)

# Подсчет гласных букв в строке
text = input("Ведите любой текст: ").lower()
vowels = ['а', 'о', 'у', 'ы', 'и', 'э', 'е', 'ё', "ю", "я"]
count = 0
for i in text:
    if i in vowels:
        count += 1
print(count)

#Вывести таблицу умножения
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")
        print()

#Вывести сумму цифр заданного числа
x = input("Введите число: ")
total = 0
for digit in x:
    total += int(digit)
print(f"Сумма чисел: {total}")

#ДЗ 24.05.2025
#Задача 11
letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
for letter in letters:
    if letter.upper() == letters:
        letters.replace(letter, '')
        print(letters)

# Здача 12
secret_nicknames = ["Мавпродош", "Лорнектиф", "Древерол", "Фиригарпиг", 'Клодобродыч']
password = "123456"

while True:
    username = input("Введите свой никнейм: ")
    if username in secret_nicknames:
        print("Ты – свой. Приветствую, любезный ", username + "! Пароль:", password)
        break
    else:
        print("Тут ничего нет. Еще есть вопросы?")