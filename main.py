# Sunanth Sakthivel and Caameron Nakasone
# CS 510 Sound Class Project
# Wave file Alterer

import numpy
import scipy.io.wavfile as sci
import sys
from scipy.signal import hilbert

'import functions from other files'
from changeSpeed import increaseSpeed, decreaseSpeed
from filters import lowpass, delay, repeat, flanger, invert
from changeVolume import increase_volume, decrease_volume
from stereoMono import stereo_to_mono
from monoStereo import mono_to_stereo
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


# Our basic UI for the project. It is a simple command line UI that will
# print out all the options that user can make to alter their wav file.
# The user has to give the wav file as an argument when starting the program
# There is then a while loop that will keep asking the user to alter their
# file until they are satisfies. Once done it will ask for a name for their
# new file and place it in the current directory
while True:
    print("1. Increase volume by factor")
    print("2. Decrease volume by factor")
    print("3. Increase speed by factor")
    print("4. Decrease speed by factor")
    print("5. Convert audio to mono")
    print("6. low pass filter (work in progress)")
    print("7. delay")
    print("8. echo")
    print("9. flangerish")
    print("10. invert")
    print('11. Convert audio to stereo')

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
    elif choice == '8':
        sampleData = repeat(sampleData)
    elif choice == '9':
        sampleData = flanger(sampleData)
    elif choice == '10':
        sampleData = invert(sampleData)
    elif choice == '11':
        sampleData = mono_to_stereo(sampleData)
    elif choice == '0':
        break

file_name = raw_input("What do you want the updated name of file to be? (dont include .wav)")
sci.write(file_name +".wav", sampleRate, sampleData)
