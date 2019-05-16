import numpy
import scipy.io.wavfile as sci
import sys
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


'Increase volume of wav file by multiplying the samples by a factor of 2'
data = []
for sample in sampleData:
    value = sample * 2
    data.append(value)

returnData = numpy.array(data)

sci.write(output, samples[0], returnData)
