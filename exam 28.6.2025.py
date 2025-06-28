#задача 3 Поиск наибольшего общего делителя (НОД).

def fnod(a, b):
    nod = max(a, b)
    while nod >= 2:
        if a % nod == 0 and b % nod == 0:
            break
        nod -= 1
    return nod if min([a, b]) > 1 else 1

[a, b] = [int(i) for i in input("Введите два числа: ").split(" ")]
print(fnod(a, b))

# задача 2 Поиск простых чисел в заданном диапазоне

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

for i in range(start, end + 1):
    if is_prime(i):
        print(i)