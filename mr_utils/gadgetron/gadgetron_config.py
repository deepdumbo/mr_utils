## IDEA: programmatically generate local configurations so reconstruction
# pipelines can be created in the script, modified conditionally, etc...

import xml.etree.cElementTree as ET
from tempfile import NamedTemporaryFile

class GadgetronConfig(object):

    def __init__(self):
        self.get_stream_config()
        # self.filename = None

    def get_stream_config(self):
        '''
        <gadgetronStreamConfiguration
          xsi:schemaLocation="http://gadgetron.sf.net/gadgetron gadgetron.xsd"
          xmlns="http://gadgetron.sf.net/gadgetron"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        '''
        self.gadgetronStreamConfiguration = ET.Element('gadgetronStreamConfiguration')
        self.gadgetronStreamConfiguration.set('xmlns',"http://gadgetron.sf.net/gadgetron")
        self.gadgetronStreamConfiguration.set('xsi:schemaLocation',"http://gadgetron.sf.net/gadgetron gadgetron.xsd")
        self.gadgetronStreamConfiguration.set('xmlns:xsi',"http://www.w3.org/2001/XMLSchema-instance")

    def add_reader(self,slot,classname,dll='gadgetron_mricore'):
        '''
        <reader>
          <slot>1008</slot>
          <dll>gadgetroncore</dll>
          <classname>GadgetIsmrmrdAcquisitionMessageReader</classname>
        </reader>
        '''
        reader = ET.SubElement(self.gadgetronStreamConfiguration,'reader')
        slot_el = ET.SubElement(reader,'slot')
        slot_el.text = str(slot)
        dll_el = ET.SubElement(reader,'dll')
        dll_el.text = dll
        classname_el = ET.SubElement(reader,'classname')
        classname_el.text = classname

    def add_writer(self,slot,classname,dll='gadgetron_mricore'):
        '''
        <writer>
          <slot>1004</slot>
          <dll>gadgetroncore</dll>
          <classname>MRIImageWriterCPLX</classname>
        </writer>
        '''
        writer = ET.SubElement(self.gadgetronStreamConfiguration,'writer')
        slot_el = ET.SubElement(writer,'slot')
        slot_el.text = str(slot)
        dll_el = ET.SubElement(writer,'dll')
        dll_el.text = dll
        classname_el = ET.SubElement(writer,'classname')
        classname_el.text = classname

    def add_gadget(self,name,classname=None,dll=None,props=[]):
        '''
        <gadget>
          <name>Acc</name>
          <dll>gadgetroncore</dll>
          <classname>AccumulatorGadget</classname>
        </gadget>
        '''

        if classname is None:
            classname = '%sGadget' % name

        gadget = ET.SubElement(self.gadgetronStreamConfiguration,'gadget')
        name_el = ET.SubElement(gadget,'name')
        name_el.text = name

        # Let's try to be smart about the dlls...
        dll_el = ET.SubElement(gadget,'dll')
        if dll is None:
            if 'grappa' in name.lower():
                dll_el.text = 'gadgetron_grappa'
            elif 'epi' in name.lower() or 'epi' in classname.lower():
                dll_el.text = 'gadgetron_epi'
            elif 'gtplus' in name.lower() or 'gtplus' in classname.lower():
                dll_el.text = 'gadgetronPlus'
            else:
                dll_el.text = 'gadgetron_mricore'
        else:
            dll_el.text = dll


        classname_el = ET.SubElement(gadget,'classname')
        classname_el.text = classname

        for prop in props:
            prop_el = ET.SubElement(gadget,'property')
            name_el = ET.SubElement(prop_el,'name')
            name_el.text = prop[0]
            value_el = ET.SubElement(prop_el,'value')
            value_el.text = prop[1]

    def print(self):
        val = self.tostring()
        print(val)

    def tostring(self):
        val = ET.tostring(self.gadgetronStreamConfiguration,encoding='utf-8',method='xml').decode('utf-8')
        return(val)

    # def get_filename(self):
    #     '''Create a temporary file and hand back the filename.'''
    #
    #     if self.filename is None:
    #         self.filename = NamedTemporaryFile().name
    #     return(self.filename)

if __name__ == '__main__':
    pass
