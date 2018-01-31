# PANDAS 패키지 불러오기
from sklearn import datasets
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pymysql
from sqlalchemy import create_engine


def func(row):
    if row['custtype'] == 'Big-Screen-lover':
        return 0
    elif row['custtype'] == 'Sleeping-dog':
        return 1
    elif row['custtype'] == 'Early-bird':
        return 2
    else:
        return 3

# DB 커넥션 열기
engine = create_engine('mysql+pymysql://kopo:kopo@localhost:3306/kopo')

# DB 테이블을 읽어 Data Frame 변수에 저장하기
customerData = pd.read_sql_query('SELECT * FROM kopo_customerdata2', engine)
customerData

# 컬럼해더 재정의
customerData.columns = ('custid', 'averageprice', 'emi', 'devicecount', 'productage', 'custtype')
customerData['custtype'] = customerData.apply(func, axis=1)
print(customerData)

# 'averageprice', 'emi',
x = pd.DataFrame(customerData, columns=['devicecount', 'productage'])
y = pd.DataFrame(customerData, columns=['custtype'])
plt.figure(figsize=(12, 3))

# Create an array of three colours, one for each species.
colors = np.array(['red', 'green', 'blue'])

# Draw a Scatter plot for Sepal Length vs Sepal Width
# nrows=1, ncols=2, plot_number=1
# http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.subplot
plt.subplot(1, 2, 1)

# http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.scatter
plt.scatter(x['productage'], x['devicecount'], c=colors[y['custtype']], s=40)
plt.title('productage vs devicecount')
#plt.show()

# create a model object with 3 clusters
# http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans
# http://scikit-learn.org/stable/modules/clustering.html#k-means
model = KMeans(n_clusters=3)
model.fit(x)
# print(model.labels_)

# Start with a plot figure of size 12 units wide & 3 units tall
plt.figure(figsize=(12, 3))

# Create an array of three colours, one for each species.
colors = np.array(['red', 'green', 'blue'])

# The fudge to reorder the cluster ids.
predictedY = np.choose(model.labels_, [1, 0, 2]).astype(np.int64)

colormap = np.array(['red', 'green', 'blue'])
# Plot the classifications that we saw earlier between Petal Length and Petal Width
plt.subplot(1, 2, 1)
plt.scatter(x['productage'], x['devicecount'], c=colormap[y['custtype']], s=40)
plt.xlabel("productage")
plt.ylabel("devicecount")
plt.title('Before clustering')

# Plot the classifications according to the model
plt.subplot(1, 2, 2)
plt.scatter(x['productage'], x['devicecount'], c=colormap[predictedY], s=40)
plt.title("Model's clustering")
plt.xlabel("productage")
plt.ylabel("devicecount")
plt.show()