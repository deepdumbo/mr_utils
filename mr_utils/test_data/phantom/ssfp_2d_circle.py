import numpy as np
from mr_utils.sim.ssfp import ssfp

def ssfp_2d_circle(dims=(256,256),T1=.8,T2=.5,TR=6e-6,alpha=np.pi/3,min_df=0,max_df=500):

    x = np.linspace(min_df,max_df,dims[0])
    y = np.linspace(min_df,max_df,dims[1])
    field_map,_ = np.meshgrid(x,y)
    im = ssfp(T1,T2,TR,alpha,field_map)
    return(im)

if __name__ == '__main__':
    pass
