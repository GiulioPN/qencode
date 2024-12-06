import unittest

from sympy import lambdify  # type: ignore

from qencode.encodings.binary import apply_binary_delta, build_binary_variables
from qencode.tsp.cost_function import build_cost_function


class TestCostFunctionBinary(unittest.TestCase):

    def test_cost_function_3d(self):
        matrix = [[0, 2, 3], [2, 0, 1], [3, 1, 0]]

        vars = build_binary_variables(len(matrix))

        cost_function = build_cost_function(matrix, vars, apply_binary_delta)

        v = {vars[i][b] for b in range(len(vars[0])) for i in range(len(vars))}

        f = lambdify(v, cost_function, "numpy")

        f1 = f(x_0_0=0, x_0_1=0, x_1_0=1, x_1_1=0, x_2_0=0, x_2_1=1)
        self.assertEqual(f1, 3)

        f2 = f(x_0_0=0, x_0_1=0, x_1_0=0, x_1_1=1, x_2_0=1, x_2_1=0)
        self.assertEqual(f2, 4)

        f3 = f(x_0_0=1, x_0_1=0, x_1_0=0, x_1_1=0, x_2_0=0, x_2_1=1)
        self.assertEqual(f3, 5)

        f4 = f(x_0_0=1, x_0_1=0, x_1_0=0, x_1_1=1, x_2_0=0, x_2_1=0)
        self.assertEqual(f4, 5)

        f5 = f(x_0_0=0, x_0_1=1, x_1_0=1, x_1_1=0, x_2_0=0, x_2_1=0)
        self.assertEqual(f5, 3)

        f6 = f(x_0_0=0, x_0_1=1, x_1_0=0, x_1_1=0, x_2_0=1, x_2_1=0)
        self.assertEqual(f6, 4)


if __name__ == "__main__":
    unittest.main()
