import matplotlib.pyplot as plt
import numpy as np

def draw_random_scatter(num_points=50):
    """
    Создает точечную диаграмму со случайными координатами
    и случайным размером маркеров (шариков).
    
    :param num_points: Количество точек на графике
    """
    # 1. Генерируем данные с помощью NumPy
    # Координаты X и Y (случайные числа от 0 до 100)
    x = np.random.randint(0, 100, num_points)
    y = np.random.randint(0, 100, num_points)
    
    # Случайные размеры шариков (от 20 до 1000 пикселей)
    # Параметр s в scatter принимает массив размеров
    sizes = np.random.randint(20, 1000, num_points)
    
    # Случайные цвета для каждой точки (массив случайных чисел для colormap)
    colors = np.random.rand(num_points)

    # 2. Построение графика
    # Создаем фигуру (холст) заданного размера
    plt.figure(figsize=(10, 6))
    
    # Строим точечную диаграмму
    # x, y - координаты
    # s - размеры точек (sizes)
    # c - цвета (colors)
    # alpha - прозрачность (чтобы видеть перекрытия)
    # cmap - цветовая схема (например, 'viridis', 'plasma', 'jet')
    plt.scatter(x, y, s=sizes, c=colors, alpha=0.5, cmap='viridis')

    # Настраиваем отображение цветовой шкалы (справа)
    plt.colorbar(label='Случайное значение цвета')

    # Добавляем сетку и подписи
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.title(f'Случайная точечная диаграмма ({num_points} точек)')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')

    # Отображаем график
    plt.show()

# --- Блок запуска ---
if __name__ == "__main__":
    print("Генерация графика...")
    draw_random_scatter(100) # Генерируем 100 шариков
    print("График построен.")