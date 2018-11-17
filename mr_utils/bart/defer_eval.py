from mr_utils.bart import Bartholomew as B
from mr_utils import view

class DeferEval(object):

    def __init__(self):
        self.evaluated = False
        self.queue = []
        self.outputs = {}

    def add(self,fun,output,*args,**kwargs):
        self.queue.append((fun,output,args,kwargs))
        self.outputs[output] = None

    def eval(self):
        for cmd in self.queue:

            # Get ouput for args
            format_args = []
            for a in cmd[2]:
                if type(a) is Output:
                    format_args.append(self.outputs[a.var_name])
                else:
                    format_args.append(a)

            # Get output for kwargs
            format_kwargs = {}
            for key,val in cmd[3].items():
                if type(val) is Output:
                    format_kwargs[key] = self.outputs[val.var_name]
                else:
                    format_kwargs[key] = val

            # Evaluate the function
            self.outputs[cmd[1]] = cmd[0](*format_args,**format_kwargs)

        self.evaluated = True

class Output(object):
    def __init__(self,var_name):
        self.var_name = var_name


if __name__ == '__main__':

    defer = DeferEval()

    num_spokes = 32
    num_chan = 8
    traj_rad = Output('traj_rad')
    traj_rad2 = Output('traj_rad2')
    ksp_sim = Output('ksp_sim')
    igrid = Output('igrid')

    defer.add(B.traj,'traj_rad',x=512,y=num_spokes,r=True)
    defer.add(B.scale,'traj_rad2',0.5,traj_rad)
    defer.add(B.phantom,'ksp_sim',k=True,s=num_chan,t=traj_rad2)
    defer.add(B.scale,'traj_rad2',0.6,traj_rad)
    defer.add(B.nufft,'igrid',ksp_sim,i=True,t=traj_rad2)
    defer.add(B.rss,'reco1',num_chan,igrid)
    defer.eval()

    view(defer.outputs['reco1'])
