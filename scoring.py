import numpy as np

def score(lag, req):
    gain = np.dot(req.T, lag)

    