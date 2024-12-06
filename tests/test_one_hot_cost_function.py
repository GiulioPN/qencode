import unittest

from sympy import lambdify  # type: ignore

from qencode.encodings.one_hot import apply_one_hot_delta, build_one_hot_variables
from qencode.tsp.cost_function import build_cost_function


class TestCostFunctionOneHot(unittest.TestCase):

    def test_cost_function_3d(self):
        matrix = [[0, 2, 3], [2, 0, 1], [3, 1, 0]]

        vars = build_one_hot_variables(len(matrix))

        cost_function = build_cost_function(matrix, vars, apply_one_hot_delta)

        v = {vars[i][b] for b in range(len(vars[0])) for i in range(len(vars))}

        f = lambdify(v, cost_function, "numpy")

        p_123 = f(
            x_0_0=0,
            x_0_1=0,
            x_0_2=1,
            x_1_0=0,
            x_1_1=1,
            x_1_2=0,
            x_2_0=1,
            x_2_1=0,
            x_2_2=0,
        )
        self.assertEqual(p_123, 3)

        p_132 = f(
            x_0_0=0,
            x_0_1=0,
            x_0_2=1,
            x_1_0=1,
            x_1_1=0,
            x_1_2=0,
            x_2_0=0,
            x_2_1=1,
            x_2_2=0,
        )
        self.assertEqual(p_132, 4)

        f3 = f(
            x_0_0=0,
            x_0_1=1,
            x_0_2=0,
            x_1_0=0,
            x_1_1=0,
            x_1_2=1,
            x_2_0=1,
            x_2_1=0,
            x_2_2=0,
        )
        self.assertEqual(f3, 5)

        p_231 = f(
            x_0_0=0,
            x_0_1=1,
            x_0_2=0,
            x_1_0=1,
            x_1_1=0,
            x_1_2=0,
            x_2_0=0,
            x_2_1=0,
            x_2_2=1,
        )
        self.assertEqual(p_231, 5)

        p_321 = f(
            x_0_0=1,
            x_0_1=0,
            x_0_2=0,
            x_1_0=0,
            x_1_1=1,
            x_1_2=0,
            x_2_0=0,
            x_2_1=0,
            x_2_2=1,
        )
        self.assertEqual(p_321, 3)

        p_312 = f(
            x_0_0=1,
            x_0_1=0,
            x_0_2=0,
            x_1_0=0,
            x_1_1=0,
            x_1_2=1,
            x_2_0=0,
            x_2_1=1,
            x_2_2=0,
        )
        self.assertEqual(p_312, 4)


if __name__ == "__main__":
    unittest.main()
