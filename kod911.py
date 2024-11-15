import random

def generate_random_points(n):
    """Генерация случайных точек."""
    return [(random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(n)]

def input_points():
    """Ввод точек вручную."""
    points = input("Введите точки в формате (x1, y1), (x2, y2), ... : ")
    points = points.strip().split('), (')
    points = [tuple(map(float, point.strip('()').split(','))) for point in points]
    return points

if __name__ == "__main__":
    # Тестирование функции генерации массива
    num_points = 5  # Количество случайных точек
    points = generate_random_points(num_points)
    print(f"Сгенерированные точки: {points}")

    # Тестирование функции ввода массива
    manual_points = input_points()
    print(f"Введенные точки: {manual_points}")
