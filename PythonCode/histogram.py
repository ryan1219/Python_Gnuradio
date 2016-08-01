import numpy as np
import scipy.stats as stats
import pylab as pl


def iround(x):
    y = round(x) - .5
    return int(y) + (y > 0)

inputFilePath = "/home/moez/Desktop/exp_7_29/2.4g_100k_5k_300"

content = []

#####for txt data
# with open(inputFilePath, 'r') as ins:
#     for line in ins:
#         content.append(line)
# content = [line.rstrip(' \n') for line in open(inputFilePath)]
# content = [float(i) for i in content]
# content = [iround(i) for i in content]
#####

#####for binary data
file = open(inputFilePath)
content = np.fromfile(file, dtype=np.float32)
#####

h = sorted(content)  #sorted
#print h

fit = stats.norm.pdf(h, np.mean(h), np.std(h))  #this is a fitting indeed
pl.plot(h,fit,'-o')
pl.hist(h,normed=True)      #use this to draw histogram of your data
pl.show()                   #use may also need add this