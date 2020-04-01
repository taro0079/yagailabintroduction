from matplotlib import pyplot as plt
import numpy as np 
import pandas as pd


data = pd.read_csv('14Zn1Gegsdata.csv', delimiter=',')
data2 = pd.read_csv('15Zngs.csv', delimiter=',')

ht1 = data['sample']
gs1 = data['grainsize']

ht2 = data2['HT']
gs2 = data2['gs']


fig, ax = plt.subplots(figsize=(5,8))
ax.tick_params(axis='x', labelrotation=70)
ax.set_ylabel('Average grain size (nm)')
ax.bar(ht1, gs1, label='Ge addition', width=0.5)
ax.bar(ht2, gs2, label='No Ge addition', width=0.5)
ax.legend()
plt.tight_layout()
plt.savefig('out.pdf', dpi=300, tight_layout=True)