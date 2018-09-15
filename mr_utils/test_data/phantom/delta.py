import numpy as np

def delta_2d(dims=(64,64)):
    '''Create a centered 2d delta function.'''

    d = np.zeros(dims)
    d[0,0] = 1
    d = np.fft.fftshift(d)
    return(d)

if __name__ == '__main__':
    pass
