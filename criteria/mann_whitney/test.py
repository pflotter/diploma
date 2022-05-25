import numpy as np
from scipy.stats import mannwhitneyu


def go(data_1: np.array,
       data_2: np.array,
       alpha: float = 0.05) -> np.array:

    # необходимо передавать данные одного размера
    if len(data_1) != len(data_2):
        print("разные размеры выборок:", len(data_1), len(data_2))
        return []

    stat, p = mannwhitneyu(data_1, data_2)
    ans = ""
    print('Statistics=%.10f, p=%.10f' % (stat, p))

    if p > alpha:
        print('Same distribution (fail to reject H0)')
        ans = "Выборки равны"
    else:
        print('Different distribution (reject H0)')
        ans = "Выборки разные"

    return [[stat, "Статистика Манна—Уитни"],
            [p, "p-value ({})".format(ans)]]
