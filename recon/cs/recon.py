import numpy as np
from scipy.optimize import minimize

def tv_norm_aniso(im_est):
    '''2D, anisotropic TV norm.'''

    norm = np.sum(np.abs(np.roll(im_est,1,axis=0) - im_est) + np.abs(np.roll(im_est,1,axis=1) - im_est),axis=(0,1))
    return(norm)

def run(kspace,obj,niter=200,tol=1e-8):

    cur_x = kspace.copy()
    gamma = .5 # const step size multiplier
    previous_step_size = 1

    # Forward finite difference method
    def grad(x0,h=1e-5):
        g = np.empty_like(x0)
        for ii in range(x0.size):
            x_tmp = x0.copy()
            x_tmp[ii] += h
            g[ii] = (obj(x_tmp) - obj(x0))/h
        return(g)

    # Gradient descent method
    iter = 0
    # while (np.any(previous_step_size > tol)) & (iter < niter):
    while iter < niter:
        prev_x = cur_x
        cur_x -= gamma*grad(prev_x)
        # previous_step_size = np.abs(cur_x - prev_x)
        iter += 1
        if np.mod(iter,100):
            print('Progress... [%d%%]\r' % (iter/niter*100),end='')

    print('Iter total: %d' % iter)
    print('Min at %f' % obj(cur_x))

    return(cur_x)

def ed_run(kspace,weights,niter=70,step=0.5):
    # These methods are scale sensitive so we arbitrarily rescale the image so
    # that the max value is 4 for consistency's sake
    MAGIC_SCALE_NUMBER = 4.

    #create_image_input(kspace)
    im0 = np.fft.ifftn(kspace)

    #scale_image_input()
    scale_factor = MAGIC_SCALE_NUMBER/np.max(np.abs(im0[:]))
    im0 *= scale_factor

    # iteratively_reconstruct()
    im_est = im0.copy()
    for ii in range(niter):
        # update_fidelity_term
        fidelity_term = weights[0]*(im0 - im_est)

        # update_spatial_term
        spatial_term = weights[1]*tv_norm_aniso(im_est)

        # update_image_estimate
        image_update = step_size*(fidelity_term + spatial_term)
        im_est += image_update

    # unscale_image()
    im_est /= scale_factor

    return(im_est)

if __name__ == '__main__':

    import matplotlib.pyplot as plt

    # Create a sparse signal in the Fourier domain
    x0 = np.sin(np.linspace(0,2*np.pi,200)*3)
    x0 = np.fft.fft(np.fft.ifft(x0))

    # Undersample it
    n_coeffs = 100
    idx = np.random.permutation(x0.size)
    idx = idx[0:n_coeffs]
    ds_x0 = np.zeros(x0.shape,dtype='complex')
    ds_x0[idx] = x0[idx]

    # Give an objective function
    def obj(x_curr):
        # Fidelity term
        fidelity_term = .5*np.linalg.norm(ds_x0[idx] - x_curr[idx])

        # l1 minimization
        l1_min_term = np.linalg.norm(np.abs(np.fft.fftshift(np.fft.fft(x_curr))),ord=1)
        return(fidelity_term + l1_min_term)

    x = run(ds_x0,obj)

    plt.plot(np.abs(np.fft.fftshift(np.fft.fft(x))))
    plt.plot(np.abs(np.fft.fftshift(np.fft.fft(x0))),'--')
    plt.show()

    plt.plot(np.abs(x))
    plt.plot(np.abs(x0),'--')
    plt.show()
