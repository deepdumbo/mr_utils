import numpy as np
from mr_utils import view

def sort2d_loop(A):
    '''An efficient selection sorting algorithm for two-dimensional arrays.

    Implementation of algorithm from:
        Zhou, M., & Wang, H. (2010, December). An efficient selection sorting
        algorithm for two-dimensional arrays. In Genetic and Evolutionary
        Computing (ICGEC), 2010 Fourth International Conference on
        (pp. 853-855). IEEE.
    '''

    # (1) Sort each row by selection sorting, (assume elements are sorted in
    # descending order)
    A = -np.sort(-A,axis=1)

    # (2) Initialize B by specifying index values of element (row, col) as
    # row=1, col=1
    B = np.zeros(A.shape)

    # (3) Find the maximum element from the first column, and move it to
    # B(row,col), then the moved element’s successor will be the first element
    # in the row.
    A_flat = A.flatten('F').astype(float)
    for ii in range(A.shape[0]):
        for jj in range(A.shape[1]):
            # Note that the first column will always be the 1st A.shape[0]
            # elements of the reduced Fortran-flattened array.  This is not
            # clear in the paper...
            first_col = A_flat[:A.shape[0]]
            idx = np.argmax(first_col)
            B[ii,jj] = first_col[idx]
            A_flat = np.delete(A_flat,idx)

    return(B)

def sort2d(A):
    # Get the indices
    idx0 = np.arange(A.size).reshape(A.shape)
    idx1 = idx0[np.arange(A.shape[0])[:,None],np.argsort(-A,axis=1)]
    idx2 = idx1.flatten('F')
    idx3 = idx2.take(np.argsort(np.sort(-A,axis=1).flatten('F')),axis=0)
    idx4 = idx3.reshape(A.shape,order='C')

    # Tread carefully...
    # val0 = -A.take(idx2)
    # assert np.allclose(np.sort(-A,axis=1).flatten('F'),val0)
    #
    # val1 = A.take(idx3)
    # assert np.allclose(-np.sort(np.sort(-A,axis=1).flatten('F'),axis=0),val1)
    #
    # val2 = A.take(idx4)
    # assert np.allclose(np.reshape(-np.sort(np.sort(-A,axis=1).flatten('F'),axis=0),A.shape,order='C'),val2)

    val = np.reshape(-np.sort(np.sort(-A,axis=1).flatten('F'),axis=0),A.shape,order='C')
    return(val,idx4)

if __name__ == '__main__':

    A = np.array([ [3,4,6],[7,2,8],[1,9,5] ])

    B = sort2d_loop(A)
    C,idx = sort2d(A)

    print(A)
    print(B)
    print(C)

    assert np.allclose(B,C)
