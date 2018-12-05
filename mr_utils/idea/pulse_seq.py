

# #include "MrServers/MrMeasSrv/SeqIF/Sequence/SeqIF.h"
# #include "MrServers/MrImaging/libSBB/SeqRunKernel.h"
#

class PulseSequence(object):

    def __init__(self,seq_name):
        self.seq_name = seq_name
        self.lines = []
        self.code = ''

    def add_grad(self,waveform):
        pass

    def add_rf(self,waveform):
        pass

    def add_adc(self,waveform):
        pass

    def compile(self):

        self.seq_class()
        self.initialize()
        self.fSEQInit()
        self.fSEQPrep()
        self.fSEQRun()
        self.fSEQCheck()
        self.fSEQRunKernel()

        # Put code into one string
        self.code = '\n'.join(self.lines)

        # Add in all the includes we can find
        self.includes()

        # return the code string
        return(self.code)

    def seq_class(self):
        # Define the seq:
        self.lines.append('SEQIF_DEFINE (%s)' % self.seq_name)

        # main seq class
        self.lines.append('class %s : public SeqIF' % self.seq_name)
        self.lines.append('{')

        # all sequences must have the following functions:
        self.lines.append('virtual NLSStatus initialize (SeqLim*);')
        self.lines.append('virtual NLSStatus prepare (MrProt*, SeqLim*, SeqExpo*);')
        self.lines.append('virtual NLSStatus check (MrProt*, SeqLim*, SeqExpo*, SEQCheckMode*);')
        self.lines.append('virtual NLSStatus run (MrProt*, SeqLim*, SeqExpo*);')

        # end main seq class
        self.lines.append('}')

    def initialize(self):
        self.lines.append('NLSStatus initialize (SeqLim*)')
        self.lines.append('{')
        self.lines.append('}')

    def fSEQInit(self):
        self.lines.append('NLS_STATUS fSEQInit (SeqLim *pSeqLim)')
        self.lines.append('{')
        self.lines.append('}')

    def fSEQPrep(self):
        self.lines.append('NLS_STATUS fSEQPrep (MrProt *pMrPort, SeqLim *pSeqLim, SeqExpo *pSeqExpo)')
        self.lines.append('{')
        self.lines.append('}')

    def fSEQRun(self):
        self.lines.append('NLS_STATUS fSEQRun (MrProt *pMrProt, SeqLim *pSeqLim, SeqExpo *pSeqExpo)')
        self.lines.append('{')
        self.lines.append('}')

    def fSEQCheck(self):
        self.lines.append('NLS_STATUS fSEQCheck (MrProt *pMrProt, SeqLim *pSeqLim, SeqExpo *pSeqExpo, SEQCheckMODE *pSEQCheckMode)')
        self.lines.append('{')
        self.lines.append('}')

    def fSEQRunKernel(self):
        self.lines.append('static NLS_STATUS fSEQRunKernel (MrProt *pMrProt, SeqLim *pSeqLim, SeqExpo *pSeqExpo, long lKernelMode, long lChronologicSliceIndex, long lPartitionIndex, long lLineIndex)')
        self.lines.append('{')
        self.lines.append('}')

    def includes(self):
        # Take care of includes
        if any(el in self.code for el in [ 'SeqIF','MrProt','SeqLim','SeqExpo','SEQCheckMode','SEQData' ]):
            self.code = '#include "MrServers/MrMeasSrv/SeqIF/Sequence/SeqIF.h"\n' + self.code
        elif 'NLSStatus' in self.code:
            self.code = '#include "MrServers/MrMeasSrv/MeasUtils/NLSStatus.h"\n' + self.code

        if 'SeqRunKernel' in self.code:
            self.code = '#include "MrServers/MrImaging/libSBB/SeqRunKernel.h"\n' + self.code
        elif 'NLS_STATUS' in self.code:
            self.code = '#include "MrServers/MrMeasSrv/MeasUtils/nlsmac.h"\n' + self.code

if __name__ == '__main__':

    # Desired pulse sequence iterface
    ps = PulseSequence('MyFirstSeq')

    # ps.add_grad(ss_waveform)
    # ps.add_rf(rf_waveform)
    # ps.add_grad(fe_waveform)
    # ps.add_grad(pe_waveform)
    # ps.add_adc(adc_waveform)

    code = ps.compile()
    print(code)
