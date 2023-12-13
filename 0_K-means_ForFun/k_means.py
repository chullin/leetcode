from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# 生成一些隨機數據
data = np.random.rand(100, 2)

# 指定要分成的群數
num_clusters = 3

# 使用 KMeans 演算法進行聚類
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(data)

# 獲取每個樣本的所屬群組
labels = kmeans.labels_

# 獲取每個群組的中心
centers = kmeans.cluster_centers_

# 視覺化數據和 K-means 結果
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', alpha=0.7, edgecolors='b')
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, label='Cluster Centers')
plt.title('K-means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()
