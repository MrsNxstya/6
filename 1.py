def split_list_by_index():
    input_str = input("Введіть елементи списку через пробіл: ")
    lst = input_str.split()

    while True:
        try:
            index = int(input(f"Введіть порядковий номер елемента для розбиття (від 0 до {len(lst)}): "))
            if 0 <= index <= len(lst):
                break
            else:
                print("Помилка: індекс виходить за межі списку.")
        except ValueError:
            print("Помилка: введіть ціле число.")

    first_part = lst[:index]
    second_part = lst[index:]

    print("Перша частина списку:", first_part)
    print("Друга частина списку:", second_part)

split_list_by_index()
