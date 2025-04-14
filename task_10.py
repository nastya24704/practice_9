def count(a, max):
    if a == 0:
        return 1
    if a < 0 or max == 0:
        return 0
    return count(a - max, max - 1) + count(a, max - 1)
a = int(input("Введите количество кубиков: "))
print(count(a, a - 1))
