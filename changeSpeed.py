
def increaseSpeed(sampleRate,choice):
    # choice = float(input("Increase speed of file by how much? "))
    newRate = sampleRate * choice
    return newRate

def decreaseSpeed(sampleRate,choice):
    # choice = float(input("Decrease speed of file by how much? "))
    newRate = sampleRate / choice
    return newRate
