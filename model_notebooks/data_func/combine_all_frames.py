import pandas as pd

def combine_all_frames(frames: [pd.DataFrame]):
    
    for i, frame in enumerate(frames):
        if i == 0:
            frame['location'] = '0'
        elif i == 1:
            frame['location'] = '1'
        elif i == 2:
            frame['location'] = '2'
    combined = pd.concat(frames)
    combined['location'] = combined['location'].astype('float64')

    return combined


if __name__ == '__main__':
  list = [pd.DataFrame({'locA': [1,2,3,4,5,6,7,8,9,10]}), pd.DataFrame({'locB': [1,2,3,4,5,6,7,8,9,10]}), pd.DataFrame({'locC': [1,2,3,4,5,6,7,8,9,10]})]
  df = combine_all_frames(list)
  print(df['location'].dtype)
  print(df)

