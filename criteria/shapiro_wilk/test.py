import numpy as np
from scipy.stats import shapiro

def check(data: np.array) -> np.array:
    stat, p = shapiro(data)
    ans = ""
    tmp = []
    print('Статистика Шапиро-Уилка = %.10f, p=%.10f' % (stat, p))

    # альфа-уровень принятия гиипотезы
    alpha = 0.05

    if p > alpha:
        ans = "нормальное распределение"
        print("данные имеют нормальное распределение")
    else:
        ans = "ненормальное распределение"
        print('данные распределены не по нормальному закону')

    tmp.append([stat, 'Статистика Шапиро-Уилка'])
    tmp.append([p, 'P-значение ({})'.format(ans)])

    return tmp
