# Dependencies and Setup
import pandas as pd
import numpy as np

# Raw data file
game_csv = 'purchase_data.csv'

# Read purchasing file and store into pandas data frame
game_df = pd.read_csv(game_csv)


player_df = game_df['SN'].nunique()


Player_Count = pd.DataFrame({"Total Players": [player_df]})
print(Player_Count)

unique_items = game_df['Item ID'].nunique()
avg_price = game_df['Price'].mean()
num_purchases = game_df['Purchase ID'].count()
total_revenue = game_df['Price'].sum()
Summary_df = pd.DataFrame({"Number of Unique Items": [unique_items], "Average Price": [avg_price], "Number of Purchases": [num_purchases], "Total Revenue": [total_revenue]})
print(Summary_df)
