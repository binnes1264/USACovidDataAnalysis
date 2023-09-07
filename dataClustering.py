import pandas as pd
import matplotlib.pyplot as plt

#open newest file
df_old = pd.read_csv('Final_Data.csv')

#create new file
df_new = pd.DataFrame()

#retrieve 'Death' and 'Cases' values
model = df_old.iloc[:,[1, 2]].values

from sklearn.cluster import KMeans

#create clusters that with 'Death' and 'Cases' values
y_kmeans = KMeans(n_clusters = 4, init='k-means++')
y_kmeans = y_kmeans.fit_predict(model)

#print clustering results
#print(y_kmeans)

#create graph of clusters
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

#create legend by colors and display graph
plt.legend()
plt.show()
