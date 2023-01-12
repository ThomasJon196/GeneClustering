import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import pandas as pd

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]


df_stat = pd.read_csv("~/Documents/Studies/Modules/DatenanalyseLifeScience/Tasks/GeneClustering/resources/pawitan-death-stat.csv")
df_genes = pd.read_csv("~/Documents/Studies/Modules/DatenanalyseLifeScience/Tasks/GeneClustering/resources/pawitan-gene-expr.csv")

data = df_genes.iloc[:, 2:]


linkage_data = linkage(data.transpose(), method='ward', metric='euclidean')
dendrogram(linkage_data)

plt.show()