import pandas as pd

def multiply_columns(A: pd.Series, B: pd.Series) -> pd.Series:
    '''
    Given two pandas series, returns a series with multiplied values. 

    NB! Series A and B must be of same length
    '''

    if len(A) != len(B): 
        raise Exception("In multiply columns -> length of series is not equal")
    
    C = A*B

    return C
    
def divide_columns(A: pd.Series, B: pd.Series) -> pd.Series:
    '''
    Given two pandas series, returns a series with divided values A/B. 

    NB! Series A and B must be of same length
    In case of a value pair with zero division, you're on your own...
    '''
    if len(A) != len(B): 
        raise Exception("In multiply columns -> length of series is not equal")

    C = A/B

    return C

if __name__ == '__main__':
    a = pd.Series([0,1,2,3,4,5,6,7,8,9])
    b = pd.Series([0,1,2,3,4,5,6,7,8,9])
    b2 = pd.Series([9,8,7,6,5,4,3,2,1,0])
    c = multiply_columns(a,b)
    d = divide_columns(a,b2)
    print(c)
    print(d)