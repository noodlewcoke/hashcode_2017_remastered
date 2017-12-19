from __future__ import print_function
import numpy as np
import sys



def get_matricies(file_loc):
    with open(file_loc) as f:
        all_lines = f.readlines()

    v, e, nr_of_req, c, size_c = map(int, all_lines[0].split("\n")[0].split())
    size_video = map(int, all_lines[1].split("\n")[0].split())

    lag_diff_matrix = np.zeros((e, c), dtype=np.int32)
    req_mat = np.zeros((e, v), dtype=np.int32)

    index = 2
    for endpoint_id in range(e):
        dl_lag, connected_caches = map(int, all_lines[index].split("\n")[0].split())
        index+=1
        for cache in range(connected_caches):
            init_cache_id, lag = map(int, all_lines[index+cache].split("\n")[0].split())
            lag_diff_matrix[endpoint_id, init_cache_id] = dl_lag - lag
        index += cache+1


    for request in range(nr_of_req):
        vid, ep_id, nr_req = map(int, all_lines[index].split("\n")[0].split())
        req_mat[ep_id, vid] += nr_req
        index+=1

    return lag_diff_matrix, req_mat

if __name__ == "__main__":
    file_loc = sys.argv[1]
    lags, reqs = get_matricies(file_loc)
    print(lags.shape, reqs.shape)