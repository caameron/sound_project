import numpy
import scipy.io.wavfile as sci
import sys
from scipy.signal import hilbert

'import functions from other files'
from changeSpeed import increaseSpeed, decreaseSpeed
from filters import lowpass, delay
from changeVolume import increase_volume, decrease_volume
from stereoMono import stereo_to_mono
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

# test = hilbert(sampleData)
# print(test)
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
    print("5. Convert audio to mono")
    print("6. low pass filter (work in progress)")
    print("7. delay")

    '''
    add more options here
    '''
    print("0. Quit")
    choice = raw_input("Choose how to alter sound file: ")
    if choice == '1':
        choice = int(input("Increase volume by a factor of how much?  "))
        sampleData = increase_volume(sampleData,sampleRate,choice)
    elif choice == '2':
        choice = int(input("Decrease volume by a factor of how much?  "))
        sampleData = decrease_volume(sampleData,sampleRate,choice)
    elif choice == '3':
        choice = float(input("Increase speed of file by how much? "))
        sampleRate = increaseSpeed(sampleRate,choice)
    elif choice == '4':
        choice = float(input("Decrease speed of file by how much? "))
        sampleRate = decreaseSpeed(sampleRate,choice)
    elif choice == '5':
        sampleData = stereo_to_mono(sampleData)
    elif choice == '6':
        sampleData = lowpass(sampleData, sampleRate)
    elif choice == '7':
        choice = int(input("delay but how many miliseconds?"))
        sampleData = delay(sampleData, choice)
    elif choice == '0':
        break

file_name = raw_input("What do you want the updated name of file to be? (dont include .wav)")
sci.write(file_name +".wav", sampleRate, sampleData)
