import numpy

#turn off the first channel of chunk of samples
def even_off(array):
    for i in array:
        i[0]=0

#turn off the second channel of chunk of samples
def odd_off(array):
    for i in array:
        i[1]=0

def mono_to_stereo(sampleData):
    dimension = len(sampleData.shape)
    length = len(sampleData)
    #check to see if samples are multidimensional, if it is then audio is already
    #in stereo and a mono .wav is needed with single channel.
    print("Converting to Stereo please wait...")
    if dimension > 1:
        print("already in stereo")
        return numpy.array(sampleData)

    #create two channels and turn off respective channels on a 6 range split.
    dupe = sampleData
    two_channel = numpy.column_stack((sampleData, dupe))

    one,two,three,four,five,six = numpy.array_split(two_channel,6)

    #calling functions to turn off respective channels
    even_off(two)
    even_off(four)
    even_off(six)
    odd_off(one)
    odd_off(three)
    odd_off(five)

    #concatenate final result
    first = numpy.concatenate((one,two))
    second = numpy.concatenate((first,three))
    third = numpy.concatenate((second,four))
    fourth = numpy.concatenate((third,five))
    fifth = numpy.concatenate((fourth,six))
    data = fifth
    # print(data)

    # final_result = numpy.array(data)
    # return final_result
    final_result = numpy.array(data, dtype='int16')
    return final_result
