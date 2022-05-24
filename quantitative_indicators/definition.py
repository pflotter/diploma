import numpy as np
from scipy import stats


# мат. ожидание по выборке data
def get_mean(data: np.array) -> float:
    return round(np.mean(data), 3)


# среднеквадратичное отклонение по выборке data
def get_standard_deviation(data: np.array) -> float:
    return round(np.std(data), 3)


# медиана по выборке data
def get_median(data: np.array) -> float:
    return np.median(data)


# мода по выборке data
def get_mode(data: np.array) -> float:
    return float(stats.mode(data)[0])


# диапазон значений по выборке data
def get_range(data: np.array) -> float:
    return max(data) - min(data)


# межквартильный диапазон по выборке data:
def get_interquartile_range(data: np.array) -> float:
    tmp = sorted(data)
    quartile_1 = np.median(tmp[:len(tmp) // 2])
    quartile_3 = np.median(tmp[(len(tmp) + 1) // 2:])
    return quartile_3 - quartile_1


# стандартное отклонение по выборке data:
def get_variance(data: np.array) -> float:
    return np.var(data)



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



