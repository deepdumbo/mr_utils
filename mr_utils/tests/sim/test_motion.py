import unittest
import numpy as np
import matplotlib.pyplot as plt

class SimMotionTestCase(unittest.TestCase):

    def test_motion_delta(self):
        from mr_utils.sim.motion import cartesian_acquire,get_time_grid
        from mr_utils.test_data.phantom import delta_2d

        d = delta_2d((32,32))
        pos = (lambda t: 0,lambda t: 0)
        BW = 50e3
        TR = 5e-3
        print(TR)
        time_grid = get_time_grid(d.shape,TR,BW)

        kspace,xs,ys = cartesian_acquire(pos,time_grid)
        imspace = np.fft.ifft2(kspace)

        plt.subplot(2,1,1)
        plt.imshow(np.rot90(d))
        plt.title('Original Image')
        plt.subplot(2,1,2)
        plt.imshow(np.rot90(np.abs(imspace)))
        plt.title('PSF')
        plt.show(block=True)
        plt.figure()
        plt.plot(time_grid.flatten(),xs)
        plt.show()

    def test_motion_shepp_logan(self):
        from mr_utils.sim.motion import cartesian_acquire
        from mr_utils.test_data.phantom import modified_shepp_logan

        # Load in a shepp logan phantom, 2D
        dim = 32
        im = modified_shepp_logan((dim,dim,dim))[:,:,int(dim/2)]
        im_dims = (.05,.05) # cm x cm image

        # Create a position function for the object in image space
        # pos = (lambda t: 0,lambda t: 0)
        # pos = (lambda t: .0035*t,lambda t: 0)
        pos = (lambda t: .0025*np.sin(t*5),lambda t: 0)

        # The time grid defines the kspace trajectory and the times each voxel
        # gets measured
        row_time = 2e-3 # seconds for one phase encode
        TR = 5e-3 # TR must be greater than the time it takes to get one row
        self.assertLess(row_time,TR)
        t0 = 0 # time at the beginning of a row
        pts_per_line = dim
        PEs = dim
        time_grid = np.zeros((PEs,pts_per_line))
        for row in range(PEs):
            # Row starts at t0 and ends after the time it takes to get a row
            time_grid[row,:] = np.linspace(t0,t0+row_time,pts_per_line)

            # The new start time happens after TR
            t0 += TR

        # cartesian_acquire(im,im_dims,pos,time_grid)


if __name__ == '__main__':
    unittest.main()
