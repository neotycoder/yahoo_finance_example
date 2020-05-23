#!/usr/bin/python3

# Description: This script will show various uses of the Pandas module. This version of the script organizes the functions into a class.
# Another added example is calling the various methods via an object call. 


import pandas as pd
import ssl
import yfinance as yf

class stockquery:

    def __init__(self, sym):
        self.sym = sym 

    def get_stock(self, symbol):
        
        sym = self.sym
        # This will rectify an issue with an SSL certificate request when querying the yahoo finance api.
        ssl._create_default_https_context = ssl._create_unverified_context

        # Query details for the Apple Stock
        stock = yf.Ticker(sym)
        return stock

    def build_dataframe(self, stock_obj):
        # Get history details for the Apple Stock
        hist = stock_obj.history(period="5y")


        # Assign the history details to a data frame
        history_df = pd.DataFrame(hist)

        return history_df

    def output_dataframe_to_csv(self, stock_dataframe, stock_symbol):

        filename = '{}.csv'.format(stock_symbol)
        # Let's export the data frame to a csv file:
        stock_dataframe.to_csv(filename, header=True)

    def query_print(self, stock_dataframe):
        # select a rows based on values
        print("Display Price close less than 120: ")
        less_than_120 = stock_dataframe.loc[stock_dataframe['Close'] <= 120]
        print(less_than_120)

        print("Display Price close more than 300: ")
        more_than_120 = stock_dataframe.loc[stock_dataframe['Close'] > 300.00]
        print(more_than_120)

        print("Display Price close equal to 121.69: ")
        equal_to_120 = stock_dataframe.loc[stock_dataframe['Close'] == 121.69]
        print(equal_to_120)

        print("Display Price close greater or equal to 120 and less than or equal to 130: ")
        more_than_or_equal_120_and_less_than_or_equal_to_300 = stock_dataframe.loc[(stock_dataframe['Close'] >= 120) & (stock_dataframe['Close'] <= 300.00)]
        print(more_than_or_equal_120_and_less_than_or_equal_to_300)

def main():
    # Initialize the object
    stock_symbol = "aapl"
    sq = stockquery(stock_symbol)
    
    stock_object = sq.get_stock(stock_symbol)

    # Build the data frame
    stock_dataframe = sq.build_dataframe(stock_object)

    # Perform a query on the data frame and then print it out to STDOUT
    sq.query_print(stock_dataframe)

    # Output the data frame
    sq.output_dataframe_to_csv(stock_dataframe, stock_symbol)


# Call main()
main()