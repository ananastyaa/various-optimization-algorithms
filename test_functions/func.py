""" Модуль содержит тестовые функции """
from typing import Union

import numpy as np


def test_function_1(points: Union[np.array, list]) -> float:
    """
    Минимизируемая функция
    Реальный минимум находится в точке (0, 0) со значением функции 0

    :param points: координаты точек x, y

    :return: значение функции в точке
    """
    x, y = points
    return x ** 2 + 4 * x * y + 18 * (y ** 2)


def test_function_2(points: Union[np.array, list]) -> float:
    """
    Минимизируемая тестовая функция
    Реальный минимум находится в точке (5, 6) со значением функции 0

    :param points: координаты точек x, y

    :return: значение функции в точке
    """
    x, y = points
    return 4 * (x - 5) ** 2 + (y - 6) ** 2


def test_function_3(points: Union[np.array, list]) -> float:
    """
    Минимизируемая тестовая функция
    Реальный минимум находится в точке (0, 0) со значением функции 0

    :param points: координаты точек x, y

    :return: значение функции в точке
    """
    x, y = points
    return 2 * (x ** 2) + x * y + y ** 2
