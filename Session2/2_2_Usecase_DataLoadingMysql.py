# PANDAS 패키지 불러오기
import pandas as pd
import pymysql
from sqlalchemy import create_engine

# DB 커넥션 열기
engine = create_engine('mysql+pymysql://kopo:kopo@localhost:3306/kopo')

# DB 테이블을 읽어 Data Frame 변수에 저장하기
customerData = pd.read_sql_query('SELECT * FROM customerdata', engine)

# 컬럼해더 재정의
customerData.columns = ['CUSTID', 'AVGPRICE', 'EMI', 'DEVICECOUNT', 'PRODUCTAGE', 'CUSTTYPE']

# 데이터 VIEW
customerData

resultname = 'mysqlresult'
customerData.to_sql(resultname, engine, flavor=None
                    , schema=None
                    , if_exists='replace'
                    , index=False
                    , index_label=None
                    , chunksize=None
                    , dtype=None)