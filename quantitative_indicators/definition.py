### Normal distribution

# Independent groups
def student_t_criterion(title: str='') -> None:
    return title + ' | student_t_criterion'

# Dependent groups

        # Парный критерий стьюдента
def student_paired_criterion(title: str='') -> None:
    return title + ' | student_paired_criterion'

def pearson_normal(title: str='') -> None:
    return title + ' | pearson_normal'
################################################################################
### Not normal distribution

# Independent groups
def mann_whitney_criterion(title: str='') -> None:
    return title + ' | mann_whitney_criterion'

# Dependent groups

def kolmogorov_smirnov_criterion(title: str='') -> None:
    return title + ' | kolmogorov_smirnov_criterion'



