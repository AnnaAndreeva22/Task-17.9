# 1. Преобразование введённой последовательности в список

array = input("Введите последовательность чисел через пробел:").split()
array_list = list(map(int, array))

print(type(array_list))

# 2. Сортировка списка по возрастанию элементов в нем

for i in range(len(array_list)):
    for j in range(len(array_list)-i-1):
        if array_list[j] > array_list[j+1]:
            array_list[j], array_list[j+1] = array_list[j+1], array_list[j]

print(array_list)
print("----")


# 3. Устанавливается номер позиции элемента, который меньше введенного пользователем числа,
# а следующий за ним больше или равен этому числу.

# 3.1 Бинарный поиск


def binary_search(array_list, number, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array_list[middle] == number:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif number < array_list[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array_list, number, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array_list, number, middle + 1, right)


# 3.2 Вводим числа с клавиатуры

array_list_1 = input("Введите последовательность чисел через пробел:").split()
array_list = list(map(int, array_list_1))

# 3.3 Сортируем список, тк бинарный поиск работает в отсортированном списке

for i in range(len(array_list)):
    for j in range(len(array_list)-i-1):
        if array_list[j] > array_list[j+1]:
            array_list[j], array_list[j+1] = array_list[j+1], array_list[j]

print(array_list)
print("Длина списка:", (len(array_list)))

# 3.4 Введите число из последовательности


number = int(input("Введите число из списка:"))
print(type(number))


if number in array_list:
    print("Число корректно")
    a = (binary_search(array_list, number, 0, (len(array_list) - 1)))
    print(a)
    print(a - 1)
else:
    number_1 = int(input("Введите корректное число:"))
    a = (binary_search(array_list, number_1, 0, (len(array_list) - 1)))
    print(a)
    print(a - 1)
