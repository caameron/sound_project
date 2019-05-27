import numpy
def increase_volume(samples,rate,choice):
    # choice = int(input("Increase volume by a factor of how much?  "))
    data = []
    for sample in samples:
        value = sample * choice
        data.append(value)

    returnData = numpy.array(data)
    return returnData

def decrease_volume(samples,rate,choice):
    # choice = int(input("Decrease volume by a factor of how much?  "))
    data = []
    for sample in samples:
        value = sample / choice
        data.append(value)

    returnData = numpy.array(data)
    return returnData
