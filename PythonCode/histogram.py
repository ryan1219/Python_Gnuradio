import numpy as np
import scipy.stats as stats
import pylab as pl


def iround(x):
    y = round(x) - .5
    return int(y) + (y > 0)

def main():
    inputFilePath1 = "/home/moez/Desktop/exp_7_29/5.8g_81920_1_300"
    inputFilePath2 = "/home/moez/Desktop/exp_7_29/5.8g_81920_1_air"
    inputFilePath3 = "/home/moez/Desktop/exp_7_29/5.8g_81920_1_water"
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
    file1 = open(inputFilePath1)
    content1 = np.fromfile(file1, dtype=np.float32)
    file2 = open(inputFilePath2)
    content2 = np.fromfile(file2, dtype=np.float32)
    file3 = open(inputFilePath3)
    content3 = np.fromfile(file3, dtype=np.float32)
    #####

    h1 = sorted(content1)  #sorted
    h2 = sorted(content2)
    h3 = sorted(content3)
    #print h

    fit3 = stats.norm.pdf(h3, np.mean(h3), np.std(h3))
    fit2 = stats.norm.pdf(h2, np.mean(h2), np.std(h2))
    fit1 = stats.norm.pdf(h1, np.mean(h1), np.std(h1))  #this is a fitting indeed

    pl.plot(h1,fit1, color = 'green', linestyle= 'solid', marker='o', label = "300SBF")
    pl.plot(h2, fit2, color = 'blue', linestyle= 'dashed', marker='s', label = "air")
    pl.plot(h3, fit3, color='red', linestyle='dash-dot', marker='*', label="pure water")
    ##pl.hist(h,normed=True)      #use this to draw histogram of your data
    pl.title("5.8GHz_81920Hz Sample Rate_1Hz Frequency")
    pl.xlabel("Power reading")
    pl.ylabel("Probability")
    pl.legend()                   #use may also need add this
    pl.show()

if __name__ == '__main__':
    main()