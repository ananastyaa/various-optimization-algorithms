"""
Модуль содержит реализацию метода Нелдера - Мида, так же известного,
как метод деформируемого многогранника
Функция описанная ниже, возвращает массив точек вида
[[[x, y], [x, y], [x, y]], [...]]],
пакет визуализации не работает с массивами такого вида,
но если вы хотите использовать этот пакет и увидеть корректный результат,
перед тем как передавать массив с точками сверните его в одно измерение
с помощью np.flatten. Например так,
points = points.flatten()
points = [point.flatten() for point in points]
"""
from typing import Union, Callable
from operator import itemgetter

import numpy as np


def nelder_mead(vertexes: Union[np.array, list], eps: float,
                function: Callable[[Union[np.array, list]], float],
                alpha: float = 1, beta: float = 0.5,
                gamma: float = 2.5) -> tuple([np.array]):
    """
    Функция реализующая алгоритм Нелдера - Мида
    В основу метода деформируемого многогранника положено построение
    последовательности систем n + 1 точек, которые являются
    вершинами выпуклого многогранника
    Нелдер и Мид рекомендуют использовать следующие значения
    параметров alpha = 1, beta = 0.5, gamma = 2
    Ознакомиться с работой алгоритма подробнее по ссылке - https://w.wiki/4MCG

    :param vertexes         : начальные координаты вершин многогранника
    :param eps              : коээфициент для остановки алгоритма,
                              строго больше нуля
    :param function         : минимизируемая функция
    :param alpha            : коээфициент отражения в большинстве случаев
                              равен 1
    :param beta             : коээфициент сжатия, лежит в интервале
                              от 0.4 до 0.6
    :param gamma            : коээфициент растяжения, лежит в интервале
                              от 2 до 3

    :return minimum         : координты точки минимума
    :return all_vertexes    : массив с координатами вершин за время работы
                              алгоритма (для отрисовки по шагам)
    """
    iterations = 0
    all_vertexes = []
    while True:
        points = np.array(sorted([(vertex, function(vertex))
                                  for vertex in vertexes], key=itemgetter(1)))
        vertexes = points[:, 0]
        all_vertexes.append(vertexes)
        center = 1 / (len(vertexes) - 1) * sum(points[:-1, 0])
        norm = np.linalg.norm(points[:, 1] - function(center))
        sigma = (1 / len(vertexes) * norm) ** (1 / 2)
        if sigma <= eps:
            minimum = points[0]
            break
        reflect = center + alpha * (center - points[-1, 0])
        if function(reflect) <= points[0, 1]:
            stretch = center + gamma * (reflect - center)
            if function(stretch) < points[0, 1]:
                vertexes[-1] = stretch
            else:
                vertexes[-1] = reflect
        if points[-2, 1] < function(reflect) <= points[-1, 1]:
            compress = center + beta * (vertexes[-1] - center)
            vertexes[-1] = compress
        if points[0, 1] < function(reflect) <= points[-2, 1]:
            vertexes[-1] = reflect
        if function(reflect) > points[-1, 1]:
            vertexes = [points[0, 0] + ((1 / 2) * (vertex - points[0, 0]))
                        for vertex in vertexes]
        iterations += 1
    return minimum, np.array(all_vertexes)
