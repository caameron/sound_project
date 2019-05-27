import numpy

def stereo_to_mono(sampleData):
    dimension = len(sampleData.shape)
    length = len(sampleData)
    #check to see if samples are multidimensional, if not then this means there
    #is a single channel and the audio is already in mono and doesn't need
    #to be converted to mono.
    print(dimension)
    if dimension < 2:
        return numpy.array(sampleData)

    data = []

    #to convert to mono, average the sample chunks from all the channels and append
    #to final result.
    average = 0
    for i in range (length):
        for x in range(0,dimension):
            average = average + sampleData[i][x]/dimension
        data.append(average)
        average = 0

    # final_result = numpy.array(data)
    # return final_result
    final_result = numpy.array(data, dtype='int16')
    return final_result
