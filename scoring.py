import numpy as np
from scipy.sparse import csr_matrix, csc_matrix, lil_matrix
from sys import getsizeof


def time_analysis(func):
    import time
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        print(func.__name__,time.time()-start, "sn")
        return result
    return wrapper


def fitness_generator(lag_diff, request):
    lag_diff = csr_matrix(lag_diff)
    request = csr_matrix(request)

    #@time_analysis
    def scoring(cache):
        gain = np.empty(request.shape)
        cache = csc_matrix(cache)
        for r_index in range(lag_diff.shape[0]):
            d = (cache.multiply(lag_diff.getrow(r_index))).max(axis=1)
            gain[r_index] = np.squeeze(d.todense())
        gain = csr_matrix(gain)
        return int(gain.multiply(request).sum()*1000/request.sum())
    return scoring

#@time_analysis
def translation(prob_matrix, cache_size, video_sizes):
    prob_matrix = prob_matrix.copy()
    cache_size = np.ones(prob_matrix.shape[1])*cache_size
    trans_matrix = np.zeros_like(prob_matrix)
    col_indices = np.arange(trans_matrix.shape[1]).astype(np.int32)
    for i in range(25):
        max_indices = np.argmax(prob_matrix, axis=0)
        selected_video_size = video_sizes[max_indices]
        chosen_indices = cache_size >= selected_video_size
        cache_size -= video_sizes[max_indices]*chosen_indices
        trans_matrix[max_indices, col_indices] = chosen_indices
        prob_matrix[max_indices, col_indices] = 0
    return trans_matrix

    

if __name__ == "__main__":
    p_mat = np.random.normal(size=(10000,1000))
    c_s = np.random.randint(low=40, high=100, size=1000)
    v_s = np.random.randint(low=5, high=20, size=10000)
    t_m = translation(p_mat, c_s, v_s)
    print(csr_matrix(t_m))
    
