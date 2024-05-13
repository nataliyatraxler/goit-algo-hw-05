def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    upper_bound = None
    iterations = 0
    
    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
            upper_bound = arr[mid]  # Оновлюємо верхню межу
        else:
            # Знайдено точне співпадіння
            # Наступний елемент буде верхньою межею, якщо існує
            if mid + 1 < len(arr):
                upper_bound = arr[mid + 1]
            else:
                upper_bound = arr[mid]  # Якщо це останній елемент, він же є верхньою межею
            break
    
    # Якщо не знайшли співпадіння і left вийшло за межі, шукаємо перший елемент правіше останньої перевіреної позиції
    if upper_bound is None and left < len(arr):
        upper_bound = arr[left]
    elif upper_bound is None:
        # Якщо target більше за всі елементи, повертаємо максимальний елемент
        upper_bound = arr[-1]

    return (iterations, upper_bound)

# Приклад використання:
arr = [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]
print(binary_search(arr, 3.5))  
print(binary_search(arr, 4))    
print(binary_search(arr, 6.0)) 
