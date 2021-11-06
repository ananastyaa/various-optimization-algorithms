""" Модуль содержит тестовые функции """
import numpy as np
from typing import Union


def math_function(points: Union[np.array, list]) -> float:
    """
    Минимизируемая функция

    :param points: координаты точек x, y

    :return: значение функции в точке
    """
    return points[0] ** 2 + 4 * points[0] * points[1] + 18 * (points[1] ** 2)


def test_function(points: Union[np.array, list]) -> float:
    """
    Минимизируемая тестовая функция

    :param points: координаты точек x, y

    :return: значение функции в точке
    """
    return 4 * (points[0] - 5) ** 2 + (points[1] - 6) ** 2


def test_function_two(points: Union[np.array, list]) -> float:
    """
    Минимизируемая тестовая функция

    :param points: координаты точек x, y

    :return: значение функции в точке
    """
    return 2 * (points[0] ** 2) + points[0] * points[1] + points[1] ** 2
