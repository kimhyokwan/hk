import pandas as pd
from sqlalchemy import create_engine

# DB 커넥션 열기
engine = create_engine('oracle+cx_oracle://kopo:kopo@localhost:1521/XE')

# DB 테이블을 읽어 Data Frame 변수에 저장하기
customerData = pd.read_sql_query('SELECT * FROM customerdata', engine)

# 컬럼해더 재정의
customerData.columns = ['CUSTID', 'AVGPRICE', 'EMI', 'DEVICECOUNT', 'PRODUCTAGE', 'CUSTTYPE']

# 데이터 VIEW
customerData

resultname = 'oracleresult'
customerData.to_sql(resultname, engine, if_exists='replace', index=False)
