import scipy.io.wavfile as wf
import scipy
import scipy.fftpack as fftpk
import numpy as np
from matplotlib import pyplot as plt

# this procedure shows the averaged fft graph of the .wav input file
def show_fourier_graph_compare(PATH):
    

    #fast fourier transform of input signal
    s_rate , signal = wf.read(PATH)
    FFT = np.abs(fftpk.fft(signal))
    freqs = fftpk.fftfreq(len(FFT), (1.0/s_rate))


    # doing an average of the values between the frequences n and n+0.5
    a = 0.5
    res = []
    sum = 0
    den = 0
    for i,f in enumerate(freqs[range(len(FFT)//2)]):
        if f <= a:
            sum += FFT[i][0]
            den+=1
        else:
            if den == 0:
                res.append(0)
            else:
                res.append(sum/den)
            
            if f <= a + 0.5 :
                sum = FFT[i][0]
                den = 1
                a +=0.5
            else :
                res.append(0)
                sum = 0
                den = 0
                a +=1
    
    # new frequences for res, you can use them to visualise the graph of the output with matplotlib
    freqs = np.arange(0.0,20000,0.5)
    
    # plot of the figure
    
    while len(res) < 40000:
        res.append(0)

    plt.plot(freqs, res[:40000])

    plt.xlabel("Frequence (Hz)")
    plt.ylabel("Amplitude")
    plt.xlim([0,20000])
    plt.ylim(bottom=0)
    plt.title(PATH)

    #show figure
    plt.show()

fem1 = "C:\\Users\\marti\\Desktop\\fem1.wav"
vem1 = "C:\\Users\\marti\\Desktop\\vem1.wav"
fft1 = "C:\\Users\\marti\\Desktop\\fft1.wav"
vvt1 = "C:\\Users\\marti\\Desktop\\vvt1.wav"

show_fourier_graph_compare(fft1)
show_fourier_graph_compare(vvt1)
show_fourier_graph_compare(fem1)
show_fourier_graph_compare(vem1)
