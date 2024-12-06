"""QEncode: standard computation"""

from sympy import symbols  # type: ignore
from sympy.utilities.lambdify import implemented_function  # type: ignore

delta_std = implemented_function("d", lambda v, alpha: 1 if v == alpha else 0)


def build_std_vars(n_vars: int):
    return [symbols(f"v_{i}") for i in range(n_vars)]  # variable v_i for node i
