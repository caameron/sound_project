import unittest
import os
import numpy
import scipy.io.wavfile as sci
import sys
from changeSpeed import increaseSpeed, decreaseSpeed
from changeVolume import increase_volume, decrease_volume
from filters import lowpass, delay, repeat, flanger, invert
from stereoMono import stereo_to_mono
#add more files here for other functions to test

absFilePath = os.path.abspath(__file__)                # Absolute Path of the module
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module

class Test(unittest.TestCase):
    samples = sci.read(fileDir + "/Test_Sound_Files/LRMonoPhase4.wav")
    sampleData = samples[1]
    sampleRate = samples[0]

    def test_increaseSpeed(self):
        print("\nStarting increase speed test")
        finalRate = increaseSpeed(self.sampleRate,2)
        finalData = self.sampleData
        testRate,testData = sci.read(fileDir + "/Test_Sound_Files/increasespeedtest.wav")
        self.assertEqual(testRate,finalRate)
        self.assertEqual(testData.all(),finalData.all())

    def test_decreaseSpeed(self):
        print("\nStarting decrease speed test")
        finalRate = decreaseSpeed(self.sampleRate,2)
        finalData = self.sampleData
        testRate,testData = sci.read(fileDir + "/Test_Sound_Files/decreaseSpeedTest.wav")
        self.assertEqual(testRate,finalRate)
        self.assertEqual(testData.all(),finalData.all())

    def test_increaseVolume(self):
        print("\nStarting increase volume test")
        finalData = increase_volume(self.sampleData,self.sampleRate,2)
        finalRate = self.sampleRate
        testRate,testData = sci.read(fileDir + "/Test_Sound_Files/increasevolumetest.wav")
        self.assertEqual(testRate,finalRate)
        self.assertEqual(testData.all(),finalData.all())

    def test_decreaseVolume(self):
        print("\nStarting decrease volume test")
        finalData = decrease_volume(self.sampleData,self.sampleRate,2)
        finalRate = self.sampleRate
        testRate,testData = sci.read(fileDir + "/Test_Sound_Files/decreaseVolumeTest.wav")
        self.assertEqual(testRate,finalRate)
        self.assertEqual(testData.all(),finalData.all())

    def test_stereoMono(self):
        print("\nStarting stereo to mono conversion test")
        finalData = stereo_to_mono(self.sampleData)
        finalRate = self.sampleRate
        testRate,testData = sci.read(fileDir + "/Test_Sound_Files/to_mono_test.wav")
        self.assertEqual(testRate,finalRate)
        self.assertEqual(testData.all(),finalData.all())

    def test_delay(self):
        print("Starting delay test\n")
        finalData = delay(self.sampleData,100)
        finalRate = self.sampleRate
        testRate,testData = sci.read(fileDir + "/Test_Sound_Files/delayTest.wav")
        self.assertEqual(testRate,finalRate)
        self.assertEqual(testData.all(),finalData.all())

    def test_echo(self):
        print("Starting echo test\n")
        finalData = repeat(self.sampleData)
        finalRate = self.sampleRate
        testRate,testData = sci.read(fileDir + "/Test_Sound_Files/echoTest.wav")
        self.assertEqual(testRate,finalRate)
        self.assertEqual(testData.all(),finalData.all())

    def test_flagner(self):
        print("Starting flanger test\n")
        finalData = flanger(self.sampleData)
        finalRate = self.sampleRate
        testRate,testData = sci.read(fileDir + "/Test_Sound_Files/flangerTest.wav")
        self.assertEqual(testRate,finalRate)
        self.assertEqual(testData.all(),finalData.all())

    def test_echo(self):
        print("Starting invert test\n")
        finalData = invert(self.sampleData)
        finalRate = self.sampleRate
        testRate,testData = sci.read(fileDir + "/Test_Sound_Files/invertTest.wav")
        self.assertEqual(testRate,finalRate)
        self.assertEqual(testData.all(),finalData.all())

if __name__ == '__main__':
    unittest.main()
