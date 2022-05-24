import numpy as np
from scipy.stats import kruskal


def go(all_data: np.array, alpha: float = 0.05) -> np.array:

    stat, p = kruskal(all_data[0], all_data[1], all_data[2])
    print('Statistics=%.3f, p=%.3f' % (stat, p))

    if p > alpha:
        print("одинаковые распределения")
    else:
        print("различные распределения")

    return [[stat, "Статистика Краскела-Уоллиса"],
            [p, "p-value (Краскела-Уоллиса)"]]
