from PIL import Image
import os

def swap_pixels(image_path, coords1, coords2):
    """
    Меняет местами пиксели, координаты которых указаны в двух списках.
    
    :param image_path: Путь к файлу изображения
    :param coords1: Список кортежей (x, y) первой группы пикселей
    :param coords2: Список кортежей (x, y) второй группы пикселей
    """
    try:
        # Открываем изображение
        with Image.open(image_path) as img:
            # Загружаем карту пикселей для прямого доступа (чтение/запись)
            pixels = img.load()
            width, height = img.size
            
            # Определяем минимальную длину, чтобы не выйти за границы списков,
            # если они разной длины
            limit = min(len(coords1), len(coords2))
            
            swapped_count = 0
            
            for i in range(limit):
                x1, y1 = coords1[i]
                x2, y2 = coords2[i]
                
                # Проверка границ изображения (чтобы не получить ошибку IndexError)
                if (0 <= x1 < width and 0 <= y1 < height) and \
                   (0 <= x2 < width and 0 <= y2 < height):
                    
                    # Python позволяет менять значения местами в одну строку
                    # без использования третьей временной переменной
                    pixels[x1, y1], pixels[x2, y2] = pixels[x2, y2], pixels[x1, y1]
                    swapped_count += 1
            
            print(f"Успешно перемещено пар пикселей: {swapped_count}")
            
            # Показываем результат (откроется стандартный просмотрщик)
            img.show()
            # Можно сохранить результат (опционально)
            # img.save("result_swap.png")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{image_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# --- Блок тестирования ---
if __name__ == "__main__":
    # Создадим тестовое изображение программно, чтобы проверить работу функции
    # без внешних файлов. Белый фон, черный квадрат и красный квадрат.
    test_img_name = "test_source.png"
    img = Image.new("RGB", (100, 100), "white")
    pixels = img.load()
    
    # Рисуем черную точку в (10, 10) и красную в (50, 50)
    pixels[10, 10] = (0, 0, 0)       # Черный
    pixels[50, 50] = (255, 0, 0)     # Красный
    img.save(test_img_name)
    print("Создано тестовое изображение. Черная точка (10,10), Красная (50,50).")

    # Списки координат для обмена
    list_a = [(10, 10)] # Координаты черной точки
    list_b = [(50, 50)] # Координаты красной точки

    print("Выполняем обмен...")
    swap_pixels(test_img_name, list_a, list_b)
    
    # Удаляем временный файл
    if os.path.exists(test_img_name):
        os.remove(test_img_name)