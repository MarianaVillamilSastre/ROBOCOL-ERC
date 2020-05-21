import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


TeoricValues=np.genfromtxt('teorico.txt',delimiter=',')
RGB= plt.imread('prueba2.jpeg')



redChannel = RGB[:, :, 0]
greenChannel = RGB[:, :, 1]
blueChannel = RGB[:, :, 2]

medianredChannel=np.median(redChannel)
mediangreenChannel=np.median(greenChannel)
medianblueChannel=np.median(blueChannel)

meanredChannel=np.mean(medianredChannel)
meangreenChannel=np.mean(mediangreenChannel)
meanblueChannel=np.mean(medianblueChannel)

stdredChannel=np.std(medianredChannel)
stdgreenChannel=np.std(mediangreenChannel)
stdblueChannel=np.std(medianblueChannel)

red=TeoricValues[:,0]
stdred=TeoricValues[:,1]
green=TeoricValues[:,2]
stdgreen=TeoricValues[:,3]
blue=TeoricValues[:,4]
stdblue=TeoricValues[:,5]


chi=[];

for i in range(1,9):
    	desv= np.sqrt(((red[i] - meanredChannel)**2.0 + (stdred[i] - stdredChannel)**2.0 + 
        (green[i] - meangreenChannel)**2.0 + (stdgreen[i] - stdgreenChannel)**2.0 + 
        (blue[i] - meanblueChannel)**2.0 + (stdblue[i] - stdblueChannel)**2.0)/6.0)
    	chi=np.append(chi,desv)
	minimo=np.min(chi)
	[x]= np.where(chi==minimo)
	minimo2=[x]
if minimo2==[1]:
	print('Sample classification: A1')
	print('Very low oxidation level')
elif minimo2==[2]:
	print('Sample classification: A2')
	print('Moderately low oxidation level ')
elif minimo2==[3]:
        print('Sample classification: A3')
        print('Medium-low oxidation level ')
elif minimo2==[4]:
        print('Sample classification: B1')
        print('Medium oxidation level ')
elif minimo2==[5]:
        print('Sample classification: B2')
        print('Intermediate oxidation level ')
elif minimo2==[6]:
        print('Sample classification: B3')
        print('Medium-high oxidation level ')
elif minimo2==[7]:
        print('Sample classification: C1')
        print('High oxidation ')
elif minimo2==[8]:
        print('Sample classification: C2')
        print('Moderately high oxidation ')
elif minimo2==[9]:
        print('Sample classification: C3')
        print('Very high oxidation level')	
   	
    







