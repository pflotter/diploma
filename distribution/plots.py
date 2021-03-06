import scipy.stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Отрисовка переданных данных
def show_distribution(title: str,
                      four_moments_of_distribution: np.array,
                      x_axis: np.array,
                      values_pdf: np.array,
                      values_cdf: np.array,
                      random_values: np.array,
                      ) -> None:
    fig = plt.subplot()

    fig.plot(x_axis, values_pdf, 'r-', lw=5, alpha=0.6, label=title + ' pdf')
    fig.plot(x_axis, values_cdf, 'b-', lw=5, alpha=0.6, label=title + ' cdf')

    fig.hist(random_values, density=True, histtype='stepfilled', alpha=0.2, label=title)
    fig.legend(loc='best', frameon=False)
    plt.show()


def show_normal(size: int = 100) -> None:
    x_axis = np.linspace(scipy.stats.norm.ppf(0.01), scipy.stats.norm.ppf(0.99), size)
    values_pdf = scipy.stats.norm.pdf(x_axis)
    values_cdf = scipy.stats.norm.cdf(x_axis)
    random_values = scipy.stats.norm.rvs(size=size * size)

    four_moments_of_distribution = scipy.stats.norm.stats(moments='mvsk')

    show_distribution("normal",
                      four_moments_of_distribution,
                      x_axis,
                      values_pdf,
                      values_cdf,
                      random_values)


def show_uniform(size: int = 100) -> None:
    x_axis = np.linspace(scipy.stats.uniform.ppf(0.01), scipy.stats.uniform.ppf(0.99), size)
    values_pdf = scipy.stats.uniform.pdf(x_axis)
    values_cdf = scipy.stats.uniform.cdf(x_axis)
    random_values = scipy.stats.uniform.rvs(size=size * 10)

    four_moments_of_distribution = scipy.stats.uniform.stats(moments='mvsk')

    show_distribution("uniform",
                      four_moments_of_distribution,
                      x_axis,
                      values_pdf,
                      values_cdf,
                      random_values)


def show_logistic(size: int = 100) -> None:
    x_axis = np.linspace(scipy.stats.logistic.ppf(0.01), scipy.stats.logistic.ppf(0.99), size)
    values_pdf = scipy.stats.logistic.pdf(x_axis)
    values_cdf = scipy.stats.logistic.cdf(x_axis)
    random_values = scipy.stats.logistic.rvs(size=size * 10)

    four_moments_of_distribution = scipy.stats.logistic.stats(moments='mvsk')

    show_distribution("logistic",
                      four_moments_of_distribution,
                      x_axis,
                      values_pdf,
                      values_cdf,
                      random_values)


def show_example(size: int) -> None:
    show_normal(size)
    show_uniform(size)
    show_logistic(size)


def show_plot(title: str = "current row", data: np.array = []) -> None:
    sns.kdeplot(data=data)
    ax = plt.subplot()
    ax.grid()
    ax.set_xlabel(title)
    plt.show()

#
def get_xy_plot_values(data: np.array) -> [np.array, np.array]:
    # преобразует набор чисел в двух размерную штуковину, высчитывает плотность по У
    plot = sns.kdeplot(data=data)
    line = plot.lines[0]
    x, y = line.get_data()
    return x, y



if __name__ == "__main__":
    show_example(size=100)