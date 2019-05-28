# low pass filter implementation of moving average filter
# implementation based on https://stackoverflow.com/questions/13728392/moving-average-or-running-mean,
# https://stackoverflow.com/questions/24920346/filtering-a-wav-file-using-python
import numpy

# stil needs work
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


# Plays regular sound twice, but delays one by a certain amount of miliseconds
def delay(sampleData, choice):
    returnData = []
    for int in range(choice * 20):
        zero = [0, 0]
        zero = numpy.array(zero, dtype=numpy.int16)
        returnData.append(zero)

    # copy over sample data to new array
    for sample in sampleData:
        value = numpy.array(value, dtype=numpy.int16)
        returnData.append(value)

    for index in range(len(sampleData)):
        if(index < len(sampleData)):
            returnData[index] = returnData[index] + sampleData[index]

    returnData = numpy.array(returnData)

    return returnData

def echo(sampleData):
    returnData = []
    #Add in delay
    for int in range(8000):
        zero = [0,0]
        zero = numpy.array(zero, dtype=numpy.int16)
        returnData.append(zero)

    # Add in a decay to samples
    factor = 1
    for index in range(len(sampleData)):
        if(index % 10000):
            factor = factor + 1
        value = sampleData[index] * (1 ** factor)
        value = numpy.array(value, dtype=numpy.int16)
        returnData.append(value)

    for index in range(len(sampleData)):
        if(index < len(sampleData)):
            returnData[index] = returnData[index] + (sampleData[index] / 2)


    returnData = numpy.array(returnData)

    return returnData

def flanger(sampleData):
    returnData = []
    count = 0
    increment = 1
    for index in range(len(sampleData)):
        if(count == 0):
            increment = 1
        if(count == 30):
            increment = -1

        if(index + count < len(sampleData) and index + count >= 0):
            returnData.append(sampleData[index - count] / 2)

        count = count + increment

    for index in range(len(sampleData)):
        if(index < len(sampleData) and index < len(returnData)):
            returnData[index] = returnData[index] + (sampleData[index] / 2)

    returnData = numpy.array(returnData)
    return returnData
