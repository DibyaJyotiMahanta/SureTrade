#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt


# # SMA - Simple Moving Average

# In[ ]:


def calculate_sma(source, length): 
    sma_values = [] # Initializes an empty list

    for i in range(len(source)): # iterates through the indices of the source list
        if i < length - 1: # current index i is less than length - 1 
            sma_values.append(None)  # Appends None to the sma_values 
        else:
            sma = sum(source[i - length + 1:i + 1]) / length # extract values through slice operationand divide
            sma_values.append(sma) # append sma to sma_values

    return sma_values 


# In[ ]:


# source = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
# sma_length = 3

# sma_result = calculate_sma(source, sma_length)
# print(sma_result)


# In[ ]:


# plt.plot(sma_result);


# # RMA - RSI Moving Average (relative strength index)

# In[ ]:


def calculate_rma(source, length):
    alpha = 1 / length # formula for alpha ( smoothing factor)
    rma_values = [] # Initializes an empty list

    for i in range(len(source)): # Iterates through each element
        if i == 0: # Checks if it's the first element in the loop (index 0).
            rma = source[i]  # rma is set equal to the value of the first element in the source list.
        else:
            rma = (1 - alpha) * source[i] + alpha * rma_values[i - 1] # formula to calculate rma

        rma_values.append(rma) # append rma to rma_values

    return rma_values


# In[ ]:


# def calculate_rma(source, length):
  
#     if not isinstance(length, int) or length <= 0:
#         raise ValueError("Length must be a positive integer.")

#     if not source:
#         return []

#     alpha = 1 / length  # Formula for alpha (smoothing factor)
#     rma_values = [None] * length  # Initialize with None values

#     for i in range(length, len(source)):
#         if source[i] is None or rma_values[i - 1] is None:  # Handle None values
#             rma_values.append(None)
#         else:
#             rma_values.append((1 - alpha) * source[i] + alpha * rma_values[i - 1])

#     # Fill in the first few values after the loop
#     for i in range(1, length):
#         rma_values[i] = (1 - alpha) * source[i] + alpha * rma_values[i - 1]

#     rma_values[0] = source[0]  # Update the first value

#     return rma_values


# In[ ]:


# source_data = [10, 12, 15, 18, 22, 20, 17, 14, 12, 10]
# # rma_length = 3

# rma_result = calculate_rma(source_data, rma_length)
# print(rma_result)


# In[ ]:


# plt.plot(rma_result);


# # EMA - Exponential Moving Average 

# In[ ]:


def calculate_ema(source, length):
    alpha = 2 / (length + 1) # formula for alpha (smoothing factor)
    ema_values = [] # Initializes an empty list

    for i in range(len(source)): # Iterates through each element
        if i == 0: # # Checks if it's the first element in the loop (index 0).
            ema = source[i] # ema is set equal to the value of the first element in the source list.
        else:
            ema = alpha * source[i] + (1 - alpha) * ema_values[i - 1] # # formula to calculate ema

        ema_values.append(ema) # append ema to ema_values

    return ema_values


# In[ ]:


# source_data = [10, 12, 15, 18, 22, 20, 17, 14, 12, 10]
# ema_length = 3

# ema_result = calculate_ema(source_data, ema_length)
# print(ema_result)


# In[ ]:


# plt.plot(ema_result);


# # RSI - Relative Strength Index

# In[ ]:


def calculate_rsi(source, length):
     # Step 1: Calculate upward and downward changes
    upward_changes = [max(0, source[i] - source[i - 1]) if i > 0 else 0 for i in range(len(source))]
    downward_changes = [max(0, source[i - 1] - source[i]) if i > 0 else 0 for i in range(len(source))]
    # Step 2: Calculate Exponential Moving Averages (EMAs) for upward and downward changes
    upward_ema = calculate_rma(upward_changes, length)
    downward_ema = calculate_rma(downward_changes, length)
    # Step 3: Calculate Relative Strength (RS)
    rs = [upward_ema[i] / downward_ema[i] if downward_ema[i] != 0 else 0 for i in range(len(upward_ema))]
    # Step 4: Calculate Relative Strength Index (RSI)
    rsi_values = [100 - (100 / (1 + rs_value)) if rs_value != 0 else 0 for rs_value in rs]
    # Step 5: Return the calculated RSI values
    return rsi_values


# In[ ]:


# source = [10, 12, 15, 18, 22, 20, 17, 14, 12, 10]
# rsi_length = 3

# rsi_result = calculate_rsi(source, rsi_length)
# print(rsi_result)


# In[ ]:


# plt.plot(rsi_result);


# # MFI - Money Flow Index

# In[ ]:


def calculate_mfi(highs, lows, closes, volumes, length):
    typical_prices = [(high + low + close) / 3 for high, low, close in zip(highs, lows, closes)]
    raw_money_flow = [tp * volume for tp, volume in zip(typical_prices, volumes)]

    # positive_money_flow = [rmf if close > closes[i - 1] else 0 for i, (rmf, close) in enumerate(zip(raw_money_flow, closes))]
    positive_money_flow = [rmf if i > 0 and close > closes[i - 1] else 0 for i, (rmf, close) in enumerate(zip(raw_money_flow, closes))]

    # negative_money_flow = [rmf if close < closes[i - 1] else 0 for i, (rmf, close) in enumerate(zip(raw_money_flow, closes))]
    negative_money_flow = [rmf if i > 0 and close < closes[i - 1] else 0 for i, (rmf, close) in enumerate(zip(raw_money_flow, closes))]


    mfr_values = []
    for i in range(length, len(typical_prices)):
        sum_pmf = sum(positive_money_flow[i - length + 1 : i + 1])
        sum_nmf = sum(negative_money_flow[i - length + 1 : i + 1])

        if sum_nmf == 0:
            mfr = 100  
        else:
            mfr = sum_pmf / sum_nmf

        mfr_values.append(mfr)

    mfi_values = [100 - (100 / (1 + mfr)) for mfr in mfr_values]

    return [None] * (length - 1) + mfi_values





# In[ ]:


# highs = [50, 55, 60, 58, 62, 65, 70, 68, 72, 75, 80, 78, 82]
# lows = [45, 50, 55, 52, 57, 60, 62, 58, 65, 70, 75, 72, 78]
# closes = [48, 53, 58, 56, 60, 63, 68, 66, 70, 73, 78, 76, 80]
# volumes = [100000, 120000, 150000, 110000, 130000, 140000, 160000, 180000, 200000, 190000, 220000, 210000, 230000]
# mfi_length = 7

# mfi_result = calculate_mfi(highs, lows, closes, volumes, mfi_length)
# print(mfi_result)


# In[ ]:


# plt.plot(mfi_result);


# # HMA - Hull Moving Average

# In[ ]:


import numpy as np

def calculate_wma(source, length):
    if length == 1:
        return np.array(source)
    weights = np.arange(1, length + 1)
    wma = np.convolve(source, weights, mode='valid') / weights.sum()
    return wma

def calculate_hma(source, length):
    half_length = int(length / 2)
    sqrt_length = int(np.sqrt(length))

    wma1 = calculate_wma(source, half_length)
    wma2 = calculate_wma(wma1, sqrt_length)
    wma3 = calculate_wma(source, length)

    min_len = min(len(wma1), len(wma2), len(wma3))

    hma = 2 * wma3[:min_len] - wma2[:min_len]

    return hma


# In[ ]:


# source = [10, 12, 15, 18, 22, 20, 17, 14, 12, 10]
# hma_length = 9

# hma_result = calculate_hma(source, hma_length)
# print(hma_result)


# In[ ]:


# plt.plot(hma_result);


# # VWAP - Volume Weighted Average Price

# In[ ]:


import numpy as np

def calculate_vwap(source, volumes):
    source = np.array(source)
    volumes = np.array(volumes)

    cumulative_price_volume = np.cumsum(source * volumes)
    cumulative_volume = np.cumsum(volumes)

    vwap = cumulative_price_volume / cumulative_volume

    return vwap


# In[ ]:


# closing_prices = [50, 55, 60, 58, 62]
# trading_volumes = [100000, 120000, 150000, 110000, 130000]

# vwap_result = calculate_vwap(closing_prices, trading_volumes)
# print(vwap_result[-1]) 

