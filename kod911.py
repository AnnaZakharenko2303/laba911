import random
import math

def generate_random_points(n):
    """Генерация случайных точек."""
    return [(random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(n)]

def input_points():
    """Ввод точек вручную."""
    points = input("Введите точки в формате (x1, y1), (x2, y2), ... : ")
    points = points.strip().split('), (')
    points = [tuple(map(float, point.strip('()').split(','))) for point in points]
    return points

def distance(point1, point2):
    """Вычисление расстояния между двумя точками."""
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def find_nearest_points(points):
    """Находит ближайшую точку для каждой точки."""
    result = []
    for i, point in enumerate(points):
        nearest_point = None
        min_distance = float('inf')
        for j, other_point in enumerate(points):
            if i != j:
                dist = distance(point, other_point)
                if dist < min_distance:
                    min_distance = dist
                    nearest_point = other_point
        result.append((point, nearest_point))
    return result

def main_menu():
    """Главное меню приложения."""
    while True:
        print("\nМеню:")
        print("1) Генерация случайных точек")
        print("2) Ввод точек вручную")
        print("3) Найти ближайшие точки")
        print("0) Завершение работы")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            num_points = int(input("Введите количество случайных точек: "))
            points = generate_random_points(num_points)
            print(f"Сгенерированные точки: {points}")
        
        elif choice == '2':
            manual_points = input_points()
            print(f"Введенные точки: {manual_points}")
        
        elif choice == '3':
            if 'points' not in locals() and 'manual_points' not in locals():
                print("Ошибка: Необходимо сначала ввести или сгенерировать точки.")
                continue
            
            current_points = manual_points if 'manual_points' in locals() else points
            
            results = find_nearest_points(current_points)
            for point, nearest in results:
                print(f"Точка {point} ближайшая точка {nearest}")
        
        elif choice == '0':
            print("Завершение работы программы.")
            break
        
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()
