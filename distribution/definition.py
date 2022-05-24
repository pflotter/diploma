from scipy.stats import logistic, uniform, norm, pearsonr
import numpy as np

# Высчитывает мат.Ожидание, СКО и корреляции между распределениями

def check_pearson_correlation_coefficient(data: np.array) -> None:
    data.sort()
    temp = []

    print("Мат ожидание", str(round(np.mean(data), 3)))
    print("СКО", str(round(np.std(data), 3)))

    p = np.arange(0, len(data), 1) / len(data)
    pu = uniform.cdf(data / (np.max(data)))  # равномерное интегральное  распределение
    pn = norm.cdf(data, np.mean(data), np.std(data))  # нормальное интегральное  распределение
    pl = logistic.cdf(data, np.mean(data), np.std(data))  # логистическое  интегральное  распределение

    print("Корреляция между нормальным распределением и тестовым ", str(round(pearsonr(pn, p)[0], 3)))
    print("Корреляция между логистическим распределением и тестовым ", str(round(pearsonr(pl, p)[0], 3)))
    print("Корреляция между равномерным  распределением и тестовым ", str(round(pearsonr(pu, p)[0], 3)))

    temp = [str(round(np.mean(data), 3)), str(round(np.std(data), 3)), str(round(pearsonr(pn, p)[0], 3)), str(round(pearsonr(pl, p)[0], 3)), str(round(pearsonr(pu, p)[0], 3))]
    return temp

