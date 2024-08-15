import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.read_excel('sales_data.xlsx')

df['Sales'].fillna(df['Sales'].mean(), inplace=True)

scaler = MinMaxScaler()
df['sales_normalized'] = scaler.fit_transform(df[['Sales']])

scaler = StandardScaler()
df['sales_standardized'] = scaler.fit_transform(df[['Sales']])

df.to_excel('processed_data.xlsx', index=False)
