"""
Модуль для визуализации работы алгоритмов,
реализованных в рамках этого проекта
"""
from typing import Union, Callable, Tuple

import numpy as np
import plotly.graph_objects as go


def get_points(x: np.array, y: np.array, points: Union[np.array, list],
               function: Callable[[Union[np.array, list]], float]) -> tuple([np.array]):
    """
    Функция создает массив точек для отрисовки графика минимизируемой функции
    :param x            : массив точек x
    :param y            : массив точек y
    :param points       : массив с точками за время работы алгоритма
    :param function     : минимизируемая функция

    :return z           : значения функции в заданных точках
    :return points_x    : координаты точки x
    :return points_y    : координаты точки y
    :return points_z    : значения функции в точках полученных алгоритмом
    """
    x_grid, y_grid = np.meshgrid(x, y)
    grid_points = np.array(list(zip(x_grid, y_grid)))
    z = [function(point) for point in grid_points]
    points_x = [x[0] for x in points]
    points_y = [y[1] for y in points]
    points_z = [function(point) for point in points]
    return z, points_x, points_y, points_z


def graph_near_min(real_minimum: np.array, points: Union[np.array, list],
                   function: Callable[[Union[np.array, list]], float],
                   xlim: tuple([int]), ylim: tuple([int])) -> None:
    """
    Функция для отрисовки графика работы алгоритма

    :param real_minimum : реальный минимум функции
    :param points       : массив с точками за время работы алгоритма
    :param function     : минимизируемая функция
    :param xlim         : кортеж с границами x
    :param ylim         : кортеж с границами y
    """
    left_x, right_x = xlim
    left_y, right_y = ylim
    x = np.linspace(left_x, right_x, 20)
    y = np.linspace(left_y, right_y, 20)
    z, points_x, points_y, _ = get_points(x, y, points, function)
    points_x_near_min = [x for x in points_x if abs(x - real_minimum[0]) <= abs(left_x) | abs(right_x)]
    points_y_near_min = [y for y in points_y if abs(y - real_minimum[1]) <= abs(left_y) | abs(right_y)]
    fig1 = go.Figure(data=[go.Contour(x=x, y=y, z=z, ncontours=15)])
    fig2 = go.Figure(data=[go.Scatter(x=points_x_near_min,
                                      y=points_y_near_min)])
    fig3 = go.Figure(data=[go.Scatter(x=np.array(real_minimum[0]),
                                      y=np.array(real_minimum[1]))])
    fig = go.Figure(data=fig1.data + fig2.data + fig3.data)
    fig.show()


def graph(points: Union[np.array, list],
          function: Callable[[Union[np.array, list]], float],
          xlim: tuple([int]), ylim: tuple([int]), title: str = '') -> None:
    """
    Функция для отрисовки графика работы алгоритма

    :param points       : массив с точками за время работы алгоритма
    :param title        : название графика
    :param function     : минимизируемая функция
    :param xlim         : кортеж с границами x
    :param ylim         : кортеж с границами y
    """
    left_x, right_x = xlim
    left_y, right_y = ylim
    x = np.linspace(left_x, right_x, 50)
    y = np.linspace(left_y, right_y, 50)
    z, points_x, points_y, points_z = get_points(x, y, points, function)
    fig1 = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
    fig2 = go.Figure(data=[go.Scatter3d(x=points_x, y=points_y, z=points_z)])
    fig = go.Figure(data=fig1.data + fig2.data)
    fig.update_layout(title=f'{title}')
    fig.show()
