import numpy
import scipy.io.wavfile as sci
import sys

'import functions from other files'
from changeSpeed import increaseSpeed, decreaseSpeed
from changeVolume import increase_volume, decrease_volume
'''
Main file of program. It will take in a wav file as the argument and read the samples
From there the program will augment those samples in different ways based on the users
choice and ouput back a wavfile
'''
'name output file'
output = "output.wav"

'Read in wavfile'
samples = sci.read(sys.argv[1])
sampleData = samples[1]
sampleRate = samples[0]


# 'Increase volume of wav file by multiplying the samples by a factor of 2'
# data = []
# for sample in sampleData:
#     value = sample * 4
#     data.append(value)
#
# returnData = numpy.array(data)
#
# sci.write(output, samples[0], returnData)

'we can add more functions here, we can also abstract these functions in other files as well'
# def increase_volume(samples,rate):
#     choice = int(input("Increase volume by a factor of how much?  "))
#     data = []
#     for sample in samples:
#         value = sample * choice
#         data.append(value)
#
#     returnData = numpy.array(data)
#     return returnData
#
# def decrease_volume(samples,rate):
#     choice = int(input("Decrease volume by a factor of how much?  "))
#     data = []
#     for sample in samples:
#         value = sample / choice
#         data.append(value)
#
#     returnData = numpy.array(data)
#     return returnData

while True:
    print("1. Increase volume by factor")
    print("2. Decrease volume by factor")
    print("3. Increase speed by factor")
    print("4. Decrease speed by factor")
    '''
    add more options here
    '''
    print("0. Quit")
    choice = raw_input("Choose how to alter sound file: ")
    if choice == '1':
        sampleData = increase_volume(sampleData,sampleRate)
    elif choice == '2':
        sampleData = decrease_volume(sampleData,sampleRate)
    elif choice == '3':
        sampleRate = increaseSpeed(sampleRate)
    elif choice == '4':
        sampleRate = decreaseSpeed(sampleRate)
    elif choice == '0':
        break

sci.write(output, sampleRate, sampleData)
