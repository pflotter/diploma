import numpy as np
from scipy.stats import ttest_ind


def test(data_1: np.array,
         data_2: np.array,
         alpha: float = 0.05) -> np.array:

    # необходимо передавать данные одного размера
    if len(data_1) != len(data_2):
        print("разные размеры выборок:", len(data_1), len(data_2))
        return []

    stat, p = ttest_ind(data_1, data_2)
    print('Статистика Стьюдента = %.10f, p=%.10f' % (stat, p))

    if p > alpha:
        print("данные имеют одинаковое распределениие с p value =", p)
    else:
        print("данные имеют различное распределениие с p value =", p)

    return [[stat, "Статистика t-критерия Стьюдента"],
            [p, 'p-value (нормальное распределение)']]
