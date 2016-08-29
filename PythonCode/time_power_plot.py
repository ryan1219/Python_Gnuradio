import numpy as np
import scipy.stats as stats
import pylab as pl
import sys

# This code is for plotting the time vs power, the input data file should follow the below format.
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

    #Graph label and input data, should be checked each time before running

    file_tup = ('human_test_8_24',) #file name, support multiple file for plotting multiple lines in same graph
    color_tup = ('r', 'g', 'b', 'c', 'm', 'y', 'k', 'w')
    file_header = "C:\Users\yan.ren\Desktop\human_test_8_24\\" #file path
    plot_title = "5.8GHz_100kHz Sample Rate_5kHz Frequency"
    x_lable = "Time(s)"
    y_lable = "Power Reading"

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
        time_data = [float(i) for i in time_data]

        ##release this comment if want to round to integer
        # power_data = [iround(i) for i in power_data]

        pl.plot(time_data, power_data, color=color_tup[x % len(color_tup)],markeredgecolor = 'none', linestyle='solid', marker='o', label=file_tup[x])

    pl.title(plot_title)
    pl.xlabel(x_lable)
    pl.ylabel(y_lable)
    pl.legend()  # use may also need add this
    pl.show()


if __name__ == '__main__':
    main()
