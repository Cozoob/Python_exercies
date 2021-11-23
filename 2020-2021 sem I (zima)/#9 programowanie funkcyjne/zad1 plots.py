# Created by Marcin "Cozoob" Kozub 22.11.2021
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
from functools import reduce

def zipWith(xs, ys):
    # f(x,y) = x^2 + y^3
    xs = list(map(lambda x : x**2, xs))
    ys = list(map(lambda y : y**3, ys))
    zs = [xs[i] + ys[i] for i in range(len(xs))]
    return zs


if __name__ == '__main__':
    fig = plt.figure()
    ax = Axes3D(fig)

    xs = [i/3 for j in range(-30, 31) for i in range(-30, 31)]
    ys = [i/3 for i in range(-30, 31) for j in range(-30, 31)]

    # implement getting zs
    zs = zipWith(xs, ys)
    print(zs)

    ax.scatter(xs, ys, zs)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    fig.add_axes(ax)
    plt.show()
    plt.clf()
