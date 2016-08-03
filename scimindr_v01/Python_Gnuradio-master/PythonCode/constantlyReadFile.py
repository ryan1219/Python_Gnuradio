import numpy
import sys
import Queue
import time
import struct
import math
#full path of the file
#outputFilePath = "/home/biomindr/Data/savedDataFromPython_Tx_A_1.txt"
#inputFilePath = "/home/biomindr/Data/Tx_A_1"
outputFilePath = "/home/moez/Desktop/data_7_15/wRx_A_1.txt"
inputFilePath = "/home/moez/Desktop/data_7_15/wRx_A_1"

def countDataNumber(dataArray):
    return len(dataArray)

def read(thefile):
    #define file pointer when operating over an open file
    # fp.seek(offset, from_what)
    thefile.seek(0,2)

    while True:
        # If the file_generator hits EOF before obtaining size bytes, then it reads only available bytes.
        line = thefile.read(4)
        if not line:
            #time.sleep(0.1)
            continue
        yield line

def averageCal(fileGenerator):
    # 2^15 is fine
    #QUEUE_SIZE = int (math.pow(2,16))
    QUEUE_SIZE = 10
    #REFRESH_SAMPLE = 100

    sum = 0.0
    sampleCount = 0

    for data in fileGenerator:
        data_float = struct.unpack('f', data)

        #print data_float[0]

        if sampleCount  < QUEUE_SIZE:
            sampleCount = sampleCount + 1
            sum = sum + data_float[0]
        else:
            print "The average of %i sampels is %f mW" % (QUEUE_SIZE, sum/QUEUE_SIZE)
            sum = 0.0
            sampleCount = 0

        # if q.full == False:
        #     q.put(data_float)
        # else:
        #     sum = 0
        #     for i in range(0, QUEUE_SIZE-1, 1):
        #         sum = sum + q.get()
        #     print "average of %i sample is %f" % (QUEUE_SIZE, sum / QUEUE_SIZE)

def main():
    # set printing options, threshold: total number of array elements which trigger summarization rather than full repr (default 1000).
    numpy.set_printoptions(threshold="nan")
    # open file
    logfile = open(inputFilePath, "r")

    fileGenerator = read(logfile)

    averageCal(fileGenerator)

    # for data in fileGenerator:
    #      print(struct.unpack('f', data))
    #
    #print "Number of data converted from raw binary file: %d" % (countDataNumber(f))

    numpy.savetxt(outputFilePath, logfile, delimiter=' ', newline='\n', header='', footer='', comments='# ')

if __name__ == '__main__':
    main()
