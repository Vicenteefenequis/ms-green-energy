import math
from decimal import Decimal, ROUND_CEILING


def et(dia_ano):
    return (0.000075 + 0.001868 * math.cos(gama(dia_ano)) - 0.032077 * math.sin(gama(dia_ano))
            - 0.014615 * math.cos(2 * gama(dia_ano)) - 0.04089 * math.sin(2 * gama(dia_ano))) * 229.18


def gama(dia_ano):
    return (2 * math.pi * (dia_ano - 1) / 365) * 180 / math.pi


def deltad(dia_ano):
    return ((0.006918 - 0.399912 * cosd(gama(dia_ano)) + 0.070257 * sind(gama(dia_ano))
             - 0.006758 * cosd(2 * gama(dia_ano)) + 0.000907 * sind(2 * gama(dia_ano)) - 0.002697 * cosd(
                3 * gama(dia_ano))
             + 0.00148 * sind(3 * gama(dia_ano))) * (180 / math.pi))


def sind(a):
    return math.sin(math.radians(a))


def cosd(a):
    return math.cos(math.radians(a))


def acosd(a):
    return math.degrees(math.acos(a))


def temp_celula(temp_ambiente, irradiancia_global_m2, temp_nominal_celula):
    return temp_ambiente + irradiancia_global_m2 * ((temp_nominal_celula - 20) / 800) * 0.9


def roots(a, b, c):
    delta_val = b ** 2 - 4.0 * a * c

    if delta_val > 0.0:
        r1 = (-b - math.sqrt(delta_val)) / (2.0 * a)
        r2 = (-b + math.sqrt(delta_val)) / (2.0 * a)
        return [r1, r2]
    elif delta_val == 0.0:
        r1 = -b / (2.0 * a)
        return [r1, 0]
    else:
        return [0, 0]


def gerar_horas_oficiais(inicio, fim):
    horas_oficiais = [(inicio + i) * 60 for i in range(fim - inicio + 1)]
    return horas_oficiais


def div(a, div_val):
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] /= div_val


def mult(a, mult):
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] *= mult


def ceil_2d_array(a, scale):
    result = []
    for row in a:
        result_row = [round(val, scale) for val in row]
        result.append(result_row)
    return result


def ceil_array(a, scale):
    for i in range(len(a)):
        a[i] = ceil_2d_array(a[i], scale)


def sum_array(a):
    sum_val = [0] * len(a[0])
    for i in a:
        for j in range(len(i)):
            sum_val[j] += i[j]
    return sum_val


def sum_matrix(a, b):
    if len(a) != len(b):
        raise ValueError("As duas matrizes devem possuir o mesmo tamanho")

    sum_mat = [[0] * len(a[0]) for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(a[i])):
            sum_mat[i][j] = a[i][j] + b[i][j]

    return sum_mat


def sum_vectors(a, b):
    if len(a) != len(b):
        raise ValueError("Os dois vetores devem possuir o mesmo tamanho")

    sum_vec = [0] * len(a)

    for i in range(len(a)):
        sum_vec[i] = a[i] + b[i]

    return sum_vec


def sum_vector(a):
    return sum(a)
