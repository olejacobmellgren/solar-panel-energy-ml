import pandas as pd

def combine_columns_sum(df: pd.DataFrame, new_column_name: str, columns_list: [str]):
  df[new_column_name] = df[columns_list].sum(axis=1)
  return df

def combine_columns_sub(df: pd.DataFrame, new_column_name: str, columns_list: [str]):
  df[new_column_name] = df[columns_list[0]]
  for column in columns_list[1:]:
    df[new_column_name] = df[new_column_name] - df[column]
  return df

def combine_columns_multiplication(df: pd.DataFrame, new_column_name: str, columns_list: [str]):
  df[new_column_name] = df[columns_list].product(axis=1)
  return df

def combine_columns_division(df: pd.DataFrame, new_column_name: str, columns_list: [str]):
  df[new_column_name] = df[columns_list[0]]
  for column in columns_list[1:]:
    df[new_column_name] = df[new_column_name] / df[column]
  return df



if __name__ == '__main__':
  df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8], 'C': [9, 10, 11, 12]})
  combine_columns_sum(df, 'D', ['A', 'B', 'C'])
  print(df)
  combine_columns_sub(df, 'E', ['C', 'B', 'A'])
  print(df)
  combine_columns_multiplication(df, 'F', ['A', 'B', 'C'])
  print(df)
  combine_columns_division(df, 'G', ['B', 'A'])
  print(df)