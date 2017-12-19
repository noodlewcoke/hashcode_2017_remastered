import numpy as np
from scipy.sparse import csr_matrix, csc_matrix, lil_matrix
from sys import getsizeof

a = np.random.uniform(size = (10000, 1000)).astype(np.float32)
#VxC matrix => (10K, K)

b = np.random.uniform(size = (1000, 1000)).astype(np.float32)
#ExC matrix => (K, K)

a_sparse = csc_matrix((a>0.98)*3)
b_sparse = csr_matrix((b<0.02)*2)

c = lil_matrix((a_sparse.shape[1], a_sparse.shape[0]))
#ExV matrix => (K, 10K)

#Is csr logical??? maybe csc try it as well

for r_index in range(b_sparse.shape[0]):
    d = (a_sparse.multiply(b_sparse.getrow(r_index))).max(axis=1)
    # d = csc_matrix(d)
    # c[r_index, :] = np.squeeze(d.todense())
    c[0] += d
    


