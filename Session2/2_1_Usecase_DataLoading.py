# PANDAS 패키지 불러오기
import pandas as pd

# CSV 파일을 읽어 Data Frame 변수에 저장하기
customerData = pd.read_csv("C:\pythonWorkspace\hk\Session2\customer_data.csv")
# , header=None)

# 컬럼해더 재정의
customerData.columns = ['CUSTID', 'AVGPRICE', 'EMI', 'DEVICECOUNT', 'PRODUCTAGE', 'CUSTTYPE']

# 데이터 VIEW

# CSV 파일로 저장
customerData.to_csv("C:\pythonWorkspace\hk\Session2\customerindata.csv", index=False)
customerData

