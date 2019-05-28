
# Changes the speed of the sample audio given by altering the sampleRate of the
# original audio file. Multiplying or dividing it by a constant set by the user
# will increase or decrease the speed respectively
def increaseSpeed(sampleRate,choice):
    # choice = float(input("Increase speed of file by how much? "))
    newRate = sampleRate * choice
    return newRate

def decreaseSpeed(sampleRate,choice):
    # choice = float(input("Decrease speed of file by how much? "))
    newRate = sampleRate / choice
    return newRate
