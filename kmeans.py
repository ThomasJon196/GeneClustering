
from __future__ import division, print_function
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd


df_stat = pd.read_csv("~/Documents/Studies/Modules/DatenanalyseLifeScience/Tasks/GeneClustering/resources/pawitan-death-stat.csv")
df_genes = pd.read_csv("~/Documents/Studies/Modules/DatenanalyseLifeScience/Tasks/GeneClustering/resources/pawitan-gene-expr.csv")


X = df_genes.transpose().iloc[2:,0:]
X1 = df_genes.iloc[:, 2:]

kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto").fit(X)
# kmeans1 = KMeans(n_clusters=2, random_state=0, n_init="auto").fit(X1)

death_mask = df_stat['DEATH_BC'] == kmeans.labels_
# death_mask2 = df_stat['DEATH_BC'] == kmeans1.labels_

print("(Transpose) Ueberlappung zwischen Clustern und Todesursache Brustkrebsdeath: " + death_mask.sum())
# print("(Transpose) Ueberlappung zwischen Clustern und Todesursache Brustkrebsdeath: " + death_mask2.sum())


#####################################

kmeans_5 = KMeans(n_clusters=5, random_state=0, n_init="auto").fit(X)

np.unique(kmeans.labels_, return_counts=True)

#####################################


import matplotlib.pyplot as plt

plt.scatter(np.arange(0, len(df_genes.iloc[:, 2])), df_genes.iloc[:, 2])
plt.show()



# 1. Verteilung plotten ueber Gene von Gesund vs Ungesund



# Kein Informationen aus Verteilung aller Gene ueber einzelnen Patienten
plt.scatter(np.arange(0, len(df_genes.iloc[:, 2])), df_genes['X027JO'])
plt.show()






################################
## Fuzzy example



# import numpy as np
# import matplotlib.pyplot as plt
# import skfuzzy as fuzz

# colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']

# # Define three cluster centers
# centers = [[4, 2],
#            [1, 7],
#            [5, 6]]

# # Define three cluster sigmas in x and y, respectively
# sigmas = [[0.8, 0.3],
#           [0.3, 0.5],
#           [1.1, 0.7]]

# # Generate test data
# np.random.seed(42)  # Set seed for reproducibility
# xpts = np.zeros(1)
# ypts = np.zeros(1)
# labels = np.zeros(1)
# for i, ((xmu, ymu), (xsigma, ysigma)) in enumerate(zip(centers, sigmas)):
#     xpts = np.hstack((xpts, np.random.standard_normal(200) * xsigma + xmu))
#     ypts = np.hstack((ypts, np.random.standard_normal(200) * ysigma + ymu))
#     labels = np.hstack((labels, np.ones(200) * i))

# # Visualize the test data
# fig0, ax0 = plt.subplots()
# for label in range(3):
#     ax0.plot(xpts[labels == label], ypts[labels == label], '.',
#              color=colors[label])
# ax0.set_title('Test data: 200 points x3 clusters.')
# plt.show()