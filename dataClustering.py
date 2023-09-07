import pandas as pd
import matplotlib.pyplot as plt

df_old = pd.read_csv('Final_Data.csv')

df_new = pd.DataFrame()

model = df_old.iloc[:,[1, 2]].values

labels = df_old.Region

from sklearn.cluster import KMeans

y_kmeans = KMeans(n_clusters = 4, init='k-means++')
y_kmeans = y_kmeans.fit_predict(model)

print(y_kmeans)

plt.figure(figsize = (8, 5))
plt.yscale("log")
plt.xscale("log")
plt.title('Clusters of Covid by State')
plt.xlabel('Cases')
plt.ylabel('Deaths')
plt.scatter(model[y_kmeans==0, 0], model[y_kmeans==0, 1], s=100, c='red', label ='Cluster 1')
plt.scatter(model[y_kmeans==1, 0], model[y_kmeans==1, 1], s=100, c='blue', label ='Cluster 2')
plt.scatter(model[y_kmeans==2, 0], model[y_kmeans==2, 1], s=100, c='green', label ='Cluster 3')
plt.scatter(model[y_kmeans==3, 0], model[y_kmeans==3, 1], s=100, c='cyan', label ='Cluster 4')

plt.legend()
plt.show()