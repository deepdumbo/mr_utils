from mr_utils.gadgetron import GadgetronConfig

def distributed_default():
    config = GadgetronConfig()
    config.add_reader('1008','GadgetIsmrmrdAcquisitionMessageReader')
    config.add_reader('1022','MRIImageReader')
    config.add_writer('1022','MRIImageWriter')
    config.add_writer('1008','GadgetIsmrmrdAcquisitionMessageWriter')
    config.add_gadget('Distribute','IsmrmrdAcquisitionDistributeGadget',dll='gadgetron_distributed',props=[
        ('parallel_dimension','repetition'),
        ('use_this_node_for_compute','true')
    ])
    config.add_gadget('RemoveROOversampling')
    config.add_gadget('AccTrig','AcquisitionAccumulateTriggerGadget',props=[
        ('trigger_dimension','repetition'),
        ('sorting_dimension','slice')
    ])
    config.add_gadget('Buff','BucketToBufferGadget',props=[
        ('N_dimension',''),
        ('S_dimension',''),
        ('split_slices','true')
    ])
    config.add_gadget('SimpleRecon')
    config.add_gadget('ImageArraySplit')
    config.add_gadget('Collect',dll='gadgetron_distributed')
    config.add_gadget('Extract')
    config.add_gadget('Sort','ImageSortGadget',props=[
        ('sorting_dimension','repetition')
    ])
    config.add_gadget('ImageFinish')
    return(config)

def distributed_image_default():
    config = GadgetronConfig()
    config.add_reader('1008','GadgetIsmrmrdAcquisitionMessageReader')
    config.add_reader('1022','MRIImageReader')
    config.add_writer('1022','MRIImageWriter')
    config.add_writer('1008','GadgetIsmrmrdAcquisitionMessageWriter')
    config.add_gadget('RemoveROOversampling')
    config.add_gadget('AccTrig','AcquisitionAccumulateTriggerGadget',props=[
        ('trigger_dimension','repetition'),
        ('sorting_dimension','slice')
    ])
    config.add_gadget('Buff','BucketToBufferGadget',props=[
        ('N_dimension',''),
        ('S_dimension',''),
        ('split_slices','true')
    ])
    config.add_gadget('SimpleRecon')
    config.add_gadget('ImageArraySplit')

    config.add_gadget('Distribute','IsmrmrdImageDistributeGadget',dll='gadgetron_distributed',props=[
        ('parallel_dimension','repetition'),
        ('use_this_node_for_compute','true'),
        ('single_package_mode','true')
    ])
    config.add_gadget('Extract')
    config.add_gadget('Collect',dll='gadgetron_distributed')
    config.add_gadget('ImageSort',props=[
        ('sorting_dimension','repetition')
    ])
    config.add_gadget('ImageFinish')
    return(config)

if __name__ == '__main__':
    pass
