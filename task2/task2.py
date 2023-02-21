# Задание 2.

# Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
# length (длина в метрах), width (ширина в метрах).

# Значения данных атрибутов должны передаваться при создании экземпляра класса.


# Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна.
class Road:
    __weight = 0.5

    def __init__(self, length, width):
        self._length = length
        self._width = width
        print(
            f"Создан новый объект класса Road длиной {self._length} метров и шириной {self._width} метров"
        )

    def get_weight(self, thickness):
        ret_val = self._length * self._width * thickness * self.__weight
        print(
            f"Вес асфальта, требуемый для укладки полотна толщиной {thickness} см, равен {ret_val} т"
        )

        return ret_val


r1 = Road(100, 5)
w1 = r1.get_weight(10)

r2 = Road(1000, 20)
w2 = r2.get_weight(20)

print(f"Суммарный вес асфальта для двух объектов = {w1 + w2}")
