# CS510 Final Project .wav file audio modifier
Caameron Nakasone and Sunanth Sakthivel

## Instructions to run:
1. To run, type in console: python main.py (.wav file path here)
2. You will then be prompted with options on how the file can be modified. When done, type 0 and select the name of the modified file.
3. The newly modified audio file will be saved on the same working directory as this program. 

## Instructions to run tests:
1. to run simply type command: python unit_test.py
2. Note that some features take a while to complete so this may take a while. 

## What was built:
We built a console-based .wav file audio modifier that leverages simple base libraries in python in order create modified outputs. Essentially this allows .wav files to be extracted using scipy and with an interactive interface allow users to do the following: Increase the volume, decrease the volume, increase the speed, decrease the speed, convert audio to mono, low pass filtering, delay, echo, flangerish, invert, convert audio to stereo and splice silence segments. The final result is then written out as a .wav file where the changes can be observed. Lastly internal unit tests were made to test each individual functionality of the program along with testing functionalities in combination with each other to ensure everything is working as intended. Unit tests were made using the built in python library: unittest. 

## How it worked:
__General layout:__ the main file program will essentially take in a .wav file as an argument and then read samples. These samples will then be augmented/modified in some way (depending on the choices of the user) and write back the changes as a new .wav file. Moreover, we used a basic command line UI that prints all the options possible for the user to select from; a while loop will continue to prompt the user for a selection on how to modify the originally selected .wav file. Once completed, the modified .wav file was written using scipy and placed in the current working directory. 

__Function explanations:__ Below are explanations and music theory behind the functions we implemented.

__Increase/decrease volume:__ In order to change the volume we simply changed the amplitude of the signal and furthermore attenuated the sample by selecting a factor to multiply the samples with. This was done by iterating through the extracted samples and multiplying each sample element with a constant factor (whole numbers for increasing the volume and fractional numbers to decrease the volume). 

__Increase/decrease speed:__ In order to change the playback speed of the audio file we used scipy to extract both the sample data and the associated sample rate that was linked with the audio file. We then modified the sample rate by multiplying it with a constant factor (whole numbers for increasing the volume and fractional numbers to decrease the volume). By altering the sample rate we were able to control how many samples are played per second when rewriting the contents back to a .wav file. Keep in mind that as audio playback changed, the pitch also naturally changed; we are essentially making the wavelength longer when slowing down playback which will thus lower the pitch--the opposite occurs when audio is sped up (wave lengths are shrunk). 

__Converting to mono:__ This was done by checking to first see if the extracted sample data from the .wav file is multidimensional, if not then this tells us that there is a single channel and the audio is already in mono and no further conversions are needed. In the case where there are indeed more than one channel then the relative sample elements for each respective channel is averaged and written out into a single channel and written out with the same sample rate which creates a mono audio file. In other words, we are averaging the relative amplitudes that are projected in each channel into a final mono waveform which will then be written out as a mono .wav file. 

__Delay, echo, flanger:__ These three effects all revolved around delaying the samples of the wav file to different degrees to produce the desired effects. Echo and Delay were similar since they both involved appending empty samples in the beginning of the file and then copying over the original samples on top of that. The flanger implementation was based off a article cited in the code which would delay the samples by varying small increments from 1 - 20 milliseconds.

__Converting to stereo:__ This was done by checking to see if the extracted sample data from the .wav file was already in stereo (i.e the sample data is multidimensional indicating multiple channels), if not then the conversion process was continued. The conversion process was somewhat similar to converting to mono but this time the original mono signal is placed into each respective channel to create a new stereo mode. We decided to split the mono samples into chunks of 6 where each even chunk would be placed on the left channel and each odd chunk was placed on the right channel. This essentially created a stereo .wav file that oscillated sound from the left to right repeatedly.    

__Splicing silence segments:__ We took on a naive approach in attempting to splice intervals of silence. After extracting the sample data from the .wav file, we removed intervals of silence that are no more than an absolute value of 20 (we found that for most .wav samples the energy levels peak well past this number and for the most part accounted for silence really well). We also had to make sure that depending on if the audio file was stereo or mono we had to remove elements from the numpy array accordingly (remove from 1d array in case of mono and multidimensional array in case of stereo). Once these silence intervals were spliced out the final sample chunks are merged together and written out as a new modified .wav file. 

## What doesn't work
Aspects that didn't work was we weren’t able to retain original pitches of .wav files when modifying the playback speeds. In the future a true time stretching feature that changed playback speeds while retaining original pitch could have been implemented using an overlap add method to convolve signals with FFT. 

Additionally, the current iteration of splice silence function is too naive and not all encompassing to accomodate all kinds of .wav files. A better and more accurate approach would include keeping track of slice thresholds and monitoring intervals in which the energy levels peak past threshold and filter these appropriately based on the overall energy values of the original .wav file. The current implementation also doesn’t take into account .wav files that are naturally quieter than others which skews results and ends up splicing more than what was intended. The current approach also has difficulty equalizing splicing among stereo audio files with more than 2 or more channels. 

The current implementation of converting from mono to stereo audio seems somewhat gimmicky and would make more sense if that sample frequencies were analyzed more and distributed in multiple channels in a more meaningful manner that is more pleasing to the ear rather than hard coding distributions amongst the two channels. 

The other feature which didn't work was implementing the low pass filter using a moving running/average mean. As it is right now the samples that pass through it get jumbled up and produce a wav file full of static. This is probably do to the math of the moving average which is not producing the correct output. In the future we may be able to look at the math and create a better low pass filter that actually works. 

## What lessons were learned
We learned a lot about how exactly .wav files can be extracted and modified. For example, by extracting both the sample rate and sample data of the .wav file using scipy we were able to create many features by simply applying sound theory logic and modifying specific aspects of the two respective values. Moreover it was very fascinating to see how much could actually be altered by extracting this raw sample data. Another big lesson learned while doing this project was ensuring that final modifications of the original audio file were written back correctly such that sound quality is still retained; we ran into several instances where we forgot to properly concatenate samples together or left off specific chunks on accident which resulted in very distorted audio files (moreover, we learned to be very careful and meticulous when dealing with raw audio data, especially when huge changes are made). 
