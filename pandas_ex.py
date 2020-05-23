#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

# Description: This script will show various uses of the Pandas module.

import pandas as pd
import ssl
import yfinance as yf
print(" break point 1 You made it here!!")

# This will rectify an issue with an SSL certificate request when querying the yahoo finance api.
ssl._create_default_https_context = ssl._create_unverified_context

# Query details for the Apple Stock
aapl = yf.Ticker('AAPL')

# Get history details for the Apple Stock
hist = aapl.history(period="5y")

# You can print the details of the query and the history
#print(aapl)
#print(hist)
print("You made it here!!")
# Assign the history details to a data frame
history_df = pd.DataFrame(hist)

# You can now apply Pandas functions to the history_df data frame
print("Exploring the History Data Frame for AAPL Stock: ")
print(history_df)

# Let's export the data frame to a csv file:
history_df.to_csv('aapl.csv', header=True)

# select a rows based on values
print("Display Price close less than 120: ")
less_than_120 = history_df.loc[history_df['Close'] <= 120]
print(less_than_120)

print("Display Price close more than 300: ")
more_than_120 = history_df.loc[history_df['Close'] > 300.00]
print(more_than_120)

print("Display Price close equal to 121.69: ")
equal_to_120 = history_df.loc[history_df['Close'] == 121.69]
print(equal_to_120)

print("Display Price close greater or equal to 120 and less than or equal to 130: ")
more_than_or_equal_120_and_less_than_or_equal_to_300 = history_df.loc[(history_df['Close'] >= 120) & (history_df['Close'] <= 300.00)]
print(more_than_or_equal_120_and_less_than_or_equal_to_300)
