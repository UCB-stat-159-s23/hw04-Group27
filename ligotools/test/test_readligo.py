''' testing the examples given in the readligo.py description'''

import numpy as np
from ligotools import readligo as rl
    

def test_example_zero():
    ''' Test return types from Example 0 for general file
    '''
    strain, time, dq = rl.loaddata('hw04-Group27/data/H-H1_LOSC_4_V1-842653696-4096.hdf5', 'H1')
    assert strain is None
    assert time is None
    assert dq is None
    
    
def test_example_one():
    ''' Test return types from Example 1
    '''
    segList = rl.getsegs(842657792, 842658792, 'H1')
    
    for (start, stop) in segList:
        segList_test(segList)
        strain, meta, dq = rl.getstrain(start, stop, 'H1')
        loaddata_test(strain, meta, dq)
        

def test_example_two():
    ''' Test return types from Example 2, 
        when fileList is specified
    '''
    filelist = rl.FileList(directory='hw04-Group27/data')
    segList = rl.getsegs(842657792, 842658792, 'H1', filelist=filelist)
    
    for start, stop in segList: 
        segList_test(segList)
        strain, meta, dq = rl.getstrain(start, stop, 'H1', filelist=filelist)
        loaddata_test(strain, meta, dq)
    

def test_hdf5():
    ''' Short test for helper .read_hdf5()
    '''
    
    strain, _, _, _, _, _, _ = rl.read_hdf5('data/H-H1_LOSC_4_V2-1126259446-32.hdf5')
    assert len(strain) != 0
    

    
def loaddata_test(strain, time, dq):
    ''' Helper function to test data types from loaddata(),
        when tvec = True 
    '''
    assert isinstance(strain, dict)
    assert isinstance(time, np.ndarray)
    assert isinstance(dq, dict)
    

def segList_test(start, stop):
    ''' Helper function to test data types and size from getsegs()
    '''
    assert stop == 842657792
    assert start == 842658792