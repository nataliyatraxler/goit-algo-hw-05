import requests
import timeit

# Функція для завантаження текстів з Google Drive
def download_text_from_drive(doc_id):
    url = f"https://drive.google.com/uc?id={doc_id}&export=download"
    response = requests.get(url)
    response.raise_for_status()
    return response.text

# Алгоритм Кнута-Морріса-Пратта
def knuth_morris_pratt(text, pattern):
    # Створення LPS (longest proper prefix which is suffix) масиву
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    # Власне пошук підрядка
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            return i - j  # Позиція знаходження підрядка

        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# Функції для інших алгоритмів
def boyer_moore(text, pattern):
    # Треба додати реалізацію
    pass

def rabin_karp(text, pattern):
    # Треба додати реалізацію
    pass

def measure_time(algorithm, text, pattern):
    setup_code = f"from __main__ import {algorithm.__name__}"
    stmt = f"{algorithm.__name__}(text, pattern)"
    # Додаємо text та pattern в globals, щоб вони були доступні в середовищі виконання timeit
    return min(timeit.repeat(setup=setup_code, stmt=stmt, repeat=3, number=100, globals={'text': text, 'pattern': pattern, algorithm.__name__: algorithm}))


# Ідентифікатори документів
doc_id1 = '18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh'
doc_id2 = '13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ'

# Завантаження текстів
text1 = download_text_from_drive(doc_id1)
text2 = download_text_from_drive(doc_id2)

# Підрядки для пошуку
existing_substring = "example"  # Змініть на підрядок, який точно існує в тексті
fake_substring = "fakestring123"  # Підрядок, якого немає в тексті

# Порівняння алгоритмів
algorithms = [knuth_morris_pratt, boyer_moore, rabin_karp]
results = {}
for alg in algorithms:
    results[alg.__name__] = {
        "Article 1 - Existing": measure_time(alg, text1, existing_substring),
        "Article 1 - Fake": measure_time(alg, text1, fake_substring),
        "Article 2 - Existing": measure_time(alg, text2, existing_substring),
        "Article 2 - Fake": measure_time(alg, text2, fake_substring),
    }

# Виведення результатів
for name, times in results.items():
    print(f"Results for {name}:")
    for desc, time in times.items():
        print(f"{desc}: {time:.7f} seconds")