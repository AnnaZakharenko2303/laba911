import random

def generate_random_points(n):
    """Генерация случайных точек."""
    return [(random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(n)]

if __name__ == "__main__":
    # Тестирование функции генерации массива
    num_points = 5  # Количество случайных точек
    points = generate_random_points(num_points)
    print(f"Сгенерированные точки: {points}")
