def bubble_sort_list():
    input_str = input("Введіть числа через пробіл: ")
    try:
        lst = [int(x) for x in input_str.split()]
    except ValueError:
        print("Помилка: введіть тільки цілі числа.")
        return

    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    print("Відсортований список:", lst)

bubble_sort_list()
