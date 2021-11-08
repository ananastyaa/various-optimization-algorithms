""" Модуль содержит реализацию метода Розенброка """
from typing import Union, Callable

import numpy as np


def gram_schmidt(directions: np.array, difference: np.array) -> np.array:
    """
    Функция, реализующая процедуру Грамма - Шмидта

    :param directions       : координатные направления
    :param difference       : разность точек x(k+1) - x(k)
                              (старый и новый базисы полученные
                              при работе метода Розенброка)

    :return new_directions  : новые координатные направления
    """
    lambdas = np.linalg.solve(directions.T, difference)
    b, new_directions = [], []
    a = [lambdas[i:].dot(directions[i:]) for i in range(len(lambdas))]
    b.append(a[0])
    new_directions.append(a[0] / np.linalg.norm(a[0]))
    for i in range(1, len(a)):
        b.append(a[i] - (a[i].T).dot(new_directions[i - 1])
                 * new_directions[i - 1])
        new_directions.append(b[i] / np.linalg.norm(b[i]))
    return np.array(new_directions)


def rosenbrock(start_point: Union[np.array, list], eps: float,
               start_deltas: Union[np.array, list], max_fail: int,
               function: Callable[[Union[np.array, list]], float],
               alpha: float = 3, beta: float = -0.5) -> tuple([np.array]):
    """
    Функция реализующая метод Розенброка
    Суть метода в том, что задается начальная точка
    из которой осуществляется итеративный поиск направления
    убывания функции с помощью изменяемых дискретных шагов вдоль n линейно
    независимых и ортогональных направлений.
    Розенброк рекомендовал следующие коэффициенты растяжения и сжатия:
    alpha = 3, beta = –0.5
    Ознакомиться с работой алгоритма подробнее по ссылке - https://w.wiki/4MDg

    :param start_point      : начальная точка
    :param eps              : коээфициент для остановки алгоритма,
                              строго больше 0
    :param deltas           : массив начальных длин шага вдоль каждого
                              из направлений поиска
    :param max_fail         : максимальное число неудачных серий шагов
                              по всем направлениям на одной итерации
    :param function         : минимизируемая функция
    :param alpha            : коээфициент растяжения, строго больше 1
    :param beta             : коээфициент сжатия лежит в интервале от -1 до 0

    :return minimum         : координаты точки минимума
    :return all_points      : все точки за время работы алгоритма
    """
    # выбираем начальные линейно независимые и ортогональные направления
    directions = np.eye(len(start_deltas))
    deltas = np.array(start_deltas)
    iterations = count = 0
    i = 1
    all_points = []
    points, basis = np.array(start_point), np.array(start_point)
    while True:
        pred_deltas = np.array(deltas)
        increment = points + directions[i - 1] * deltas[i - 1]
        if function(increment) < function(points):
            all_points.append(points)
            points = increment
            deltas[i - 1] *= alpha
        else:
            deltas[i - 1] *= beta

        if i < len(deltas):
            i = i + 1
            continue
        # проверим успешность поиска по текущим ортогональным направлениям
        if function(points) < function(start_point):
            if count:
                count = 0
            start_point = np.array(points)
            i = 1
            continue

        if function(points) == function(start_point):
            if function(points) < function(basis):
                if count:
                    count = 0

            if function(points) == function(basis):
                count += 1
                if count < max_fail:
                    lenght = len([delta for delta in pred_deltas
                                  if abs(delta) <= eps])
                    if lenght == len(pred_deltas):
                        minimum = basis
                        all_points.append(minimum)
                        break
                    start_point = np.array(points)
                    i = 1
                    continue
            old_basis = np.array(basis)
            basis = np.array(points)
            if np.linalg.norm(basis - old_basis) <= eps:
                minimum = basis
                all_points.append(minimum)
                break

            directions = gram_schmidt(directions, basis - old_basis)
            iterations += 1
            deltas = np.array(start_deltas)
            start_point = np.array(old_basis)
            i = 1
    return minimum, np.array(all_points)
