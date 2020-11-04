"""Test functions for fooof.analysis.error."""

from fooof.analysis.error import *

###################################################################################################
###################################################################################################

def test_compute_pointwise_error_fm(tfm):

    errs = compute_pointwise_error_fm(tfm, False, True)
    assert np.all(errs)

def test_compute_pointwise_error_fm_plt(tfm, skip_if_no_mpl):
    """Run a separate test to run with plot pass-through."""

    compute_pointwise_error_fm(tfm, True, False)

def test_compute_pointwise_error_fg(tfg):

    errs = compute_pointwise_error_fg(tfg, False, True)
    assert np.all(errs)

def test_compute_pointwise_error_fg_plt(tfg, skip_if_no_mpl):
    """Run a separate test to run with plot pass-through."""

    compute_pointwise_error_fg(tfg, True, False)

def test_compute_pointwise_error():

    d1 = np.ones(5) * 2
    d2 = np.ones(5)

    errs = compute_pointwise_error(d1, d2)
    assert np.array_equal(errs, np.array([1, 1, 1, 1, 1]))

def test_compute_mae_error():

    data = np.array([2, 4, 6])
    model = np.array([3, 6, 9])

    mae = compute_mae_error(model, data)
    assert mae == 2.0
