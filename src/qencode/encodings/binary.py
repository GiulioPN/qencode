"""QEncode: binary encoding"""

from typing import Any

from sympy import symbols  # type: ignore


def build_binary_variables(n_vars: int) -> list:
    """Builds a list of binary variables for a given number of variables.

    Parameters
    ----------
    n_vars : int
        Number of variables

    Returns
    -------
    list
        List of binary variables: x_i_b for variable i, bit b
    """
    n_bits = (n_vars - 1).bit_length()  # log2(n_nodes) rounded up

    return [
        [
            symbols(f"x_{i}_{b}")  # Binary variable x_i_b variable i, bit b
            for b in range(n_bits)
        ]
        for i in range(n_vars)
    ]


def apply_binary_delta(alpha: int, v: list) -> Any:
    """Encodes the delta function delta(v_i = alpha) in binary encoding.

    Parameters
    ----------
    alpha : int
        Alpha value
    v : list
        List of variables

    Returns
    -------
    Any
        Expression
    """
    n_bits = len(v)

    alpha_bits = [
        ((alpha - 1) >> b) & 1 for b in range(n_bits)
    ]  # Extract alpha's binary bits

    prod = 1
    for i in range(n_bits):
        prod *= v[i] * (2 * alpha_bits[i] - 1) - alpha_bits[i] + 1

    return prod
