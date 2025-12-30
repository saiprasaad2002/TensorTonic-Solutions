import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    array_data = np.asarray(x)
    return np.where(array_data>=0, array_data, array_data*alpha)