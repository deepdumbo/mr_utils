import unittest
import numpy as np
from mr_utils.gadgetron.configs import GadgetronConfig,default_config,grappa_cpu_config
from mr_utils.gadgetron import client
from mr_utils.test_data import GadgetronClient
from mr_utils.test_data import GadgetronTestConfig
from mr_utils import view
from xmldiff import main

class GadgetronConfigTestCase(unittest.TestCase):

    def setUp(self):
        self.config = GadgetronConfig()

    def test_create_xml(self):
        self.config.add_reader(1008,'GadgetIsmrmrdAcquisitionMessageReader')
        self.config.add_writer(1004,'MRIImageWriterCPLX')
        self.config.add_writer(1005,'MRIImageWriterFLOAT')
        self.config.add_writer(1006,'MRIImageWriterUSHORT')
        self.config.add_gadget('Acc','AccumulatorGadget')
        self.config.add_gadget('FFT')
        self.config.add_gadget('Extract')
        self.config.add_gadget('ImageFinishFLOAT','ImageFinishGadgetFLOAT')
        # self.config.print()

    def test_create_default_config(self):
        config = default_config()
        truth = GadgetronTestConfig.default_config()
        res = len(main.diff_texts(truth.encode(),config.tostring().encode()))
        self.assertTrue(res == 0)

    def test_use_default_config(self):
        # Give the filename of raw data to the client
        filename = GadgetronClient.raw_input_filename()

        # Send gadgetron the local default configuration file
        config = default_config()
        # print(config)
        # data,header = client(filename,config_local=config.get_filename())
        data,header = client(filename,config_local=config.tostring())

        # Make sure the output is the same as when h5 is given
        true_output_data = GadgetronClient.true_output_data()
        assert(np.allclose(data,true_output_data))

    def test_use_grappa_cpu_config(self):
        filename = GadgetronClient.grappa_input_filename()
        config = grappa_cpu_config()
        data,header = client(filename,config_local=config.tostring())
        # view(data)
        # data,header = client(filename,config='grappa_cpu.xml')
        # np.save('true_output_data_grappa_cpu.npy',data)
        true_output_data = GadgetronClient.true_output_data_grappa_cpu()
        assert(np.allclose(data,true_output_data))

    def test_use_grappa_cpu_float_config(self):
        filename = GadgetronClient.grappa_input_filename()
        config = GadgetronConfig()

        config.add_reader(1008,'GadgetIsmrmrdAcquisitionMessageReader')
        config.add_reader(1026,'GadgetIsmrmrdWaveformMessageReader')
        config.add_writer(1022,'MRIImageWriter')
        config.add_gadget('NoiseAdjust')
        config.add_gadget('PCA','PCACoilGadget')
        config.add_gadget('CoilReduction',props=[
            ('coils_out','16')
        ])
        config.add_gadget('AsymmetricEcho','AsymmetricEchoAdjustROGadget')
        config.add_gadget('RemoveROOversampling')
        config.add_gadget('Grappa',props=[
            ('target_coils','8'),
            ('use_gpu','false')
        ])
        config.add_gadget('GrappaUnmixing')
        config.add_gadget('Extract')
        # config.add_gadget('ImageWrite','ImageWriterGadgetFLOAT')
        # config.add_gadget('AutoScale')
        # config.add_gadget('FloatToShort','FloatToUShortGadget')
        config.add_gadget('ImageFinish')

        data,header = client(filename,config_local=config.tostring())


    def test_python_config(self):

        # dir = '/usr/local/share/gadgetron/python'
        dir = '/home/myuser/scripts/python'

        config = GadgetronConfig()
        config.add_reader(1008,'GadgetIsmrmrdAcquisitionMessageReader')
        config.add_reader(1026,'GadgetIsmrmrdWaveformMessageReader')
        config.add_writer(1022,'MRIImageWriter')
        config.add_gadget('RemoveOversamplingPython',props=[
            ('python_path',dir),
            ('python_module','remove_2x_oversampling'),
            ('python_class','Remove2xOversampling')
        ])
        config.add_gadget('AccReconPython',props=[
            ('python_path',dir),
            ('python_module','accumulate_and_recon'),
            ('python_class','AccumulateAndRecon')
        ])
        config.add_gadget('CoilCombinePython',props=[
            ('python_path',dir),
            ('python_module','rms_coil_combine'),
            ('python_class','RMSCoilCombine')
        ])
        config.add_gadget('ImageViewPython',props=[
            ('python_path',dir),
            ('python_module','image_viewer'),
            ('python_class','ImageViewer')
        ])
        config.add_gadget('Extract')
        config.add_gadget('ImageFinish')

        truth = GadgetronTestConfig.python_config()
        res = len(main.diff_texts(truth.encode(),config.tostring().encode()))
        self.assertTrue(res == 0)

        # filename = GadgetronClient.raw_input_filename()
        # data,header = client(filename,config_local=config.tostring())


if __name__ == '__main__':
    unittest.main()
