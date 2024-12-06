"""QEncode: one-hot encoding"""

from sympy import symbols  # type: ignore


def build_one_hot_variables(n_vars: int) -> list:
    """Builds a list of one-hot variables for a given number of variables.

    Parameters
    ----------
    n_vars : int
        The number of variables to generate one-hot variables for.

    Returns
    -------
    list
        A list of lists, where each sublist contains one-hot variables for a variable.
    """
    n_bits = n_vars

    return [
        [
            symbols(f"x_{i}_{b}")  # One-hot variable x_i_b for variable i, bit b
            for b in range(n_bits)
        ]
        for i in range(n_vars)
    ]


def apply_one_hot_delta(alpha: int, v: list):
    """Encodes the delta function delta(v_i = alpha) in binary encoding

    Parameters
    ----------
    alpha : int
        alpha value
    v : list
        List of variables

    Returns
    -------
    Any
        Selected variable
    """
    return v[alpha - 1]
