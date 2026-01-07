import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    data_counter = Counter(x)
    mean = np.mean(x)
    median = np.median(x)
    mode = data_counter.most_common(1)[0][0]
    return (mean, median, mode)

