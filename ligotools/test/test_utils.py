import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.interpolate import interp1d

# from ligotools.utils import whiten
# from ligotools.utils import write_wavfile
# from ligotools.utils import reqshift
# from ligotools.utils import plot_helper
from ligotools import *

# Regression Test on whiten() function in utils.py
def test_whiten():
    dt = 0.01
    strain_test = np.arange(1, 1000)
    Pxx_test, freqs_test = mlab.psd(strain_test, Fs = 4096, NFFT = 512)
    psd_test = interp1d(freqs_test, Pxx_test)
    result = whiten(strain_test, psd_test, dt)
    
    first_10_key = np.array([-111.08771602, 58.79772201, -20.7398044, 11.57002635,
         -8.06776397, 4.9959963, -4.16737349, 2.95248942, -2.83196938, 2.48827797])
    
    assert type(result[:10]) == type(first_10_key), "Wrong Type"
    assert np.allclose(result[:10], first_10_key), "Wrong Value"

def test_write_wavfile():
    data_test = np.arange(1, 1000)
    write_wavfile("unit_test.wav", 4096, data_test)
    
    first_10_key = np.array([29, 59, 88, 118, 147, 177, 206, 236, 265, 295])
    
    cdir = os.getcwd()
    f = wavfile.read(cdir + "/audio/unit_test.wav")
    
    assert type(f[1][:10]) == type(first_10_key), "Wrong Type"
    assert (f[1][:10] == first_10_key).all(), "Wrong Value"
    
    os.remove(cdir + "/audio/unit_test.wav")

# Regression Test on reqshift() function in utils.py
def test_reqshift():
    dt = 0.001
    strain_test = np.arange(1, 1000)
    Pxx_test, freqs_test = mlab.psd(strain_test, Fs = 4096, NFFT = 512)
    psd_test = interp1d(freqs_test, Pxx_test)
    whiten_test = whiten(strain_test, psd_test, dt)
    result = reqshift(whiten_test, fshift=1000, sample_rate=4096)
    
    first_10_key = np.array([-2790.36470897, 1023.42737067, 374.29757367, -992.00055018, 1010.37863495, 
                             -846.73870791, 745.83944289, -704.94183416, 653.34915656, -585.46202111])
    
    assert type(result[:10]) == type(first_10_key), "Wrong Type"
    assert np.allclose(result[:10], first_10_key), "Wrong Value"
    
# Regression Test on plot_helper() function in utils.py
def test_plot_helper():
    temp = np.arange(1, 10)
    result = plot_helper(temp, 1126259462.432373, temp, 'g', 'L1', 'GW150914', 'png', 1126259462.44, temp, 
                    temp, temp, temp, 999.7431303063776, temp, temp, 4096, False)
    print(result)
    assert result == "L1 ASD and template around event", "Wrong Title"