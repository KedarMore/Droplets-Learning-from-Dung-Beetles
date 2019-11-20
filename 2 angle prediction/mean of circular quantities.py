import numpy as np
import math
from matplotlib import pyplot as plt
angle=[[]]
mean=[]
angle = np.loadtxt(fname='C:/Users/kedar/OneDrive - UCB-O365/Documents/Droplets/Prof. Orit/2 angle prediction/angle.txt', dtype=float)

for n in range(49):
    s=c=0
    for m in range(37):
        sin=math.sin(math.radians(angle[m][n]))
        cos = math.cos(math.radians(angle[m][n]))
        s=s+sin
        c=c+cos
    a=math.atan2(s,c)
    mean.append(math.degrees(a))
print(mean)

#new histogram
for step in range(49):
    plt.hist(angle[:, step], bins=100, range=[-180, 180])
    plt.gca().set(title='Frequency Histogram', ylabel='Frequency')
    plt.axvline(x=mean[step], color='red')
    #plt.show()
    plt.savefig('C:/Users/kedar/OneDrive - UCB-O365/Documents/Droplets/Prof. Orit/2 angle prediction/histogram for circular quantities/angle'+str(step)+'.png')
    plt.cla()
