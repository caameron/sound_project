# low pass filter implementation of moving average filter
# implementation based on https://stackoverflow.com/questions/13728392/moving-average-or-running-mean,
# https://stackoverflow.com/questions/24920346/filtering-a-wav-file-using-python
import numpy


def lowpass(sampleData, sampleRate):
    #calculate constants
    #window LENGTH with cutoff frequency of 500
    ratio = 500.0 / float(sampleRate)
    windowLength = int(numpy.sqrt(0.19 + ratio**2)/ ratio)

    # calculate the moving average of the sampledata which will act as a low pass filters
    arr = numpy.insert(sampleData, 0 , 0)
    cumulative = numpy.cumsum(arr)
    mean = (cumulative[windowLength:] - cumulative[:-windowLength]) / float(windowLength)
    mean = numpy.reshape(mean, (-1, 2))
    return mean


def delay(sampleData):
    returnData = []
    for sample in sampleData:
        returnData.append(sample)
        returnData.append(sample)
        # zero = [0, 0]
        # zero = numpy.array(zero, dtype=numpy.int16)
        # returnData.append(zero)
# def decrease_volume(samples,rate):
#     choice = int(input("Decrease volume by a factor of how much?  "))
#     data = []
#     for sample in samples:
#         value = sample / choice
#         data.append(value)
#
#     returnData = numpy.array(data)
#     return returnData
    returnData = numpy.array(returnData)
    # print(returnData)
    print(len(returnData))
    return returnData
