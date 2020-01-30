import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cbook
from matplotlib import cm
from matplotlib.colors import LightSource


df = pd.read_csv('./ETH_ALL.csv')
df = df[['DAU', 'Txs', 'Rank']]
points = df.values

def poly_matrix(x, y, order=2):
    """ generate Matrix use with lstsq """
    ncols = (order + 1)**2
    G = np.zeros((x.size, ncols))
    ij = itertools.product(range(order+1), range(order+1))
    for k, (i, j) in enumerate(ij):
        G[:, k] = x**i * y**j
    return G

ordr = 3  # order of polynomial
x, y, z = points.T
x, y = x - x[0], y - y[0]  # this improves accuracy

# make Matrix:
G = poly_matrix(x, y, ordr)
# Solve for np.dot(G, m) = z:
m = np.linalg.lstsq(G, z)[0]


# Evaluate it on a grid...
nx, ny = 30, 30
xx, yy = np.meshgrid(np.linspace(x.min(), x.max(), nx),
                     np.linspace(y.min(), y.max(), ny))
GG = poly_matrix(xx.ravel(), yy.ravel(), ordr)
zz = np.reshape(np.dot(GG, m), xx.shape)

# Plotting (see http://matplotlib.org/examples/mplot3d/custom_shaded_3d_surface.html):
fg, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ls = LightSource(270, 45)
rgb = ls.shade(zz, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
surf = ax.plot_surface(xx, yy, zz, rstride=1, cstride=1, facecolors=rgb,
                       linewidth=0, antialiased=False, shade=False)
ax.plot3D(x, y, z, "o")

fg.canvas.draw()
plt.show()