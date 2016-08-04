import numpy as np
import scipy.stats as stats
import pylab as pl


def iround(x):
    y = round(x) - .5
    return int(y) + (y > 0)

def main():
    '''    
    inputFilePath1 = "/home/moez/Desktop/exp_7_29/5.8g_81920_1_300"
    inputFilePath2 = "/home/moez/Desktop/exp_7_29/5.8g_81920_1_air"
    inputFilePath3 = "/home/moez/Desktop/exp_7_29/5.8g_81920_1_water"
    '''    
    inputFilePath1 = "C:\\Users\\yan.ren\\Desktop\\1ms_272.txt"
    inputFilePath2 = "C:\\Users\\yan.ren\\Desktop\\1ms_283.txt"
    inputFilePath3 = "C:\\Users\\yan.ren\\Desktop\\1ms_286.txt"
    inputFilePath4 = "C:\\Users\\yan.ren\\Desktop\\1ms_291.txt"
    inputFilePath5 = "C:\\Users\\yan.ren\\Desktop\\1ms_294.txt"
    inputFilePath6 = "C:\\Users\\yan.ren\\Desktop\\1ms_300.txt"
    inputFilePath7 = "C:\\Users\\yan.ren\\Desktop\\1ms_empty.txt"
    

    content1 = []
    content2 = []
    content3 = []

    #####for txt data
    content1 = [line.rstrip(' \n') for line in open(inputFilePath1)]
    content1 = [float(i) for i in content1]
    #content1 = [iround(i) for i in content1]
    
    content2 = [line.rstrip(' \n') for line in open(inputFilePath2)]
    content2 = [float(i) for i in content2]
    #content2 = [iround(i) for i in content2]

    content3 = [line.rstrip(' \n') for line in open(inputFilePath3)]
    content3 = [float(i) for i in content3]
    #content3 = [iround(i) for i in content3]

    content4 = [line.rstrip(' \n') for line in open(inputFilePath4)]
    content4 = [float(i) for i in content4]

    content5 = [line.rstrip(' \n') for line in open(inputFilePath5)]
    content5 = [float(i) for i in content5]

    content6 = [line.rstrip(' \n') for line in open(inputFilePath6)]
    content6 = [float(i) for i in content6]

    content7 = [line.rstrip(' \n') for line in open(inputFilePath7)]
    content7 = [float(i) for i in content7]
    #####
    
    '''
    #####for binary data
    file1 = open(inputFilePath1)
    content1 = np.fromfile(file1, dtype=np.float32)
    file2 = open(inputFilePath2)
    content2 = np.fromfile(file2, dtype=np.float32)
    file3 = open(inputFilePath3)
    content3 = np.fromfile(file3, dtype=np.float32)
    #####
    '''
    h1 = sorted(content1)  #sorted
    h2 = sorted(content2)
    h3 = sorted(content3)
    h4 = sorted(content4)
    h5 = sorted(content5)
    h6 = sorted(content6)
    h7 = sorted(content7)
    #print h

    fit1 = stats.norm.pdf(h1, np.mean(h1), np.std(h1))  #this is a fitting indeed
    fit2 = stats.norm.pdf(h2, np.mean(h2), np.std(h2))
    fit3 = stats.norm.pdf(h3, np.mean(h3), np.std(h3))
    fit4 = stats.norm.pdf(h4, np.mean(h4), np.std(h4))
    fit5 = stats.norm.pdf(h5, np.mean(h5), np.std(h5))
    fit6 = stats.norm.pdf(h6, np.mean(h6), np.std(h6))
    fit7 = stats.norm.pdf(h7, np.mean(h7), np.std(h7))

    pl.plot(h1,fit1, color = 'green', linestyle= 'solid', marker='o', label = "272")
    pl.plot(h2, fit2, color = 'blue', linestyle= 'dashed', marker='s', label = "283")
    pl.plot(h3, fit3, color='red', linestyle='dashed', marker='*', label="286")
    pl.plot(h4, fit4, color='cyan', linestyle='dashed', marker='*', label="291")
    pl.plot(h5, fit5, color='magenta', linestyle='dashed', marker='*', label="294")
    pl.plot(h6, fit6, color='yellow', linestyle='dashed', marker='*', label="300")
    #pl.plot(h7, fit7, color='black', linestyle='dashed', marker='*', label="empty")
    ##pl.hist(h,normed=True)      #use this to draw histogram of your data
    pl.title("5.8GHz_81920Hz Sample Rate_1Hz Frequency")
    pl.xlabel("Power reading")
    pl.ylabel("Probability")
    pl.legend()                   #use may also need add this
    pl.show()

if __name__ == '__main__':
    main()
