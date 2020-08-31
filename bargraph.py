import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import pandas as pd



patterns = [ "\\" , "x", "o", ".", "-" ]

#
def pow():
    x1 = [25,50,100,150,200,250]
    data = pd.read_csv('/home/saad/Desktop/bitcoinmap/plots/POW.csv',delimiter=',')
    y1 = list(data.avg1)
    y1e = list(data.sd1)
    y2 = list(data.avg2)
    y2e = list(data.sd2)
    y3 = list(data.avg3)
    y3e = list(data.sd3)
    y4 = list(data.avg4)
    y4e = list(data.sd4)
    y5 = list(data.avg5)
    y5e = list(data.sd4)
    # create plot
    n_groups = 6
    fig = plt.figure(figsize=(6, 4))
    fig.tight_layout()
    index = np.arange(n_groups)
    bar_width = 0.24
    opacity = 0.8
    rects1 = plt.bar(index, y1, bar_width,  capsize=3, align='center' ,color='#808080',label='500 KB',hatch=patterns[0], edgecolor = 'black' )
    rects2 = plt.bar(index + 0.5*bar_width, y2, bar_width, capsize=3, align='center' ,color='#00FFFF',label='1000 Bytes',hatch=patterns[1], edgecolor = 'black' )
    rects3 = plt.bar(index + bar_width, y3, bar_width, capsize=3, align='center' ,color='#00FA9A',label='2000 Bytes',hatch=patterns[2], edgecolor = 'black' )
    rects4 = plt.bar(index + 1.5*bar_width, y4, bar_width, capsize=3, align='center' ,color='#FF0000',label='4000 Bytes',hatch=patterns[3], edgecolor = 'black' )
    rects5 = plt.bar(index + 2*bar_width, y5, bar_width,  capsize=3, align='center' ,color='#FFA07A',label='10000 Bytes',hatch=patterns[4], edgecolor = 'black' )
    plt.xlabel('Number of Nodes',fontsize=16)
    plt.ylabel('Latency (ms)',fontsize=16)
    plt.title('Proof of Work',fontsize=16)
    plt.xticks(index + bar_width, ('25','50','100','150','200','250'), fontsize=14)
    plt.yticks(fontsize=14)
    plt.legend()
    plt.tight_layout()
    fig.savefig("/home/saad/Desktop/bitcoinmap/plots/pow.pdf", bbox_inches='tight')

pow()
