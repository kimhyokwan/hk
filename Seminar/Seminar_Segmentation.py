from sklearn import datasets
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# DB 커넥션 열기
engine = create_engine('mysql+pymysql://kopo:kopo@localhost:3306/kopo')

# DB 테이블을 읽어 Data Frame 변수에 저장하기
customerData = pd.read_sql_query('SELECT * FROM customerdata', engine)

# 컬럼해더 재정의
customerData.columns = ['CUSTID', 'AVGPRICE', 'EMI', 'DEVICECOUNT', 'PRODUCTAGE', 'CUSTTYPE']

# 데이터 VIEW
customerData