import numpy as np
import scipy.stats as stats
import pylab as pl
import sys

# This code is for plotting the probability density vs power, the input data file should follow the below format.
# 0.000    115.97
# 0.001    115.78
# 0.002    115.79
# 0.003    115.72
# 0.004    116.26
# 0.005    116.00
# 0.006    115.97
# 0.007    115.96
# 0.008    115.80
# 0.009    115.84

###this function is for rounding up float point number to integer
def iround(x):
    y = round(x) - .5
    return int(y) + (y > 0)

def main():

    file_tup = ('human_test_8_24',)
    color_tup = ('r','g','b','c','m','y','k','w')    
    file_header = "/home/moez/Desktop/test"
    plot_title = "5.8GHz_100kHz Sample Rate_5kHz Frequency"
    x_lable = "Power Reading"
    y_lable = "Probability"
    
    for x in xrange(0, len(file_tup)):

        time_data = []
        power_data = []
        total_data = 0

        inputFilePath = file_header + file_tup[x] + '.txt'
        print inputFilePath
        content = [line.rstrip('\n') for line in open(inputFilePath)]
        total_data = float(len(content))

        ##choose how many lines of data going to be used in plot 
        for y in xrange(0, len(content)):
            temp = content[y].split()
            time_data.append(temp[0])
            power_data.append(temp[1])
            
        power_data = [float(i) for i in power_data]

        ##release this comment if want to round to integer
        #power_data = [iround(i) for i in power_data]
        
        power_data = sorted(power_data)  #sorted

        ######
        x_axis = []
        y_axis = []

        i = 0
        while(i < len(power_data)):

            x_axis.append(power_data[i])
            y_axis.append(1)
  
            j = i + 1    
            while( j < len(power_data)):
                if power_data[i] == power_data[j]:
                    y_axis[len(y_axis)-1] = y_axis[len(y_axis)-1]+1
                else:
                    break
                j = j + 1
    
            i = j
            
        y_axis = [ k/total_data for k in y_axis]

        pl.plot(x_axis, y_axis, color = color_tup[x%len(color_tup)] , markeredgecolor = 'none', linestyle= 'solid', marker='o', label = file_tup[x])
        
    pl.title(plot_title)
    pl.xlabel(x_lable)
    pl.ylabel(y_lable)
    pl.legend()                   #use may also need add this
    pl.show()

if __name__ == '__main__':
    main()
