import numpy as np
import matplotlib.pyplot as plt
from mr_utils.test_data.phantom import modified_shepp_logan
from scipy.signal import decimate

def create_frames(im,traj,backfill=0):
    num_frames = len(traj)

    # Find change in bounds
    x_running = [0]
    y_running = [0]
    cur = [0.,0.]
    for ii in range(num_frames):
        cur[0] += traj[ii][0]
        cur[1] += traj[ii][1]
        x_running.append(cur[0])
        y_running.append(cur[1])
    dxmin = np.abs(np.min(x_running))
    dxmax = np.max(x_running)
    dymin = np.abs(np.min(y_running))
    dymax = np.max(y_running)

    # Create frames that have enough room for the image to move around in
    frames = np.zeros((im.shape[0]+dxmin+dxmax,im.shape[1]+dymin+dymax,num_frames+1))

    # First frame is zero-padded original image
    frames[:,:,0] = np.pad(im,((dxmin,dxmax),(dymin,dymax)),mode='constant')

    for ii in range(num_frames):
        frames[:,:,ii+1] = np.roll(frames[:,:,ii],traj[ii],axis=(0,1))

    return(frames)

def play(frames):
    for ii in range(frames.shape[-1]):
        plt.imshow(frames[:,:,ii])
        plt.show()

def create_frames_from_position(im,im_dims,positions,time_grid):
    # For each position, figure out the number of pixels we need to move
    px2m_x = im.shape[0]/im_dims[0]
    px2m_y = im.shape[1]/im_dims[1]
    positions_px = [ (np.round(px2m_x*pos[0]).astype(int),np.round(px2m_y*pos[1]).astype(int)) for pos in positions ]

    # Find the max displacements to zeropad image to this new size
    dxmax = max(np.abs(positions_px),key=lambda t: t[0])[0]
    dymax = max(np.abs(positions_px),key=lambda t: t[1])[1]
    dmax = max([dxmax,dymax]) # use only the max to make it square

    # First frame is zero-padded original image
    frame0 = np.pad(im,((dmax,dmax),(dmax,dmax)),mode='constant')

    kspace = np.zeros(time_grid.shape,dtype='complex')
    idx = 0
    prev_position = None
    for ii in range(time_grid.shape[0]):
        for jj in range(time_grid.shape[1]):
            # Keep track of the position, if it repeats, then we don't have to
            # recalculate
            if prev_position != positions_px[idx]:
                # Store prev position for next time around
                prev_position = positions_px[idx]

                # Compute fft of frame
                tmp = np.roll(frame0,positions_px[idx],axis=(0,1))
                tmpfft = np.fft.fftshift(np.fft.fft2(tmp))

            # The frame is too big, so find the subarray that corresponds to
            # ii,jj, take the mean of the subarray and use this as px value.
            tmp = np.array_split(tmpfft,time_grid.shape[0],axis=0)[ii]
            tmp = np.array_split(tmp,time_grid.shape[1],axis=1)[jj]
            kspace[ii,jj] = np.mean(tmp)
            idx += 1
        print('Status: [%d%%]\r' % (ii/time_grid.shape[0]*100),end='')

    return(kspace,positions_px)

def cartesian_acquire(pos,time_grid):

    # We only have im.shape pixels, but positions probably has some noninteger
    # locations that we need to be at.  So define how close we want to get, and
    # we'll go with that
    idx = 0
    xs = np.zeros(time_grid.size)
    ys = np.zeros(time_grid.size)
    kspace = np.zeros(time_grid.shape,dtype='complex')
    for ii in range(time_grid.shape[0]):
        for jj in range(time_grid.shape[1]):

            scale = 20
            x_pad = (scale*time_grid.shape[0],scale*time_grid.shape[0])
            y_pad = (0,0)
            frame = np.pad(time_grid,(x_pad,y_pad),mode='constant')*0
            frame[0,0] = 1
            frame = np.fft.fftshift(frame)

            xs[idx] = np.round((pos[0])(time_grid[ii,jj])*scale)
            ys[idx] = np.round((pos[1])(time_grid[ii,jj])*scale)

            tmp = np.roll(frame,(int(xs[idx]),int(ys[idx])),axis=(0,1))
            # print(np.argmax(tmp))
            tmp = decimate(tmp,scale*2+1,axis=0) # this doesn't seem to be working...
            tmpfft = np.fft.fftshift(np.fft.fft2(tmp))
            kspace[ii,jj] = tmpfft[ii,jj]

            idx += 1

    # Create frames for each time point t
    # kspace,positions_px = create_frames_from_position(im,im_dims,positions,time_grid)
    return(kspace,xs,ys)

def get_time_grid(dims,TR,BW):
    '''Defines the kspace trajectory and the times each voxel gets measured.

    dims -- size of grid, rows are frequency encodes, cols are phase encodes.
    TR -- repetition time.
    BW -- readout bandwidth, Hz.
    '''

    PEs,FEs = dims
    dwell_time = 1/BW
    row_time = PEs*dwell_time

    assert row_time < TR,'TR must be less than sample time, %g !< %g' % (TR,row_time)

    t0 = 0 # time at the beginning of a row
    time_grid = np.zeros(dims)
    for row in range(PEs):
        # Row starts at t0 and ends after the time it takes to get a row
        time_grid[row,:] = np.linspace(t0,t0+row_time,FEs)
        # The new start time happens after TR
        t0 += TR
    return(time_grid)

if __name__ == '__main__':
    pass
