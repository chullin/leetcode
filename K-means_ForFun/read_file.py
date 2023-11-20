import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer

# 取得當前腳本所在資料夾的絕對路徑
script_path = os.path.dirname(os.path.abspath(__file__))

# 檔案在同一個資料夾，使用相對路徑建構絕對路徑
file_path = os.path.join(script_path, 'abc.xlsx')

# 讀取 Excel 檔案，使用 'openpyxl'，指定 header=None
df = pd.read_excel(file_path, header=None)

# 選擇第二列作為欄位
columns = df.iloc[1]

# 跳過前兩行，重新讀取資料
df = pd.read_excel(file_path, header=None, skiprows=2, names=columns)

# 印出 DataFrame 的欄位名稱
print("DataFrame Columns:", df.columns)

# 選擇要用於 k-means 的三個欄位：tot、sbi 和 bemp
selected_columns = ['tot', 'sbi', 'bemp']

# 檢查所選的欄位是否存在於 DataFrame 中
if all(column in df.columns for column in selected_columns):
    # 選擇所需的欄位
    data = df[selected_columns]

    # 使用 SimpleImputer 將缺失值替換為平均值
    imputer = SimpleImputer(strategy='mean')
    data_imputed = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

    # 使用 KMeans 分群
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(data_imputed)
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_

    # 繪製散點圖
    plt.scatter(data_imputed.iloc[:, 0], data_imputed.iloc[:, 1], c=labels, cmap='viridis', alpha=0.7, edgecolors='k')

    # 繪製中心點
    plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, label='Centers')

    plt.title('K-Means Clustering with Imputed Data')
    plt.xlabel('tot')
    plt.ylabel('sbi')
    plt.legend()
    plt.show()
else:
    print("One or more selected columns are not present in the DataFrame.")