import pandas as pd
import re
import scipy.stats as stats
from scipy.io import wavfile
import numpy as np
import os

<<<<<<< HEAD

os.chdir('Data')

raw_folder = 'raw_data/'
samples = [d for d in os.listdir(raw_folder) if os.path.isdir(os.path.join(raw_folder, d))]
n_samples = len(samples)

def get_gender(readme_file):
    gender = "Unknow"
    for line in open(readme_file):
        if line.startswith("Gender:"):
            gender = line.split(':')[1].strip()
            return gender

def add_lable(gender):
    if re.search('[Ff]emale', gender): 
        gender = 'Female'
    elif re.search('[Mm]ale', gender): 
        gender = 'Male'
    else: 
        gender = 'Unknow'
    return gender

def get_freq(sample_folder):
    frequencies_folder = []
    for wav_file in os.listdir(sample_folder):
        rate, data = wavfile.read(os.path.join(sample_folder, wav_file))
        step = int(rate/5)
        frequencies_file = []
        for i in range(0,len(data), step):
            ft = np.fft.fft(data[i:i+step])
            freqs = np.fft.fftfreq(len(ft))
            imax = np.argmax(np.abs(ft))
            freq = freqs[imax]
            freq_in_hz = abs(freq * rate)
            frequencies_file.append(freq_in_hz)
        
            filtered_frequencies = [f for f in frequencies_file if (20 < f < 300) and not(46 < f < 66)]
        frequencies_folder.append(filtered_frequencies)
    frequencies = [item for sublist in frequencies_folder for item in sublist]
    return frequencies

def get_features(freq):
    nobs, mimax, mean, variance, skewness, kurtosis = stats.describe(freq)
    median = np.median(freq)
    mode = stats.mode(freq).mode[0]
    std = np.std(freq)
    low, peak = mimax
    q75, q25 = np.percentile(freq,[75,25])
    iqr = q75 - q25
    return nobs, mean, skewness, kurtosis, median, mode, std, low, peak, q25, q75, iqr

columns=['nobs', 'mean', 'skewness', 'kurtosis', 'median', 'mode', 'std', 'low', 'peak', 'q25', 'q75', 'iqr', 'lable']
myData = pd.DataFrame(columns=columns)
samples = sorted(samples)

for i in range(n_samples):
        
    #get the path to the wav files (.raw/wav) and to the README file (.raw/etc/README)
    sample = samples[i]
    sample_folder = os.path.join(raw_folder, sample)
    sample_wav_folder = os.path.join(sample_folder, 'wav')
    readme_file = os.path.join(sample_folder, 'etc', 'README')

    #get the gender from the readme file
    try:
        gender = 'Unknow'
        if os.path.isfile(readme_file):
            gender = get_gender(readme_file)
            gender = add_lable(gender)
    except:
        print(sample_folder)
    
    
        
    #Read and extract the information from the wav files:        
    if os.path.isdir(sample_wav_folder):
        frequencies = get_freq(sample_wav_folder)
        if len(frequencies) > 10: 
            nobs, mean, skewness, kurtosis, median, mode, std, low, peak, q25, q75, iqr = get_features(frequencies)
            sample_dict = {'nobs':nobs, 'mean':mean, 'skewness':skewness, 'kurtosis':kurtosis,
                           'median':median, 'mode':mode, 'std':std, 'low': low,
                           'peak':peak, 'q25':q25, 'q75':q75, 'iqr':iqr, 
                           'lable':gender}

            #Save to my pandas dataframe
            myData.loc[i] = pd.Series(sample_dict)

#and store it to a file
myData.to_csv('clean_Data.csv')
=======
raw_folder = './raw_data/'
os.chdir('Data')
>>>>>>> 375499dc44cc3774237962fff70256cff96b1b9f
