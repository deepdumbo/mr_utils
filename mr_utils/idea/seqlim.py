
class SeqLim(object):

    def __init__(self):
        self.orig_filename = ''
        self.seq_owner = ''
        self.seq_hint_text = ''

    ## Available methods
    # Methods to set simple values
    def setMyOrigFilename(filename):
        self.orig_filename = filename

    def setSequenceOwner(owner):
        # Insert your name here (const char *)
        self.seq_owner = owner

    def setSequenceHintText(hint):
        self.seq_hint_text = hin

    # def setRequiredGradAmpl(double); // Minimal gradient amplitude for sequence (mT/m) (double)
    # def setRequiredGradSlewRate(double); // Minimal gradient slew rate for sequence (mT/m)/ms (double)
    # def enableSliceShift(); // Enables slice shift
    # def disableSliceShift(); // Disables slice shift
    # def enableMSMA();  // Enables multi slice multi angle
    # def disableMSMA(); // Disables multi slice multi angle
    # def enableOffcenter(); // Enables offcenter FOV measurements
    # def disableOffcenter(); // Disables offcenter FOV measurements
    # def setReadoutOSFactor(2.0); // Sets the oversampling in readout direction. Default is 2.0, recommended (double)
    # def setExtSrfFilename(const char *); // Location of the RF envelopes (const char *)
    # def setICEProgramFilename(const char *); // Location of the ICE program (const char *)
    # def setMinSliceResolution(double); // Minimum partial fourier in slice (partition) direction (double)
    # def setMaxPhaseResolution(double); // Maximum possible resolution in phase direction (double)
    # def isSquareFOVOnly(false); // Whether or not the sequence allows only square FoV (bool)
    # def enableMoveScanRegion(); // Enables table movement
    # def disableMoveScanRegion(); // Disables table movement
    # def usesVariableFlipAngle(bool); // Whether or not the sequence uses a variable flip angle (bool)
    # def enableSAFEConsistencyCheck(); // Enables the consistency check of the SAFE model
    # def disableSAFEConsistencyCheck(); // Disables the consistency check of the SAFE model
    # def setVoIMaxShift(double); // Maximum possible VoI shift (double)
    # def isSVSSequence(false); // Identifies the sequence as a single voxel spectroscopy sequence (bool)
    # def isCSISequence(false); // Identifies the sequence as a chemical shift imaging sequence (bool)
    # def setNotSupportedSystemTypes(const char *); // List of all systems the sequence will not run on (const char *)
    # def enableCaptureCycle(); // If this is set the actual RR-interval is shown on the Physio Card

#     // Methods to set ParLim values
#     // NLS_STATUS SeqLim::setParameter (Minimum, maximum, increment, default)
#     pSeqLim->setAllowedFrequency(); // Allowed frequency range for sequence (Hz) (long,long)
#     pSeqLim->setContrasts(); // Allowed number of contrasts (echoes) (long,long,long,long)
#     pSeqLim->setSlices(); // Allowed number of slices (long,long,long,long)
#     pSeqLim->setSliceDistanceFactor(); (); // Allowed ratio Gap/SliceThickness (long,long,long,long)
#     pSeqLim->setSliceDistanceFactor(); // double dMin, dMax, SEQ::Increment eInc, dDef
#     pSeqLim->setSliceThickness(); // Allowed slice thickness (mm) (double,double,double,double)
#     pSeqLim->setSlabThickness(); // Allowed slab thickness (mm) (double,double,double,double)
#     pSeqLim->setRSats(); // Number of regular saturation regions the sequence can measure (long,long,long,long)
#     pSeqLim->setRSatThickness(); // Allowed saturation region thickness (mm) (double,double,double,double)
#     pSeqLim->setTSats(); // Number of tracking saturation regions the sequence can measure (long,long,long,long)
#     pSeqLim->setTSatThickness(); // Allowed tracking saturation region thickness (mm) (double,double,double,double)
#     pSeqLim->setTSatGapToSlice(); // Allowed distance from tracking saturation region to the slice block (double,double,double,double)
#     pSeqLim->setPSatThickness(); // Allowed parallel saturation region thickness (mm) (double,double,double,double)
#     pSeqLim->setPSatGapToSlice(); // Allowed distance from parallel saturation region to the slice block (double,double,double,double)
#     pSeqLim->setSatShift(); // Allowed saturation region shifts (mm) (double,double,double,double)
#     pSeqLim->setBaseResolution(); // The base resolution of the matrix. eInc should be SEQ::INC_BASE2 or SEQ::INC_64 (double,double,SEQ::Increment eInc,double)
#     pSeqLim->setPartition(); // Allowed number of partitions (long,long,long,long)
#     pSeqLim->setPartition(); // Allows restriction to binary increments [SEQ::INC_BASE2] (long,long,SEQ::Increment eInc,long)
#     pSeqLim->set3DPartThickness(); // Allowed (mm) partition thickness (double,double,double,double)
#     pSeqLim->setVectorSize(); // Allowed vector sizes (spectroscopy) (long,long,long,long)
#     pSeqLim->setRfBandwidth(); // Allowed RF pulse band widths (spectroscopy) (long,long,long,long)
#     pSeqLim->setVoIPosTra(); // Allowed VoI positions in transverse direction (mm) (spectroscopy) (double,double,double,double)
#     pSeqLim->setVoIPosCor(); // Allowed VoI positions in coronal direction (mm)(spectroscopy) (double,double,double,double)
#     pSeqLim->setVoIPosSag(); // Allowed VoI positions in sagittal direction (mm)(spectroscopy) (double,double,double,double)
#     pSeqLim->setVoISizeSlice(); // Allowed VoI size in slice direcion (mm)(spectroscopy) (double,double,double,double)
#     pSeqLim->setVoISizeReadout(); // Allowed VoI size in readout direction (mm)(spectroscopy) (double,double,double,double)
#     pSeqLim->setVoISizePhase(); // Allowed VoI size in phase direction (mm)(spectroscopy) (double,double,double,double)
#     pSeqLim->setFlipAngle(); // Allowed RF flip angle (degrees) (double,double,double,double)
#     pSeqLim->setAverages(); // Allowed number of averages (long,long,long,long)
#     pSeqLim->setRepetitions(); // Allowed number of sequence repetitions (long,long,long,long)
#     pSeqLim->setRepetitionsDelayTime(); // Allowed repetition delay times (μs) (long,long,long,long)
#     pSeqLim->setConcatenations(); // Allowed number of concatenations (long,long,long,long)
#     pSeqLim->setEPIFactor(); // Allowed EPI factor (double,double,double,double)
#     pSeqLim->setEPIFactor(); // Allowed EPI factor (double,double,SEQ::Increment eInc,double)
#     pSeqLim->setTurboFactor(); // Allowed turbo factor (double,double,double,double)
#     pSeqLim->setTurboFactor(); // Allowed turbo factor (double,double,SEQ::Increment eInc,double)
#     pSeqLim->setSegments(); // Allowed number of segments (long,long,long,long)
#     pSeqLim->setReadoutFOV(); // Allowed field of view in readout direction (mm) (double,double,double,double)
#     pSeqLim->setPhaseFOV(); // Allowed field of view in phase direction (mm) (double,double,double,double)
#     pSeqLim->setPhaseOversampling(); // Amount of oversampling in phase direction (double,double,double,double)
#     pSeqLim->setSliceOversampling(); // Amount of oversampling in slice (partition) direction (double,double,double,double)
#     pSeqLim->setGatingRatio(); // Ratio gated/ungated scans (double,double,double,double)
#     pSeqLim->setLinesGateOpen(); // Lines to measure once the gate is open (long,long,long,long)
#     pSeqLim->setPhase(); // Phases to measure per cycle (long,long,long,long)
#     pSeqLim->setPELines(); // Allowed number of phase encoding lines (long,long,long,long)
#     pSeqLim->setPELines(); // Allows restriction to binary increments (long,long,SEQ::Increment eInc,long)
#     pSeqLim->setBandwidth(); // Receiver bandwidth in Hz (double,double,double,double)
#     pSeqLim->setBandwidthPerPixel(); // Receiver bandwidth/pixel in Hz (double,double,double,double)
#     pSeqLim->setNoOfCombinedEchoes(); // Number of combined echoes (long,long,long,long)
#     pSeqLim->setNoOfDiffWeightings(); // Number of diffusion weightings (long,long,long,long)
#     pSeqLim->setBValue(); // Allowed b value (long,long,long,long)
#     pSeqLim->setPreparingScans(); // Number of preparing scans (long,long,long,long)
#     pSeqLim->setAcquisitionDelay(); // Allowed delay time after acquisition (long,long,long,long)
#     pSeqLim->setCardiacTriggerDelay(); // Allowed delay after cardiac trigger (long,long,long,long)
#     pSeqLim->setRespTriggerDelay(); // Allowed delay after respiratory trigger (long,long,long,long)
#     pSeqLim->setCardiacTriggerPulses(); // Range for number of trigger pulses (long,long,long,long)
#     pSeqLim->setCardiacTriggerWindow(); // Range for width of cardiac trigger window (long,long,long,long)
#     pSeqLim->setEKGGateOnThreshold(); // (long,long,long,long)
#     pSeqLim->setEKGGateOffThreshold(); // (long,long,long,long)
#     pSeqLim->setPulseGateOnThreshold(); // (long,long,long,long)
#     pSeqLim->setPulseGateOffThreshold(); // (long,long,long,long)
#     pSeqLim->setExtGateOnThreshold(); // (long,long,long,long)
#     pSeqLim->setExtGateOffThreshold(); // (long,long,long,long)
#     pSeqLim->setGridTagDistance(); // Range for the width of the tagging grid (long,long,long,long)
#     pSeqLim->setLineTagDistance(); // Range for the distance between of the tagging lines(long,long,long,long)
#     pSeqLim->setNoOfVelocities(); // Number of different flow velocities the sequence can handle (long,long,long,long)
#     pSeqLim->setVelocity(); // Range for the flow velocity the sequence can handle (long,long,long,long)
#     pSeqLim->setRetroGatedImages(); // Range for the number of images possible in retro gating (long,long,long,long)
#     pSeqLim->setfinalMatrixSizePhase(); // Size of final result in phase encoding direction (long,long,SEQ::Increment eInc,long)
#     pSeqLim->setfinalMatrixSizeRead(); // Size of final result in readout direction (long,long,SEQ::Increment eInc,long)
#     pSeqLim->setfinalMatrixSizeSlice(); // Size of final result in slice selection direction (long,long,SEQ::Increment eInc,long)
#     pSeqLim->setOffsetCorrWidth(); // Range for the width of the offset correction (long,long,long,long)
#     pSeqLim->setNavigators(); // Range for the number of navigators (long,long,long,long)
#     pSeqLim->setAccelFactor3D(); // AccelFactor for 3D PAT (long,long,long,long)
#     pSeqLim->setRefLines3D(); // RefLines for 3D PAT (long,long,long,long)
#
#     // Methods to get ParLim values
#     // NLS_STATUS SeqLim::setParameter (Number, minimum, maximum, increment, default)
#     pSeqLim->setTR(); // Repetition time (ms) (long,long,long,long,long)
#     pSeqLim->setTE(); // Echo time (ms) (long,long,long,long,long)
#     pSeqLim->setTI(); // Inversion time (ms) (long,long,long,long,long)
#     pSeqLim->setTD(); // Delay time (ms) (long,long,long,long,long)
#     pSeqLim->setNavigatorThickness(); // Range for thickness of navigator number lNumber (long,double,double,double,double)
#     pSeqLim->setNavigatorReadFOV(); // Range for readout field of view of navigator number lNumber (long,double,double,double,double)
#     pSeqLim->setNavigatorPhaseFOV(); // Range for phase field of view of navigator number lNumber (long,double,double,double,double)
#     pSeqLim->setFlipAngleArray(); // (long,double,double,double,double)
#
#
#     // Methods to set ParLimOption values
#     // NLS_STATUS SeqLim::setParameter (Option1, ...)
#     // The minimum number of parameter is always 1, additional values are optional.
#     // The first parameter is the default value and is used by POET as the parameter
#     // when creating the default protocol.
#     pSeqLim->setAllowedSliceOrientation(); // Orthogonal, single oblique, double oblique (SEQ::SliceOrientation)
#     pSeqLim->setPhaseImages(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setSliceSeriesMode(); // Ascending, descending, interleaved (Up to three of type SEQ::SeriesMode)
#     pSeqLim->setUsedADCs(); // If not set, automatic selection based on coil element selection (Up to eight SEQ::UsedADC)
#     pSeqLim->setPSatMode(); // None, single regular, double regular, single quick, double quick (Up to five of SEQ::PSatMode)
#     pSeqLim->setFlowSensitivity(); // Slow, medium, fast (Up to three of type SEQ::FlowSensitivity)
#     pSeqLim->setPhasePartialFourierFactor(); // Half, 5/8, 6/8, 7/8, off (Up to five of type SEQ::PartialFourierFactor)
#     pSeqLim->setSlicePartialFourierFactor(); // Half, 5/8, 6/8, 7/8, off (Up to five of type SEQ::PartialFourierFactor)
#     pSeqLim->setIntro(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setAveragingMode(); // Inner, outer loop (Up to two of type SEQ::AveragingMode)
#     pSeqLim->setDimension(); // One, two, three (Up to three of SEQ::Dimension)
#     pSeqLim->setEllipticalScanning(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setRFSpoiling(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setMultiSliceMode(); // Sequential, interleaved, single shot (Up to three of type SEQ::MultiSliceMode)
#     pSeqLim->set2DInterpolation(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setFatSuppression(); // Fat saturation, water excitation, water excitation fast, off (Up to three of type SEQ::FatSuppression)
#     pSeqLim->setWaterSuppression(); // Water saturation, fat excitation, off (Up to three of type SEQ::WaterSuppression)
#     pSeqLim->setInversion(); // Slice selective, volume selective, off (Up to three of type SEQ::Inversion)
#     pSeqLim->setMTC(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setRFPulseType(); // Fast, normal, low SAR (Up to three of type SEQ::RFPulseType)
#     pSeqLim->setDarkBlood(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setGradients(); // Fast, normal, whisper (Up to three of type SEQ::Gradients)
#     pSeqLim->setAsymmetricEcho(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setReconstructionMode(); // Magnitude, phase, real part, magnitude and phase, real part and phase (Up to four of type SEQ::ReconstructionMode)
#     pSeqLim->setDiffusionMode(); // Trace, orthogonal, slice, read, phase, optimize, off (Up to seven of type SEQ::DiffusionMode)
#     pSeqLim->setDiffReconMode(); // None, diffusion weighted image, ADC map, trace (Up to four of type SEQ::DiffReconMode)
#     pSeqLim->setPerfReconMode(); // None, original image, time to peak map, signal change map, time course of signal (Up to five of type SEQ::PerfReconMode)
#     pSeqLim->setFMRIReconMode(); // None, z-score, correlation, mosaic images (Up to four of type SEQ::fMRIReconMode)
#     pSeqLim->setAdjShim(); // Tuneup, standard, advanced, interactive, meas only, calculation only (Up to six of type SEQ::AdjShim)
#     pSeqLim->setAdjWatSup(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setPhaseCyclingType(); // None, automatic, twostep, eightstep, exorcycle, sixteenstep-exor (Up to six of type SEQ::PhaseCyclingType)
#     pSeqLim->setPhaseEncodingType(); // Full, elliptical, weighted (Up to three of type SEQ::PhaseEncodingType)
#     pSeqLim->setAllowedVoIOrientation(); // Orthogonal, single oblique, double oblique (Up to three of type SEQ::SliceOrientation)
#     pSeqLim->setCardiacScanWindowDialog(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setRespScanWindowDialog(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setRespGatePhase(); // Expiration or inspiration (Up to two of type SEQ::RespirationPhase)
#     pSeqLim->addPhysioMode(); // E.g. EKG trigger or EKG trigger and resp gating, may be called repeatedly (Up to two of the combination (SEQ::PhysioSignal,SEQ::PhysioMethod))
#     pSeqLim->setExcitationPulse(); // Slice selective, volume selective (Up to two of type SEQ::ExcitationPulse)
#     pSeqLim->setSaturationRecovery(); // None, slice selective, volume selective (Up to three of type SEQ::SaturationRecovery)
#     pSeqLim->setSTIRMode(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setCareBolus(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setSequenceCard(); // None, imaging, spectroscopy (One of type SEQ::SequenceCard)
#     pSeqLim->setTagging(); // None, grid, line tag (Up to three SEQ::Tagging)
#     pSeqLim->setFlowCompensation(); // No, yes, readout only, slice selective only (Up to four of type SEQ::FlowCompensation)
#     pSeqLim->setArrhythmiaDetection(); // None, time-based, pattern-based (Up to three of type SEQ::ArrhythmiaDetection)
#     pSeqLim->setUseMouseData(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setSupportedNuclei(); // Which nuclei are allowed for this sequence? Note that the actually displayed choice of nuclei depends on the coil that is currently plugged in. (Up to nine of type SEQ::MeasNucleus)
#     pSeqLim->setAcquisitionWindowCalculationMode(); // Standard, consider lines , consider partitions (Up to three of type SEQ::AcquisitionWindowCalculationMode)
#     pSeqLim->setPhaseStabilisation(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setCompensateT2Decay(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setFilterType(); // None, raw, large FOV, normalize, elliptical filter (Up to five of SEQ::FilterType)
#     pSeqLim->setReorderMode(); // Linear, centric, line or partition segmented, up to four different free reorder schemes (Up to eight of type SEQ::Reordering)
#     pSeqLim->setMagnitudeImages(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setRephasedImage(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setMagnitudeSum(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setMIPImage(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setStdDevImage(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setPCAngioFlowMode(); // Single velocity, single direction, free (Up to three of type SEQ::PCAngioFlowMode)
#     pSeqLim->setFlowDir(); // None, phase, readout, slice select, free (Up to five of type SEQ::FlowDir)
#     pSeqLim->setRSatMode(); // Regular, quick (Up to two SEQ::RSatMode)
#     pSeqLim->setMultipleSeries(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setOffsetCorr(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setHyperEcho(); // On, off  (Up to two SEQ::Switch)
#     pSeqLim->setRRestoreMagn(); // On, off  (Up to two SEQ::Switch)
# ]
