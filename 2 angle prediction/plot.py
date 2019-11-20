from matplotlib import pyplot as plt
import numpy as np
import math
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.mlab as mlab
from scipy.stats import norm

arr=np.loadtxt(fname='C:/Users/kedar/OneDrive - UCB-O365/Documents/Droplets/Prof. Orit/2 angle prediction/test.txt',dtype=float)

arr=np.transpose(arr)

angle=[[]]
row=[]

for i in range(37):
    x=arr[:,(2*i):(2*i+1)]
    y=arr[:,(2*i+1)]
    #
    lin = LinearRegression()
    lin.fit(x, y)
    poly = PolynomialFeatures(degree = 2)
    x_poly = poly.fit_transform(x)
    poly.fit(x_poly, y)
    lin2 = LinearRegression()
    lin2.fit(x_poly, y)
    plt.plot(x, lin2.predict(poly.fit_transform(x)))
    #plt.plot(x,y)

plt.show()
################################angle

arr=np.transpose(arr)

for m in range(37):
    for n in range(49):
        if ((arr[2*m][n+1])-(arr[2*m][n]))==0:
            a=90
        else:
            #tan=(int(arr[2*m+1][n+1])-int(arr[2*m+1][n]))/(int(arr[2*m][n+1])-int(arr[2*m][n]))
            a=180*(math.atan2(((arr[2*m+1][n+1])-(arr[2*m+1][n])),((arr[2*m][n+1])-(arr[2*m][n]))))/math.pi
        row.append("%.2f" % a)
    if m==0:
        angle=np.append(angle,[row],axis=1)
    else:
        angle=np.append(angle,[row],axis=0)
    row=[]

print('angle=', angle)
np.savetxt('C:/Users/kedar/OneDrive - UCB-O365/Documents/Droplets/Prof. Orit/2 angle prediction/angle.txt',angle,fmt='%s',delimiter=' ')

angle = angle.astype(np.float)
#plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})
#x = np.random.normal(size = 1000)

for step in range(49):

    mean=np.mean(angle[:,step])
    std=np.std(angle[:,step])
    plt.hist(angle[:,step], bins=100, range=[-180,180])
    bins=100
    plt.gca().set(title='Frequency Histogram', ylabel='Frequency')
    plt.axvline(x=mean, color='red')
    plt.axvline(x=(mean+std), color='green')
    plt.axvline(x=(mean-std), color='green')
    '''
    (mu, sigma) = norm.fit(angle[:, step])
    n, bins, patches = plt.hist(
        angle[:, step], 60, density=100, facecolor='blue', alpha=0.5)
    plt.axvline(x=mu, color='red')
    plt.axvline(x=(mu+sigma), color='green')
    plt.axvline(x=(mu-sigma), color='green')
    y = norm.pdf(bins, mu, sigma)
    l = plt.plot(bins, y, 'y--', linewidth=1)
    '''
    #plt.show()
    plt.savefig('C:/Users/kedar/OneDrive - UCB-O365/Documents/Droplets/Prof. Orit/2 angle prediction/histogram/angle'+str(step)+'.png')
    plt.cla()
