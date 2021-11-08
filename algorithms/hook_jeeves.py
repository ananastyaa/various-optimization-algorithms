"""
Модуль реализует алгоритм Хука-Дживса, также известный как метод конфигураций
"""
from typing import Union, Callable

import numpy as np


def hook_jeeves(start_point: Union[np.array, list], eps: float,
                deltas: Union[np.array, list],
                lamb: float, alpha: Union[int, float],
                function: Callable[[Union[np.array, list]], float]) -> tuple([np.array]):
    """
    Функция реализует алгоритм Хука-Дживса (метод конфигураций),
    который представляет собой комбинацию исследующего поиска
    с циклическим изменением переменных и ускоряющего поиска по образцу
    Ознакомиться с работой алгоритма подробнее по ссылке - https://w.wiki/4M77

    :param start_point  : начальная точка
    :param eps          : коээфициент для остановки алгоритма,
                          строго больше нуля
    :param deltas       : начальные величины шагов по координатным направлениям
    :param lamb         : ускоряющий множитель, строго больше нуля
    :param alpha        : коэффициент уменьшения шага, строго больше единицы
    :param function     : минимизируемая функция

    :return minimum     : минимум функции
    :return all_points  : массив со всеми точками за время работы алгоритма
                        (для отрисовки алгоритма по шагам)
    """
    i = 1
    points = np.array(start_point)
    all_points = [start_point]
    basis = np.array([start_point, start_point])
    # начало исследующего поиска
    while True:
        increment_points = np.array(points)
        increment = points[i - 1] + deltas[i - 1]
        increment_points[i - 1] = increment
        if function(increment_points) < function(points):
            points[i - 1] = increment
        else:
            increment = points[i - 1] - deltas[i - 1]
            increment_points[i - 1] = increment
            if function(increment_points) < function(points):
                points[i - 1] = increment

        if i < len(deltas):
            i += 1
            continue

        all_points.append(points)
        if function(points) < function(basis[1]):
            basis[1] = np.array(points)
            points = basis[1] + lamb * (basis[1] - basis[0])
            i = 1
            continue

        points = basis[1]
        basis[0] = basis[1]
        new_deltas = [delta / alpha for delta in deltas if delta <= eps]
        deltas = [delta / alpha if delta > eps else delta for delta in deltas]
        if len(new_deltas) == len(deltas):
            minimum = basis[0]
            break
        i = 1
    return minimum, np.array(all_points)
