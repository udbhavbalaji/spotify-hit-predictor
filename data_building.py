import pandas as pd


# Reading in the data from the 4 data files

raw_80s_df = pd.read_csv('data/raw/tracks_80s.csv')
raw_90s_df = pd.read_csv('data/raw/tracks_90s.csv')
raw_00s_df = pd.read_csv('data/raw/tracks_00s.csv')
raw_10s_df = pd.read_csv('data/raw/tracks_10s.csv')

# combining the data into a master dataset
combined_df = pd.concat([raw_80s_df, raw_90s_df, raw_00s_df, raw_10s_df], ignore_index=True, axis=0)

# exporting the combined dataset into a new csv file for preprocessing
combined_df.to_csv('data/built/track_data.csv', index=False)
