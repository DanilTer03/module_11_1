'''Библиотека для визуализации (`matplotlib`)

Основные возможности:
- Построение графиков и диаграмм различных типов.
- Настройка внешнего вида графиков, таких как цвета, метки, заголовки и т.д.'''

import matplotlib.pyplot as plt

# Предположим, что у нас есть данные о продажах за год
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [2000, 3000, 2500, 4000, 3500]

plt.figure(figsize=(10, 5))
plt.plot(months, sales, marker='o')
plt.title('Продажи за первый квартал года')
plt.xlabel('Месяцы')
plt.ylabel('Продажи (в $)')
plt.grid()
plt.savefig('sales_plot.png')
plt.show()

'''Создание массива: Мы создаем массив чисел от 0 до 9 с помощью функции `np.arange()`.
Математические операции:
- Увеличиваем каждый элемент на 5.
- Умножаем каждый элемент на 2.
- Вычисляем квадрат каждого элемента с использованием `np.square()`.
 Статистика: Находим среднее значение и сумму элементов массива с помощью `np.mean()` и `np.sum()` соответственно.
Вывод результатов: Результаты вычислений выводятся в консоль.'''

import numpy as np

array = np.arange(10)

print(f"Созданный массив:{array}")

array_plus_5 = array + 5
print("\nМассив после добавления 5:")
print(array_plus_5)

array_times_2 = array * 2
print("Массив после умножения на 2:")
print(array_times_2)

squared_array = np.square(array)
print("Квадраты элементов массива:")
print(squared_array)

mean_value = np.mean(array)
sum_value = np.sum(array)
print(f"Среднее значение: {mean_value}")
print(f"Сумма элементов: {sum_value}")

'''Pillow (PIL) — это библиотека для обработки изображений, которая предоставляет возможность:
Изменять размер, поворачивать, обрезать и применять фильтры к изображениям.
Конвертировать изображения между различными форматами (JPEG, PNG и т. д.), что значительно расширяет возможности обработки медиафайлов.'''

from PIL import Image

image = Image.open('image.jpg')

resized_image = image.resize((400, 400))

rotated_image = resized_image.rotate(90)

rotated_image.save('image_rotated.png')