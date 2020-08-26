import os
import numpy as np
from scipy.io import loadmat


def load_file(file, max_size=100):
    """Load spectra from a file.

    Parameters
    ----------
    file : str
        The path to a .npy, .csv, or .mat file contain a spectrum or spectra.
    max_size: int, optional, default: 100
        The maximum file size, in mb, that is allowed.

    Returns
    -------
    spectrum : np.array
        The power spectrum read from a given file.
    """

    size_mb = os.path.getsize(file) * 1e-6

    if size_mb > 500:
        raise ValueError('File size cannot exceed 500mb.')

    if file.endswith('.npy'):
        array = np.load(file, allow_pickle=False)
    elif file.endswith('.csv'):
        array = np.genfromtxt(file, delimiter=',', dtype=float)
    elif file.endswith('.mat'):
        array = loadmat(file)
    else:
        raise ValueError('File type must be .npy, .csv, or .mat.')

    if array.ndim != 1 and array.ndim != 2:
        raise ValueError('File does not contain a 1D or 2D array.')

    return array
