from mpl_toolkits.mplot3d import Axes3D
from sklearn import manifold, datasets
from pylab import *
from sklearn.decomposition import PCA
"""
Based on scikits.learn example at
http://scikit-learn.org/stable/auto_examples/manifold/plot_swissroll.html
"""

# load Swiss roll dataset
X, color = datasets.samples_generator.make_swiss_roll(n_samples=1500)
print(len(color))
# print(X)
# run Isomap on the points in X with 2 dim output
n_neighbors = 1
Y_iso = manifold.Isomap(n_neighbors, 2).fit_transform(X)

# run PCA on the points in X with 2 dim output
pca = PCA(n_components=2)
pca.fit(X)
pca_score = pca.explained_variance_ratio_
# print(pca_score)
V = pca.components_
Y_pca = pca.transform(X)

# 3D plot
fig = figure()
ax = fig.gca(projection='3d')
ax.scatter(X[:,0], X[:,1], X[:,2], c=color)

# 2D projection
figure()
scatter(Y_iso[:,0], Y_iso[:,1], c=color)

figure()
scatter(Y_pca[:,0], Y_pca[:,1], c=color)

show()
