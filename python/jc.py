import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

gedata = pd.read_csv('/Users/moritatarou/Dropbox/01_study/02_YagaiLab/2020/intro/python/14Zn1Gejc.csv', delimiter=',')
nogedata = pd.read_csv('/Users/moritatarou/Dropbox/01_study/02_YagaiLab/2020/intro/python/15Znjc.csv', delimiter=',')

geb = gedata['B']
realdata_ge = gedata.loc[7:15, 'B':'800C50h']

nogeb = nogedata['B']
realdata_noge = nogedata.loc[7:15, 'B':'15Zn']

fig, ax = plt.subplots(figsize=(5,5), tight_layout=True)

ax.set_yscale('log')

ax.set_xlabel('magnetic field (T)')
ax.set_ylabel(r'matrix $J_\mathrm{c}$ (A/mm$^2$)')
ax.minorticks_on()
ax.xaxis.set_ticks_position('both')
ax.yaxis.set_ticks_position('both')
ax.tick_params(axis='both', which='both', direction='in')

ax.plot(geb, gedata['700C200h'], color='tab:blue', label=r'Ge addition (700$^\circ$C/200 h)')
ax.scatter(realdata_ge['B'], realdata_ge['700C200h'])
#
#ax.plot(geb, gedata['750C50h'], color='tab:orange', label=r'750$^\circ$C/50 h')
#ax.scatter(realdata_ge['B'], realdata_ge['750C50h'])
#
#ax.plot(geb, gedata['750C100h'], color='tab:green', label=r'750$^\circ$C/100 h')
#ax.scatter(realdata_ge['B'], realdata_ge['750C100h'])
#
#ax.plot(geb, gedata['750C200h'], color='tab:red', label=r'750$^\circ$C/200 h')
#ax.scatter(realdata_ge['B'], realdata_ge['750C200h'])
#
#ax.plot(geb, gedata['800C50h'], color='tab:purple', label=r'800$^\circ$C/50 h')
#ax.scatter(realdata_ge['B'], realdata_ge['800C50h'])
ax.plot(nogeb, nogedata['15Zn'], color='tab:orange', label=r'No Ge addition (700$^\circ$C/200 h')
ax.scatter(realdata_noge['B'], realdata_noge['15Zn'])

ax.legend()
#plt.show()
plt.tight_layout()
plt.savefig('kramerout.pdf', dpi=600)


