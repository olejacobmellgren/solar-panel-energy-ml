import pandas as pd
import numpy as np

def date_forecast_columns(df: pd.DataFrame):

  date_forecast = df['date_forecast']
  
  df['year'] = date_forecast.dt.year
  df['month'] = date_forecast.dt.month
  df['day'] = date_forecast.dt.day
  df['hours'] = date_forecast.dt.hour

  # df.drop(columns=['date_forecast'], inplace=True)
  return df


if __name__ == '__main__':
  df = pd.DataFrame({'date_forecast': [np.datetime64('2019-06-02T23:00:00.000Z'), np.datetime64('2019-06-04T22:00:00.000Z'), np.datetime64('2019-06-03T10:00:00.000Z')]})
  df = date_forecast_columns(df)
  print(df)
