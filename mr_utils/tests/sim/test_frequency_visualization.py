import unittest
import numpy as np

class FreqVisualizationUnitTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_freq_vis(self):
        from mr_utils.sim.frequency_visualization import create_grid,excite,apply_gradients,show_slices

        # Create a grid
        lims = .005
        num_x = 4
        num_y = 8
        num_slices = 5
        X,Y,Z = create_grid((-lims,lims,num_x),(-lims,lims,num_y),(-lims,lims,num_slices))

        # Initialize omegas to random frequencies
        a,b = -1.e6,1e6 # Hz
        W = (b - a)*np.random.random(X.shape) + a
        # show_slices((X,Y,Z),W)

        # Enter main magnetic field
        gamma = 42.58*2*np.pi*1e6 # Hz/T
        B0 = 3 # T
        W = np.ones(X.shape)*gamma*B0
        # show_slices((X,Y,Z),W)

        # Slice select gradient
        Gx,Gy,Gz = 0,0,20e-3 # Hz/T
        W = apply_gradients((X,Y,Z),(Gx,Gy,Gz))
        # show_slices((X,Y,Z),W)

        # Excitation
        BW = 1000 # Hz
        X,Y,Z,W = excite((X,Y,Z),W,BW)
        # show_slices((X,Y,Z),W)

        # Phase Encode
        Gx,Gy,Gz = 0,20e-3,0 # Hz/T
        W = apply_gradients((X,Y,Z),(Gx,Gy,Gz))
        # show_slices((X,Y,Z),W)

        # Frequency Encode
        Gx,Gy,Gz = 10e-3,20e-3,0 # Hz/T
        W = apply_gradients((X,Y,Z),(Gx,Gy,Gz))
        # show_slices((X,Y,Z),W)

    def test_spins(self):
        from mr_utils.sim.frequency_visualization import create_spins,get_spin_vals,excite_spins,precess_spins

        T1_map = np.array([ [1,1.5],[2,2.5] ])
        T2_map = np.array([ [.8,1],[1.2,1.4] ])
        M0_map = np.array([ [1,2],[3,4] ])

        spins = create_spins(M0_map,T1_map,T2_map)
        print(get_spin_vals(spins))

        alphas = np.array([ [0,np.pi/4],[np.pi/2,3*np.pi/4] ])
        excite_spins(spins,alphas)
        print(get_spin_vals(spins))

        precess_spins(spins,1)
        print(get_spin_vals(spins))


if __name__ == '__main__':
    unittest.main()
