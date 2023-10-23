import numpy as np
import matplotlib.pyplot as plt
from cg_functions import coin_price
import sys

coin_id = ['tether', 'usd-coin', 'dai', 'binance-usd', 'true-usd', 'frax', 
           'usdd', 'first-digital-usd', 'gemini-dollar', 'liquity-usd']
coin_ticker = ['USDT', 'USDC', 'DAI', 'BUSD', 'TUSD', 'FRAX', 'USDD', 'FDUSD', 'GUSD', 'LUSD']

days = 1000
#days = 600
#days = 300

plt.close()  # Close current plots

P, Musdt, S, time = coin_price(coin_id[0], days)
P, Musdc, S, time = coin_price(coin_id[1], days)

yticks1 = np.arange(20, 100, 10)
yticklabels1 = ('$20B', '$30B', '$40B', '$50B', '$60B', '$70B', '$80B', '$90B')
yticks2 = np.arange(0, 80, 10)
yticklabels2 = ('0', '$10B', '$20B', '$30B', '$40B', '$50B', '$60B', '$70B')

nrows = 2; ncols = 2;
#nrows = 1; ncols = 1;
fig, ax1 = plt.subplots(nrows=nrows, ncols=ncols)

line1 = ax1[0, 0].plot(time, Musdt/1e9, color='C0')
ax1[0, 0].set_yticks(yticks1)
ax1[0, 0].set_yticklabels(yticklabels1)
ax1[0, 0].tick_params(axis='y', color='C0', labelcolor='C0')
ax1[0, 0].set_title('Tether vs. USDC Market Cap')
ax1[0, 0].grid()
for tick in ax1[0, 0].get_xticklabels():
    tick.set_rotation(45)
ax2 = ax1[0, 0].twinx()
line2 = ax2.plot(time, Musdc/1e9, color='C1')
ax2.set_yticks(yticks2)
ax2.set_yticklabels(yticklabels2)
ax2.tick_params(axis='y', color='C1', labelcolor='C1')

lines = line1 + line2
ax2.legend(lines, ['USDT','USDC'], loc=4)

sys.exit()

### Plot of Price (P), Market Cap (M), & Circulating Supply (S)
#plt.rcParams["figure.figsize"] = (13, 9)
clr = 'k'
fntsize = 11

sclfac = 1e9
ylbl = 'Billions of Dollars'
sclfac_sup = 1e9
ylbl_sup = 'Billions of Coins'
    
plt.subplot(231)
plt.plot(time, P)
plt.title('Price', fontsize=fntsize, color=clr)
plt.xticks(fontsize=8, rotation=45, color=clr)
plt.yticks(fontsize=8, color=clr)
plt.ylabel('Dollars', fontsize=fntsize, color=clr)
plt.grid(True)

plt.subplot(232)
plt.plot(time, M/sclfac)
plt.title('Market Cap', fontsize=fntsize, color=clr)
plt.xticks(fontsize=8, rotation=45, color=clr)
plt.yticks(fontsize=8, color=clr)
plt.ylabel(ylbl, fontsize=fntsize, color=clr)
#plt.ylim(-0, 25)
plt.grid(True)

stablticker = ('USDT', 'USDC', 'DAI', 'BUSD', 'TUSD', 'FRAX', 'USDD', 'FDUSD', 'GUSD', 'LUSD')
loc = 0; # Best
plt.subplot(231)
plt.legend(stablticker, loc=loc)

### Save Figure
#plt.savefig('stablecoin_price_marketcap.pdf',
#        bbox_inches='tight', 
#       )

