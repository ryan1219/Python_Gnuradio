import numpy as np
import scipy.stats as stats
import pylab as pl
import sys


###this function is for rounding up float point number to integer
def iround(x):
    y = round(x) - .5
    return int(y) + (y > 0)

def main():
    
    file_tup = ('serial_2',)
    color_tup = ('r', 'g', 'b', 'c', 'm', 'y', 'k', 'w')
    file_header = "C:\Users\yan.ren\Desktop\exp_8_8\\2.4G\\"
    plot_title = "2.4GHz_100kHz Sample Rate_5kHz Frequency_serial_2"
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

        for y in xrange(0, len(content)):
            temp = content[y].split()
            time_data.append(temp[0])
            power_data.append(temp[1])

        power_data = [float(i) for i in power_data]
        time_data = [float(i) for i in time_data]

        ##release this comment if want to round to integer
        # power_data = [iround(i) for i in power_data]

        pl.plot(time_data, power_data, color=color_tup[x % len(color_tup)], linestyle='solid', marker='o', label=file_tup[x])

    pl.title(plot_title)
    pl.xlabel(x_lable)
    pl.ylabel(y_lable)
    pl.legend()  # use may also need add this
    pl.show()


if __name__ == '__main__':
    main()
