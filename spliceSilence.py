import numpy

def splice_silence(sampleData):

    #our naive attempt at splicing intervals of silence. more accurate version would
    #include keeping track of a silce threshold and then monitoring intervals
    #in which the energy levels peak past the threshold and filter these
    #appropriately based on the overall energy values of the original .wav file
    #this naive approach doesn't take into account .wav files that are naturally
    #quieter than others which skews results. This approach also has difficulty
    #splicing stereo audio files with more than 1 channel.
    length = len(sampleData)
    dimension = len(sampleData.shape)
    index = []
    check = False

    #remove intervals of silence that are no more than an absolute value of 20
    #check to see if stereo or mono and remove appropriately.
    if dimension == 1:
        for i in range(length):
            if abs(sampleData[i]) < 20:
                index.append(i)
    else:
        for i in range(length):
            for x in range(0,dimension):
                check = False
                if abs(sampleData[i][x]) < 20:
                    check = True
            if check == True:
                index.append(i)

    # print(sampleData)
    # print(length)
    # print(len(index))

    data = numpy.delete(sampleData, index, axis=0)
    # print(data)

    # final_result = numpy.array(data)
    # return final_result
    final_result = numpy.array(data, dtype='int16')
    return final_result
