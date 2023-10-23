import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from cg_functions import coin_price

print(f"Enter the Coingecko coin id:")
coin_id = input() 
coin_id = str(coin_id)

print(f"Enter the coin ticker:")
coin_ticker = input()
coin_ticker = str(coin_ticker)

print(f"Enter how many days:")
days = input()

P, M, S, time = coin_price(coin_id, days)

### Plot of Price (P), Market Cap (M), & Circulating Supply (S)
plt.rcParams["figure.figsize"] = (13, 9)
clr = 'k'
fntsize = 11

if M[-1] > 1e9:
    sclfac = 1e9
    ylbl = 'Billions of Dollars'
else:
    sclfac = 1e6
    ylbl = 'Millions of Dollars'

if S[-1] > 1e9:
    sclfac_sup = 1e9
    ylbl_sup = 'Billions of Coins'
else:
    sclfac_sup = 1e6
    ylbl_sup = 'Millions of Coins'

plt.close()  # Close current plots

plt.subplot(231)
plt.plot(time, P)
plt.title(coin_ticker + ' price', fontsize=fntsize, color=clr)
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
plt.grid(True)

plt.subplot(233)
plt.plot(time, S/sclfac_sup)
plt.title('Circulating Supply', fontsize=fntsize, color=clr)
plt.ylabel(ylbl_sup, fontsize=fntsize, color=clr)
plt.xticks(fontsize=8, rotation=45, color=clr)
plt.yticks(fontsize=8, color=clr)
plt.grid(True)


### Save Figure
plt.savefig(coin_ticker + '_price_mc_supply.pdf',
        bbox_inches='tight', 
       )

