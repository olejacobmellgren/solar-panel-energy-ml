"""
Python file containing funcitons for aggregating data within a dataframe
Date: 10/10/2023
"""
import pandas as pd
import numpy as np

agg_types = ['count', 
             'sum',
             'mean',
             'median',
             'min',
             'max',
             'mode',
             'std',
             'var']

def stocastic_median(x_list):
    s = np.median(x_list)
    return int(s)


def gen_agg(df: pd.DataFrame, agg_type, batch_size: int = 4) -> pd.DataFrame:
    """
    Pass dataframe WITH date_forecast value and choose aggregation type by passing string to 'agg_type'

        - count -> Number of non-null observations
        - sum -> Sum of values
        - mean -> Mean of values
        - median -> Arithmetic median of values, e.g. middle of ordered dataset
        - min -> Minimum
        - max -> Maximum
        - std -> Standard deviation
        - var -> Variance

        Also possible to pass aggregation function directly f.eks. np.mean
    """
    agg_func = {col: agg_type for col in df.columns[1:]} # [1:] assumes 'date_forecast' is first
    return df.groupby(df.index // batch_size).agg({**{'date_forecast': 'last'}, **agg_func})


def agg_test(df: pd.DataFrame, agg_type, batch_size: int = 4) -> pd.DataFrame:
    agg_func = {col: agg_type for col in df.columns} # [1:] assumes 'date_forecast' is first
    return df.groupby(df.index // batch_size).agg({**agg_func})

if __name__ == '__main__':
    df = pd.DataFrame(data=[0,1,1,3,4,5,6,7,8,9,10,11,12,13,14,15], columns=['numb'])
    print(df)
    dfa = agg_test(df, 'mean')
    print(f'mean aggregation \n{dfa}')
    dfa = agg_test(df, 'median')
    print(f'median aggregation \n{dfa}')
    dfa = agg_test(df, 'sum')
    print(f'sum aggregation \n{dfa}')
    dfa = agg_test(df, stocastic_median)
    print(f'mode aggregation \n{dfa}')