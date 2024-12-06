"""QEncode: TSP cost function"""

from typing import Any, Callable

from sympy import Mul, simplify  # type: ignore

Delta = Callable[[int, int | list], Any] | Any


def build_cost_function(data: list[list[int]], vars: list, apply_delta: Delta) -> Any:

    n_nodes = len(data)

    # Encode the cost function
    cost_terms = 0
    for alpha in range(1, n_nodes):
        for i in range(n_nodes):
            for j in range(n_nodes):
                if j > i:
                    delta_first = Mul(
                        apply_delta(alpha, vars[i]), apply_delta(alpha + 1, vars[j])
                    )
                    delta_second = Mul(
                        apply_delta(alpha, vars[j]), apply_delta(alpha + 1, vars[i])
                    )
                    cost_terms += Mul(data[i][j], (delta_first + delta_second))

    cost_function = simplify(cost_terms)

    return cost_function
