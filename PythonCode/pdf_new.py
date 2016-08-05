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
    file_tup = ('1ms_272','1ms_283', '1ms_286', '1ms_291', '1ms_294', '1ms_300', '1ms_empty')
    color_tup = ('r','g','b','c','m','y','k','w')
    
    
    file_header = "C:\\Users\\yan.ren\\Desktop\\"

    for x in xrange(0, 7):
        #####for txt data
        inputFilePath = file_header + file_tup[x] + '.txt'
        
        content = [line.rstrip(' \n') for line in open(inputFilePath)]
        content = [float(i) for i in content]
        #content = [iround(i) for i in content]

        h = sorted(content)  #sorted
   
        fit = stats.norm.pdf(h, np.mean(h), np.std(h))  #this is a fitting indeed
        pl.plot(h,fit, color = 'r', linestyle= 'solid', marker='o', label = file_tup[x])
        
    pl.title("5.8GHz_81920Hz Sample Rate_1Hz Frequency")
    pl.xlabel("Power reading")
    pl.ylabel("Probability")
    pl.legend()                   #use may also need add this
    pl.show()

if __name__ == '__main__':
    main()
