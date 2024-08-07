import pandas as pd

df = pd.read_csv('sales.csv')





sales_summary = df.groupby('Product').agg({'Sales per Product': 'first', 'amount': ['sum', 'mean']}).reset_index()


sales_summary.columns = ['Product', 'Sales per Product', 'Total Sales', 'Average Sales']


sales_summary.to_csv('output.csv')


