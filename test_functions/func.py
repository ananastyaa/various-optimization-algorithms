""" Модуль содержит тестовые функции """
import numpy as np


def math_function(points: np.array) -> int:
    """
    Минимизируемая функция

    :param points: координаты точек x, y

    :return: значение функции в точке
    """
    return points[0] ** 2 + 4 * points[0] * points[1] + 18 * (points[1] ** 2)


def test_function(points: np.array) -> int:
    """
    Минимизируемая тестовая функция

    :param points: координаты точек x, y

    :return: значение функции в точке
    """
    return 4 * (points[0] - 5) ** 2 + (points[1] - 6) ** 2


def test_function_two(points: np.array) -> int:
    """
    Минимизируемая тестовая функция

    :param points: координаты точек x, y

    :return: значение функции в точке
    """
    return 2 * (points[0] ** 2) + points[0] * points[1] + points[1] ** 2
