# supertrend

The supertrend algorithm uses ATR (Average True Range) to calculate the direction of the trend based on a combination of historical price data and volatility.

### ATR (Average True Range)

The Average True Range is a technical indicator that measures how much an asset moves on an average. It is a lagging indicator meaning that it takes into account the historical data of an asset to measure the current value but it’s not capable of predicting the future data points. This is not considered as a drawback while using ATR as it’s one of the indicators to track the volatility of a market more accurately. Along with being a lagging indicator, ATR is also a non-directional indicator meaning that the movement of ATR is inversely proportional to the actual movement of the market. To calculate ATR, it is requisite to follow two steps:

- Calculate True Range (TR): A True Range of an asset is calculated by taking the greatest values of three price differences which are: market high minus marker low, market high minus previous market close, previous market close minus market low. It can be represented as follows:

```
MAX [ {HIGH - LOW}, {HIGH - P.CLOSE}, {P.CLOSE - LOW} ]where,
MAX = Maximum values
HIGH = Market High
LOW = Market Low
P.CLOSE = Previous market close
```

- Calculate ATR: The calculation for the Average True Range is simple. We just have to take a smoothed average of the previously calculated True Range values for a specified number of periods. The smoothed average is not just any SMA or EMA but an own type of smoothed average created by Wilder Wiles himself but there aren’t any restrictions in using other MAs too. In this article, we will be using the Exponential Moving Average (EMA) to calculate ATR rather than the custom moving average created by the founder of the indicator just to make things simple. The calculation of ATR with a traditional setting of 14 as the number of periods can be represented as follows:

```
ATR 14 = EMA 14 [ TR ]

where,
ATR 14 = 14 Period Average True Range
SMA 14 = 14 Period Simple Moving Average
TR = True Range
```

##### Medium Article

Here is an article that goes more into depth on the complex calculation of super trends:

https://medium.com/codex/step-by-step-implementation-of-the-supertrend-indicator-in-python-656aa678c111

