import math

class GeometryCalculator:
    @staticmethod
    def circle_area(radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        return math.pi * radius**2

    @staticmethod
    def triangle_area(side1, side2, side3):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("Длины сторон треугольника должны быть положительными числами")
        if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            raise ValueError("Невозможно построить треугольник с данными сторонами")

        s = (side1 + side2 + side3) / 2
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        return area

    @staticmethod
    def is_right_triangle(side1, side2, side3):
        sides = [side1, side2, side3]
        sides.sort()
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

if __name__ == "__main__":
    # Пример использования
    radius = 5
    side1 = 3
    side2 = 4
    side3 = 5

    calculator = GeometryCalculator()

    circle_area = calculator.circle_area(radius)
    print(f"Площадь круга с радиусом {radius}: {circle_area:.2f}")

    triangle_area = calculator.triangle_area(side1, side2, side3)
    print(f"Площадь треугольника со сторонами {side1}, {side2}, {side3}: {triangle_area:.2f}")

    is_right_triangle = calculator.is_right_triangle(side1, side2, side3)
    print(f"Треугольник со сторонами {side1}, {side2}, {side3} прямоугольный: {is_right_triangle}")
