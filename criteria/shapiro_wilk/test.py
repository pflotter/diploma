import numpy as np
from scipy.stats import shapiro


def check(data: np.array):
    stat, p = shapiro(data)
    print('Статистика Шапиро-Уилка = %.3f, p=%.3f' % (stat, p))

    # альфа-уровень принятия гиипотезы
    alpha = 0.05

    if p > alpha:
        print("данные имеют нормальное распределение")
    else:
        print('данные распределены не по нормальному закону')