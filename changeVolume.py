import numpy

# Increases the volume of the audio sample given by simply multiplying each
# sample by a constant value set by the user
def increase_volume(samples,rate,choice):
    # choice = int(input("Increase volume by a factor of how much?  "))
    data = []
    for sample in samples:
        value = sample * choice
        data.append(value)

    returnData = numpy.array(data)
    return returnData

# Decreases the volume of the audio sample given by simply dividing each
# sample by a constant value set by the user
def decrease_volume(samples,rate,choice):
    # choice = int(input("Decrease volume by a factor of how much?  "))
    data = []
    for sample in samples:
        value = sample / choice
        data.append(value)

    returnData = numpy.array(data)
    return returnData
