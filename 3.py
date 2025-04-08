def merge_vowel_sets():
    initial_set = {'c', 'd'}
    vowels_set = {'a', 'e', 'i', 'o', 'u', 'y'}

    try:
        result_set = initial_set.union(vowels_set)
    except TypeError:
        print("Не вдалося виконати операцію напряму, перетворюємо через список.")
        temp_list = list(initial_set) + list(vowels_set)
        result_set = set(temp_list)

    print("Результуюча множина:", result_set)

merge_vowel_sets()
