import numpy
#full path of the file
#outputFilePath = "/home/biomindr/Data/savedDataFromPython_Tx_A_1.txt"
#inputFilePath = "/home/biomindr/Data/Tx_A_1"

def countDataNumber(dataArray):
    return len(dataArray)

def main():
    outputFilePath = "/home/moez/Desktop/savedDataFromPython_wrist60I.txt"
    inputFilePath = "/home/moez/Desktop/Data2/wrist60I.txt"

    # set printing options, threshold: total number of array elements which trigger summarization rather than full repr (default 1000).
    numpy.set_printoptions(threshold="nan")
    file = open(inputFilePath)

    f = numpy.fromfile(file, dtype=numpy.float32)

    print "Number of data converted from raw binary file: %d" % (countDataNumber(f))

    numpy.savetxt(outputFilePath, f, delimiter=' ', newline='\n', header='', footer='', comments='# ')

if __name__ == '__main__':
    main()
