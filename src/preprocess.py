#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Apply data normalization and dimension reduction to a data cube
 and prepare it to be fed into the PyGMMis
"""

import numpy as np

def normalize(data, fit_params):
    """Receives a NxM ndarray and applies some normalization method to it"""
    # update this to match-case? Does require Python 3.10 or later
    method = fit_params['norm_method']

    if method == 'none':
        return data


def reduce_dimensions(hdul, fit_params):
    """Receives a HDUL and applies some dimensionality reduction algorithm to it.
    Returns an NxM numpy array where N is the number of data points and M the number of features"""

    # Update this to match-case? Requires Python 3.10 or later
    method = fit_params['reduce_method']
    N = hdul[0].data.shape[1] * hdul[0].data.shape[2]
    M = hdul[0].data.shape[0]

    if method == 'none':
        return np.reshape(hdul[0].data, (N, M))  # TODO: Check all of these values