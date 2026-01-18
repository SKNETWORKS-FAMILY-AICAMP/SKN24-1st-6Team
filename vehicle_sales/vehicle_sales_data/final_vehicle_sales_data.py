import pandas as pd

data = pd.read_csv('vehicle_sales_data.csv')
data.dropna(inplace=True)
data.drop_duplicates()

print(data['모델명'].str.len().max())

data['연월'] = pd.to_datetime(data['연월'])
data['판매량'] = pd.to_numeric(data['판매량'])

print(data.info())

data.to_csv('final_vehicle_sales_data.csv', index=False)