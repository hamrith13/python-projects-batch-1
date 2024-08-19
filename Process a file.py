import pandas as pd
file_name = "sample_data"
def sort_csv(file_name):
    df = pd.read_csv(file_name)
    print("Available columns:")
    for i, col in enumerate(df.columns, start=1):
        print(f"{i}. {col}")
    column_choice = int(input("Enter the number corresponding to the column you'd like to sort by: ")) - 1
    sort_column = df.columns[column_choice]
    sort_order = input("Enter 'asc' for ascending or 'desc' for descending sort: ").strip().lower()
    ascending = True if sort_order == 'asc' else False
    sorted_df = df.sort_values(by=sort_column, ascending=ascending)
    sorted_df.to_csv(file_name, index=False)
    print(f"File '{file_name}' has been sorted by '{sort_column}' in {'ascending' if ascending else 'descending'} order and saved.")


