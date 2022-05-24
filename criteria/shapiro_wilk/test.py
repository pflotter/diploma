import numpy as np
from scipy.stats import shapiro


def go(data: np.array, alpha: float = 0.05) -> np.array:
    stat, p = shapiro(data)
    print('Статистика Шапиро-Уилка = %.10f, p=%.10f' % (stat, p))

    if p > alpha:
        print("данные имеют нормальное распределение")
    else:
        print('данные распределены не по нормальному закону')

    return [[stat, "Статистика Шапиро-Уилка"],
            [p, "p-value (нормальное распределение)"]]

