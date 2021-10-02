# Created by Marcin "Cozoob" Kozub 02.10.2021
import matplotlib.pyplot as plt
from math import log
from random import randint

def log_distribution(dist_probes):
    new_dist_probes = []
    for probe in dist_probes:
        try:
            new_dist_probes.append(log(probe))
        except ValueError:
            pass

    return dist_probes

def plot_histogram(values):
    plt.hist(values)
    plt.show()

if __name__ == '__main__':
    dist_probes = [randint(-20, 1001) for _ in range(10000)]
    new = log_distribution(dist_probes)
    print(new)
    plot_histogram(new)