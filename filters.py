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

    # Create empty samples equal to amount of miliseconds that will be
    # used for the initial delay
    for int in range(choice * 20):
        zero = [0, 0]
        zero = numpy.array(zero, dtype=numpy.int16)
        returnData.append(zero)

    # copy over sample data to new array
    for sample in sampleData:
        value = numpy.array(value, dtype=numpy.int16)
        returnData.append(value)

    # merge original audio
    for index in range(len(sampleData)):
        if(index < len(sampleData)):
            returnData[index] = returnData[index] + sampleData[index]

    returnData = numpy.array(returnData)

    return returnData

#similiar to delay except uses a constant delay and slowly fades the volume of
#the repeated sound
def repeat(sampleData):
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

    # copy over the original sound by merging it with the newly created sound
    # file
    for index in range(len(sampleData)):
        if(index < len(sampleData)):
            returnData[index] = returnData[index] + (sampleData[index] / 2)


    returnData = numpy.array(returnData)
    return returnData

# Our attempt at creating a flanger effect but more simplified. We based Our
# flanger effect on the description from "A Sound Project Using Python"
# https://www.ijera.com/papers/Vol4_issue5/Version%201/B45010811.pdf
# They describe it as mixing audio signals but with one being delayed by a
# small and gradually changing period. To do this we had a count which
# went between -20 and 20 by increments of 1 or -1. This acted as our delay
# so it was gradually changing throughout the process of merging the two
# audios together
def flanger(sampleData):
    returnData = []
    count = 0
    increment = 1
    for index in range(len(sampleData)):
        if(count == -20):
            increment = 1
        if(count == 20):
            increment = -1

        # use count and index to choose how much of a delay is needed
        if(index + count < len(sampleData) and index + count >= 0):
            returnData.append(sampleData[index + count] / 2)

        count = count + increment

    # Copy over original audio as well to overlap with the delayed.
    # We also had to make both audios softer so as to not amplify the
    # the sound
    for index in range(len(sampleData)):
        if(index < len(sampleData) and index < len(returnData)):
            returnData[index] = returnData[index] + (sampleData[index] / 2)

    returnData = numpy.array(returnData)
    return returnData

# Invert the audio samples by setting them in an array but reversed
def invert(sampleData):
    returnData = []
    count = len(sampleData) - 1
    for index in range(len(sampleData)):
        val = count - index
        if(index < len(sampleData) and val < len(sampleData)):
            returnData.append(sampleData[val])

    returnData = numpy.array(returnData)
    return returnData
