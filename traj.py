from __future__ import print_function
import warnings
import time

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn import manifold, datasets
from sklearn.decomposition import PCA
from pylab import *

from ase import __version__
from ase.atoms import Atoms
from ase.io.trajectory import Trajectory
from ase.visualize import view

start = time.clock()

prop  = np.loadtxt('md00001_55_hop0.log')
traj  = Trajectory('md00001_55_hop0.traj')

energy      = prop[:,2]
energy_min  = np.amin(energy, axis=0)
energy_max  = np.amax(energy, axis=0)
scale = 10
label       = (energy - energy_min)*scale

length_trajectory = len(traj)
n_atoms = len(traj[-1].get_positions())

i = 0
X = np.zeros((length_trajectory, n_atoms*3))
for atoms in traj:
    a = np.array(atoms.get_positions())
    X[i,:] = a.reshape((a.size))
    i=i+1

# run Isomap on the points in X with n_component dim output
n_neighbors = 3
n_components = 2
Y_iso = manifold.Isomap(n_neighbors, n_components).fit_transform(X)

# run PCA on the points in X with n_component dim output
pca = PCA(n_components=3)
pca.fit(X)
pca_score = pca.explained_variance_ratio_
# print(pca_score)
V = pca.components_
Y_pca = pca.transform(X)

# ND projection
figure()
scatter(Y_iso[:,0], Y_iso[:,1], c = label)

# 3D plot
# fig = figure()
# ax = fig.gca(projection='3d')
# ax.scatter(Y_iso[:,0], Y_iso[:,1], Y_iso[:,2], c = label)

# figure()
# scatter(Y_pca[:,0], Y_pca[:,1], c = label)

# 3D plot
fig = figure()
bx = fig.gca(projection='3d')
bx.scatter(Y_pca[:,0], Y_pca[:,1], Y_pca[:,2], c = label)

show()

stop = time.clock()
print(stop - start)
