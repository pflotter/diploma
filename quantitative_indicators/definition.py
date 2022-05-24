import numpy as np
from scipy import stats


# мат. ожидание по выборке data
def get_mean(data: np.array) -> np.array:
    return [round(np.mean(data), 3), 'Мат. ожидание: ']


# среднеквадратичное отклонение по выборке data
def get_standard_deviation(data: np.array) -> np.array:
    return [round(np.std(data), 3), 'Среднеквадратичное отклонение: ']


# медиана по выборке data
def get_median(data: np.array) -> np.array:
    return [np.median(data), 'Медиана: ']


# мода по выборке data
def get_mode(data: np.array) -> np.array:
    return [float(stats.mode(data)[0]), 'Мода: ']


# диапазон значений по выборке data
def get_range(data: np.array) -> np.array:
    return [max(data) - min(data), 'Диапазон значений: ']


# межквартильный диапазон по выборке data:
def get_interquartile_range(data: np.array) -> np.array:
    tmp = sorted(data)
    quartile_1 = np.median(tmp[:len(tmp) // 2])
    quartile_3 = np.median(tmp[(len(tmp) + 1) // 2:])
    return [quartile_3 - quartile_1, 'Межквартильный диапазон: ']





### Normal distribution

# Independent groups
def student_t_criterion(title: str='') -> None:
    return title

# Dependent groups

        # Парный критерий стьюдента
    #def student_paired_criterion

################################################################################
### Not normal distribution

# Independent groups
    #def mann_whitney_criterion

# Dependent groups

    #def kolmogorov_smirnov_criterion



