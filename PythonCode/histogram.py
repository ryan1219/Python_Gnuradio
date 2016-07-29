import numpy as np
import scipy.stats as stats
import pylab as pl


def iround(x):
    y = round(x) - .5
    return int(y) + (y > 0)

inputFilePath = "/home/moez/Desktop/data_7_27/1ms_empty.txt"

# set printing options, threshold: total number of array elements which trigger summarization rather than full repr (default 1000).
#np.set_printoptions(threshold="nan")
#file = open(inputFilePath, 'r')

content = []

# with open(inputFilePath, 'r') as ins:
#     for line in ins:
#         content.append(line)
content = [line.rstrip(' \n') for line in open(inputFilePath)]
content = [float(i) for i in content]
content = [iround(i) for i in content]

h = sorted(content)  #sorted
print h

fit = stats.norm.pdf(h, np.mean(h), np.std(h))  #this is a fitting indeed
pl.plot(h,fit,'-o')
pl.hist(h,normed=True)      #use this to draw histogram of your data
pl.show()                   #use may also need add this