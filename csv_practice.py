import pandas as pd
songs_df = pd.read_csv('top2018.csv', index_col=2)
# index_col = 1, use name as index of
print(songs_df.head())  # 5 * 16
#  head only shows the first five rows
songs_df.drop('id', axis=1, inplace=True)
print(songs_df.head())  # only 14 columns left, Why?
# to index by artists, change index_col=2
print(songs_df.loc['Ariana Grande'])
print(songs_df.columns)
#  one col called duration_ms
# change col name and all data in that col
songs_df.rename(columns={'duration_ms': 'duration_s'}, inplace=True)
# can change multiple col names through dict
print(songs_df.columns)
songs_df['duration_s'] = round(songs_df['duration_s']/1000)
print(songs_df['duration_s'])
