import numpy as np
import matplotlib.pyplot as plt
from cg_functions import coin_price
import sys

coin_id = ['sonne-finance', 'moonwell-artemis']
coin_ticker = ['SONNE', 'WELL']

days = 1000
#days = 600
#days = 300

plt.close()  # Close current plots

Psonne, Msonne, Ssonne, time_sonne = coin_price(coin_id[0], days)
Pwell, Mwell, Swell, time_well = coin_price(coin_id[1], days)

nrows = 2; ncol = 3;
fig, ax = plt.subplots(nrows, ncol)

ax1 = ax[0, 1]
yticks1 = np.arange(0, 14, 2)
yticks2 = yticks1
yticklabels1 = ('$0M', '$2M', '$4M', '$6M', '$8M', '$10M', '$12M')
yticklabels2 = yticklabels1
line1 = ax1.plot(time_sonne, Msonne/1e6, color='C1')
ax1.set_ylim(0, 12)
ax1.set_yticks(yticks1)
ax1.set_yticklabels(yticklabels1)
ax1.tick_params(axis='y', color='C1', labelcolor='C1')
ax1.set_title('Market Cap')
ax2 = ax1.twinx()
line2 = ax2.plot(time_well, Mwell/1e6, color='C0')
ax2.set_ylim(0, 12)
ax2.set_yticks(yticks2)
ax2.set_yticklabels(yticklabels2)
ax2.tick_params(axis='y', color='C0', labelcolor='C0')
ax1.tick_params(axis='x', rotation=45)
ax2.tick_params(axis='x', rotation=45)
ax1.grid(True)

ax1 = ax[0, 0]
yticks1 = np.arange(0, 0.4, 0.05)
yticks2 = np.arange(0, 0.061, 0.01)
yticklabels1 = ('$0', '$0.05', '$0.1', '$0.15', '$0.2', '$0.25', '$0.3', '$0.35')
yticklabels2 = ('$0', '$0.01', '$0.02', '$0.03', '$0.04', '$0.05', '$0.06')
line1 = ax1.plot(time_sonne, Psonne, color='C1')
ax1.set_ylim(0, 0.35)
ax1.set_yticks(yticks1)
ax1.set_yticklabels(yticklabels1)
ax1.tick_params(axis='y', color='C1', labelcolor='C1')
ax1.set_title('Price')
ax2 = ax1.twinx()
line2 = ax2.plot(time_well, Pwell, color='C0')
ax2.set_ylim(0, 0.06)
ax2.set_yticks(yticks2)
ax2.set_yticklabels(yticklabels2)
ax2.tick_params(axis='y', color='C0', labelcolor='C0')
ax1.tick_params(axis='x', rotation=45); ax1.grid(True)

ax1 = ax[0, 2]
yticks1 = np.arange(0, 70, 10)
yticks2 = np.arange(0, 1.4, 0.2)
yticklabels1 = ('0M', '10M', '20M', '30M', '40M', '50M', '60M')
yticklabels2 = ('0B', '0.2B', '0.4B', '0.6B', '0.8B', '1B', '1.2B')
line1 = ax1.plot(time_sonne, Ssonne/1e6, color='C1')
ax1.set_ylim(0, 65)
ax1.set_yticks(yticks1)
ax1.set_yticklabels(yticklabels1)
ax1.tick_params(axis='y', color='C1', labelcolor='C1')
ax1.set_title('Supply')
ax2 = ax1.twinx()
line2 = ax2.plot(time_well, Swell/1e9, color='C0')
ax2.set_ylim(0, 1.2)
ax2.set_yticks(yticks2)
ax2.set_yticklabels(yticklabels2)
ax2.tick_params(axis='y', color='C0', labelcolor='C0')
ax1.tick_params(axis='x', rotation=45)
ax2.tick_params(axis='x', rotation=45)
ax1.tick_params(axis='x', rotation=45); ax1.grid(True)

lines = line1 + line2
ax2.legend(lines, ['SONNE','WELL'])

plt.subplots_adjust(hspace=0.25, wspace=0.4)
plt.show()

### Save Figure
plt.savefig('sonne_well_price_marketcap.pdf',
        bbox_inches='tight', 
       )

