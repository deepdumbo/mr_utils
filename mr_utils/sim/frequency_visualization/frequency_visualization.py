# Visualization of frequency as a function of 3d position with arbitrary pulse
# sequence parameters.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def create_grid(xparams,yparams,zparams):
    x = np.linspace(*xparams)
    y = np.linspace(*yparams)
    z = np.linspace(*zparams)
    X,Y,Z = np.meshgrid(x,y,z)
    return(X,Y,Z)

def apply_gradients(XYZ,Gi,B0=3,gamma=42.58*2*np.pi*1e6):
    Gi = np.array(Gi)
    XYZ = np.array(XYZ)
    W0 = gamma*(B0*np.ones(XYZ[0].shape) + Gi.dot(XYZ.transpose(1,2,0,3)))
    return(W0)

def excite(XYZ,W,BW,B0=3,gamma=42.58*2*np.pi*1e6):
    # This is basically masking all frequencies except those excited
    w0 = B0*gamma
    mask = np.logical_and(W >= (w0 - BW/2),W <= (w0 + BW/2))
    W0 = W*mask
    X,Y,Z = [ mask*U for U in XYZ ]
    return(X,Y,Z,W0)

def show_slices(XYZ,W):
    fig = plt.figure()

    for ii in range(W.shape[-1]):
        ax = fig.gca(projection='3d')
        ax.plot_surface(*[ A[:,:,ii] for A in XYZ[:-1] ],W[:,:,ii])
    plt.show()

class Spin(object):
    def __init__(self,M0,T1,T2):
        self.M0 = M0
        self.T1 = T1
        self.T2 = T2
        self.M = np.array([ 0,0,self.M0 ])
        self.B = np.array([ 0,0,3 ])

        # Rotation matrices
        self.Rx = lambda alpha: np.array(((1,0,0),(0,np.cos(alpha),-np.sin(alpha)),(0,np.sin(alpha),np.cos(alpha))))
        self.Ry = lambda beta: np.array(((np.cos(beta),0,np.sin(beta)),(0,1,0),(-np.sin(beta),0,np.cos(beta))))
        self.Rz = lambda gamma: np.array(((np.cos(gamma),-np.sin(gamma),0),(np.sin(gamma),np.cos(gamma),0),(0,0,1)))

    def get_sig(self):
        return(self.M[0] + 1j*self.M[1])

    def excite(self,alpha,beta,gamma):
        self.M = np.linalg.multi_dot((self.Rz(gamma),self.Ry(beta),self.Rx(alpha),self.M))

    def precess(self,t0,dt=1e-4,gamma=42.58):
        Mx,My,Mz = self.M[:]
        Bx,By,B0 = self.B[:]
        steps = int(t0/dt)
        for ii in range(steps):
            Mx += (gamma*(My*B0 - Mz*By) - Mx/self.T2)*dt
            My += (gamma*(Mz*Bx - Mx*B0) - My/self.T2)*dt
            Mz += (gamma*(Mx*By - My*Bx) - (Mz - self.M0)/self.T1)*dt

        self.M = np.array([ Mx,My,Mz ])


def create_spins(M0_map,T1_map,T2_map):
    '''Create an array of spins given proton densities, T1s, and T2s.

    M0_map -- proton density map, or how relative amount of signal at location.
    T1_map -- T1 time constant values for all spin locations.
    T2_map -- T2 time constant values for all spin locations.

    Returns an array of spins.
    '''

    spins = list()
    for ii in range(M0_map.shape[0]):
        row = list()
        for jj in range(M0_map.shape[1]):
            row.append(Spin(M0_map[ii,jj],T1_map[ii,jj],T2_map[ii,jj]))
        spins.append(row)
    return(np.array(spins))

def excite_spins(spins,alphas):
    for (ii,jj),spin in np.ndenumerate(spins):
        spin.excite(alphas[ii,jj],0,0)

def precess_spins(spins,t0):
    for (ii,jj),spin in np.ndenumerate(spins):
        spin.precess(t0)

def get_spin_vals(spins):
    vals = np.zeros(spins.shape,dtype='complex')
    for (ii,jj),spin in np.ndenumerate(spins):
        vals[ii,jj] = spin.get_sig()
    return(vals)

if __name__ == '__main__':
    pass
