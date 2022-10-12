#Import Dependencies
import pandas as pd
import pandas_ta as ta
import alpaca_trade_api as tradeapi

API_KEY=''
SECRET_KEY=''
api = tradeapi.REST(API_KEY, SECRET_KEY,'https://paper-api.alpaca.markets')

# Define crypto related variables
symbol = 'BTCUSD'
qty_per_trade = 1

# Check Whether Account Currently Holds Symbol
def check_positions(symbol):
    positions = api.list_positions()
    for p in positions:
        if p.symbol == symbol:
            return float(p.qty)
    return 0

# Supertrend Indicator Bot Function
def supertrend_bot(bar):
    try:
        # Get the Latest Data
        dataframe = api.get_crypto_bars(symbol, tradeapi.TimeFrame(1, tradeapi.TimeFrameUnit.Minute)).df
        dataframe = dataframe[dataframe.exchange == 'CBSE']
        sti = ta.supertrend(dataframe['high'], dataframe['low'], dataframe['close'], 7, 3)
        dataframe = pd.concat([dataframe, sti], axis=1)

        position = check_positions(symbol=symbol)
        should_buy = bar['c'] > dataframe["SUPERT_7_3.0"][-1]
        should_sell = bar['c'] < dataframe["SUPERT_7_3.0"][-1]
        print(f"Price: {bar['c']}")
        print("Super Trend Indicator: {}".format(dataframe["SUPERT_7_3.0"][-1]))
        print(f"Position: {position} | Should Buy: {should_buy}")

        # Check if No Position and Buy Signal is True
        if position == 0 and should_buy == True:
            api.submit_order(symbol, qty=qty_per_trade, side='buy', time_in_force='gtc')
            message = f'Symbol: {symbol} | Side: Buy | Quantity: {qty_per_trade}'
            print(message)

        # Check if Long Position and Sell Signal is True
        elif position > 0 and should_sell == True:
            api.submit_order(symbol, qty=qty_per_trade, side='sell', time_in_force='gtc')
            message = f'Symbol: {symbol} | Side: Sell | Quantity: {qty_per_trade}'
            print(message)
        print("-"*20)

    except Exception as e:
        print (e)

# Create handler for receiving live bar data
async def on_crypto_bar(bar):
    print(bar)
    supertrend_bot(bar)

# Create instance of Alpaca data streaming API
print(12)
alpaca_stream = tradeapi.Stream(API_KEY, SECRET_KEY, raw_data=True, crypto_exchanges=['CBSE'])


# Subscribe to data and assign handler
alpaca_stream.subscribe_crypto_bars(on_crypto_bar, symbol)

# Start streaming of data
alpaca_stream.run()
