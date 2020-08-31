import pandas as pd
import seaborn as sns
import scipy.stats as stats
import numpy as np
plt.figure(figsize=(9,3), dpi=100)
df = pd.read_csv('path to csv', delimiter=',')
bn = df['Bitnodes']
dns = df['DNS']
common = df['Common']
time = df['time']
low = []
for x in range(0,len(bn)):
    low.append(np.min(common)-100)


plt.fill_between(time, dns, bn, color="#224392", alpha=0.2)
plt.fill_between(time, common, dns, color="#6ab9cb", alpha=0.7)
plt.fill_between(time, low, common, color="#4dbcd3", alpha=0.4)

plt.plot(time,bn,linewidth=2, color='#1a237c', label='Bitnodes')
plt.plot(time,dns,linewidth=2, color='#1a237c', alpha= 0.8,linestyle='-.', label='DNS')
plt.plot(time,common,linewidth=2, color='#1a237c',alpha=0.5,linestyle=':', label='Common')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.09),
          ncol=3, fancybox=True)
plt.xlabel('Sample Time',fontsize=12)
plt.ylabel('Number of Addresses',fontsize=12)
plt.margins(0,0)
plt.savefig('path to save as pdf', transparent = True, bbox_inches = 'tight', pad_inches = 0)


