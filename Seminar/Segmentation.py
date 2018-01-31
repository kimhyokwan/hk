# PANDAS 패키지 불러오기
from sklearn import datasets
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pymysql
from sqlalchemy import create_engine


def func(row):
    if row['Species'] == 'setosa':
        return 0
    elif row['Species'] == 'virginica':
        return 1
    elif row['Species'] == 'versicolor':
        return 2
    else:
        return 3


# DB 커넥션 열기
engine = create_engine('mysql+pymysql://kopo:kopo@localhost:3306/kopo')

# DB 테이블을 읽어 Data Frame 변수에 저장하기
irisData = pd.read_sql_query('SELECT * FROM iris', engine)

# 컬럼해더 재정의
irisData.columns = ('SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species')
irisData['Species'] = irisData.apply(func, axis=1)

x = pd.DataFrame(irisData, columns=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth'])
y = pd.DataFrame(irisData, columns=['Species'])

# Start with a plot figure of size 12 units wide & 3 units tall
plt.figure(figsize=(12, 3))

# Create an array of three colours, one for each species.
colors = np.array(['red', 'green', 'blue'])

# Draw a Scatter plot for Sepal Length vs Sepal Width
# nrows=1, ncols=2, plot_number=1
# http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.subplot
plt.subplot(1, 2, 1)

# http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.scatter
plt.scatter(x['SepalLength'], x['SepalWidth'], c=colors[y['Species']], s=40)
plt.title('Sepal Length vs Sepal Width')

plt.subplot(1, 2, 2)
plt.scatter(x['PetalLength'], x['PetalWidth'], c=colors[y.Species], s=40)
plt.title('Petal Length vs Petal Width')
plt.show
