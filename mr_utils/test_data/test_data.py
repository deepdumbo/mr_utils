from pathlib import Path
from mr_utils.load_data import load_mat

## DAT FILES
bssfp_phantom = str(Path('mr_utils/test_data/raw/bssfp_phantom.dat').resolve())

# For Single Voxel Simulation
single_voxel_512 = str(Path('mr_utils/test_data/tests/sim/single_voxel/single_voxel_512.dat').resolve())
single_voxel_256_0 = str(Path('mr_utils/test_data/tests/sim/single_voxel/single_voxel_256_0.dat').resolve())
single_voxel_256_1 = str(Path('mr_utils/test_data/tests/sim/single_voxel/single_voxel_256_1.dat').resolve())

## MAT FILES
# For SC-GROG:
class SCGROG(object):

    @staticmethod
    def test_grog_data_4D():
        path = str(Path('mr_utils/test_data/tests/gridding/scgrog/test_grog_data_4D.mat').resolve())
        data = load_mat(path)
        traj = data['testTrajectory3D']
        kspace = data['testData4D']
        return(kspace,traj)

    @staticmethod
    def gx_gy_results():
        path = str(Path('mr_utils/test_data/tests/gridding/scgrog/gx_gy_results.mat').resolve())
        data = load_mat(path)
        Gxm = data['officialGx']
        Gym = data['officialGy']
        return(Gxm,Gym)

    @staticmethod
    def test_gridder_data_4D():
        path = str(Path('mr_utils/test_data/tests/gridding/scgrog/test_gridder_data_4D.mat').resolve())
        data = load_mat(path,'KSpaceData')
        kspace = data['kSpace'][0][0]
        traj = data['trajectory'][0][0]
        cartdims = tuple(list(data['cartesianSize'][0][0][0]))
        return(kspace,traj,cartdims)

    @staticmethod
    def test_gx_gy_data():
        path = str(Path('mr_utils/test_data/tests/gridding/scgrog/test_gx_gy_data.mat').resolve())
        data = load_mat(path)
        Gxm = data['Gx']
        Gym = data['Gy']
        return(Gxm,Gym)

    @staticmethod
    def grog_result():
        path = str(Path('mr_utils/test_data/tests/gridding/scgrog/grog_result.mat').resolve())
        data = load_mat(path)
        kspacem = data['officialCartesianKSpace']
        maskm = data['officialKMask']
        return(kspacem,maskm)

# For scr_reordering_adluru:
Coil1_data = str(Path('mr_utils/test_data/tests/recon/reordering/Coil1_data.mat').resolve())
mask = str(Path('mr_utils/test_data/tests/recon/reordering/mask.mat').resolve())
tv_prior = str(Path('mr_utils/test_data/tests/recon/reordering/tv_prior.mat').resolve())
recon = str(Path('mr_utils/test_data/tests/recon/reordering/recon.mat').resolve())
true_orderings = str(Path('mr_utils/test_data/tests/recon/reordering/true_orderings.mat').resolve())
TV_re_order = str(Path('mr_utils/test_data/tests/recon/reordering/TV_re_order.mat').resolve())
TV_term_update = str(Path('mr_utils/test_data/tests/recon/reordering/TV_term_update.mat').resolve())
fidelity_update = str(Path('mr_utils/test_data/tests/recon/reordering/fidelity_update.mat').resolve())
recon_at_iter_100 = str(Path('mr_utils/test_data/tests/recon/reordering/recon_at_iter_100.mat').resolve())
recon_at_iter_1 = str(Path('mr_utils/test_data/tests/recon/reordering/recon_at_iter_1.mat').resolve())
recon_at_iter_2 = str(Path('mr_utils/test_data/tests/recon/reordering/recon_at_iter_2.mat').resolve())
recon_at_iter_10 = str(Path('mr_utils/test_data/tests/recon/reordering/recon_at_iter_10.mat').resolve())
recon_at_iter_50 = str(Path('mr_utils/test_data/tests/recon/reordering/recon_at_iter_50.mat').resolve())

# For elliptical signal model:
class EllipticalSignal(object):
    @staticmethod
    def I1():
        path = str(Path('mr_utils/test_data/tests/recon/ssfp/I1.mat').resolve())
        return(load_mat(path,key='I1'))

    @staticmethod
    def I2():
        path = str(Path('mr_utils/test_data/tests/recon/ssfp/I2.mat').resolve())
        return(load_mat(path,key='I2'))

    @staticmethod
    def I3():
        path = str(Path('mr_utils/test_data/tests/recon/ssfp/I3.mat').resolve())
        return(load_mat(path,key='I3'))

    @staticmethod
    def I4():
        path = str(Path('mr_utils/test_data/tests/recon/ssfp/I4.mat').resolve())
        return(load_mat(path,key='I4'))

    @staticmethod
    def Id():
        path = str(Path('mr_utils/test_data/tests/recon/ssfp/Id.mat').resolve())
        return(load_mat(path,key='M'))

    @staticmethod
    def I():
        path = str(Path('mr_utils/test_data/tests/recon/ssfp/I.mat').resolve())
        return(load_mat(path,key='I'))

    @staticmethod
    def I_max_mag():
        path = str(Path('mr_utils/test_data/tests/recon/ssfp/I_max_mag.mat').resolve())
        return(load_mat(path,key='maximum'))

    @staticmethod
    def CS():
        path = str(Path('mr_utils/test_data/tests/recon/ssfp/CS.mat').resolve())
        return(load_mat(path,key='CS'))

    @staticmethod
    def w13():
        path = str(Path('mr_utils/test_data/tests/recon/ssfp/w13.mat').resolve())
        return(load_mat(path,key='w1'))

    @staticmethod
    def w24():
        path = str(Path('mr_utils/test_data/tests/recon/ssfp/w24.mat').resolve())
        return(load_mat(path,key='w2'))
