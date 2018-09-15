import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    num_bins = 500

    # Map the frequencies to locations
    freq_locations = np.linspace(1e3,10e3,num_bins)

    # Create image space 1D M0 map
    m0 = np.zeros(num_bins)
    step = 20
    m0[:step:] = np.ones(m0[:step:].shape)

    # The signal we record is the sum of all oscillors with M0 weights, listen
    # for a full period
    t = np.linspace(0,np.pi,num_bins)
    # sig = m0*np.exp(-1j*freq_locations*t)
    sig = np.array([ m0.dot(np.exp(-1j*freq_locations*tt)) for tt in t ])
    # sig = np.array([ m0.dot(np.exp(-1j*ws*tt)) for tt in t ])

    # Show the signal we recieved
    plt.plot(t,np.abs(sig))
    plt.title('Recieved Signal')
    plt.show()

    # Fourier transform to get back the frequencies from the time domain signal
    im = (np.fft.ifft(sig))

    #  Each frequency has an associated location, we're interested in the
    # locations associated with each ws
    freqs = np.fft.fftfreq(im.size)


    plt.plot(freqs,np.abs(im))
    # center = int(sig.size/2)
    # plt.plot(np.abs(im[center:center+pd.size*3]))
    plt.title('Reconstructed Proton Density Map')
    plt.show()
