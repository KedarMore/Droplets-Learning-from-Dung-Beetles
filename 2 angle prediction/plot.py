from matplotlib import pyplot as plt
import numpy as np
import math
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

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
    poly = PolynomialFeatures(degree = 5)
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
    for n in range(9):
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

avgangle=[]
for i in range(37):
    addx=0
    for j in range(9):
        addx=addx+float(angle[i][j])
    avgangle.append(addx/37)

angle = angle.astype(np.float)
#plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})
#x = np.random.normal(size = 1000)

plt.hist(angle[:,1], bins=80)
plt.gca().set(title='Frequency Histogram', ylabel='Frequency')
plt.show()