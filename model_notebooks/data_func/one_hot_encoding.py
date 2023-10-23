import pandas as pd


def one_hot_encode(df: pd.DataFrame, col_list: [str]):
  for col in col_list:
    column_to_encode = df[col]
    df_encoded = pd.get_dummies(column_to_encode, prefix=col) # Convert categorical variable into dummy/indicator variables
    df.drop(col, axis=1, inplace=True)
    df_encoded_binary = df_encoded.astype(int) # Convert to binary from boolean
    df = pd.concat([df, df_encoded_binary], axis=1) # Concatenate dataframes
  return df


if __name__ == '__main__':
  data = {'Category': [0, 0, 1, 1, 1, 3, 5],
          'numb': [0, 1, 1, 3, 4, 5, 6],
          'numb2': [0, 2, 1, 3, 4, 5, 6],}
  df = pd.DataFrame(data)
  df_encoded = one_hot_encode(df, ["Category", "numb2"])
  print(df_encoded)
