import unittest
import os
import numpy
import scipy.io.wavfile as sci
import sys
from changeSpeed import increaseSpeed, decreaseSpeed
from changeVolume import increase_volume, decrease_volume
from stereoMono import stereo_to_mono
#add more files here for other functions to test

absFilePath = os.path.abspath(__file__)                # Absolute Path of the module
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module

class Test(unittest.TestCase):
    samples = sci.read(fileDir + "/Test_Sound_Files/LRMonoPhase4.wav")
    sampleData = samples[1]
    sampleRate = samples[0]

    def test_increaseSpeed(self):
        print("Starting change speed test\n")
        finalRate = increaseSpeed(self.sampleRate,2)
        finalData = self.sampleData
        testRate,testData = sci.read(fileDir + "/Test_Sound_Files/increasespeedtest.wav")
        self.assertEqual(testRate,finalRate)
        self.assertEqual(testData.all(),finalData.all())

    def test_increaseVolume(self):
        print("Starting increase volume test\n")
        finalData = increase_volume(self.sampleData,self.sampleRate,2)
        finalRate = self.sampleRate
        testRate,testData = sci.read(fileDir + "/Test_Sound_Files/increasevolumetest.wav")
        self.assertEqual(testRate,finalRate)
        self.assertEqual(testData.all(),finalData.all())

    def test_stereoMono(self):
        print("Starting stereo to mono conversion test\n")
        finalData = stereo_to_mono(self.sampleData)
        finalRate = self.sampleRate
        testRate,testData = sci.read(fileDir + "/Test_Sound_Files/to_mono_test.wav")
        self.assertEqual(testRate,finalRate)
        self.assertEqual(testData.all(),finalData.all())

if __name__ == '__main__':
    unittest.main()
