def bursty_none_logL(p,x):
    """Compute the log-likelihood of data microstates.

    Parameters
    ----------
    p: np.ndarray
        log10 biological parameters.
    x: int np.ndarray
        microstates in the experimental data histogram, a Nstates x 2 array.

    Returns
    -------
    log_proposal: float np.ndarray
        The log-likelihood of each state in Nstates.
    """

    raise ValueError('Not yet implemented!')

def bursty_none_grid(p,lm):
    """Evaluate the PMF of the model over a grid at a set of parameters.

    Parameters
    ----------
    p: np.ndarray
        log10 biological parameters.
    limits: list of int
        grid size for PMF evaluation, size n_species.


    Returns
    -------
    Pss: np.ndarray
        the steady-state model PMF over a grid (0,...,limits[0]-1) x (0,...,limits[1]-1).
    """

    raise ValueError('Not yet implemented!')