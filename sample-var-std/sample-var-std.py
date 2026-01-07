import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    data = np.asarray(x)
    mean = np.mean(data)
    n = len(data)
    variance = np.sum((data-mean)**2 / (n-1))
    std = np.sqrt(variance)
    return (variance,std)
