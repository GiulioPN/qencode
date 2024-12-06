import unittest

from sympy import lambdify  # type: ignore

from qencode.encodings.standard import build_std_vars, delta_std
from qencode.tsp.cost_function import build_cost_function


class TestCostFunctionStandard(unittest.TestCase):

    def test_cost_function_3d(self):
        matrix = [[0, 2, 3], [2, 0, 1], [3, 1, 0]]

        std_vars = build_std_vars(len(matrix))

        cost_function = build_cost_function(matrix, std_vars, delta_std)
        vars = {std_vars[i] for i in range(len(std_vars))}

        f = lambdify(vars, cost_function, "numpy")

        p_123 = f(v_0=1, v_1=2, v_2=3)
        self.assertEqual(p_123, 3)

        p_132 = f(v_0=1, v_1=3, v_2=2)
        self.assertEqual(p_132, 4)

        p_213 = f(v_0=2, v_1=1, v_2=3)
        self.assertEqual(p_213, 5)

        p_231 = f(v_0=2, v_1=3, v_2=1)
        self.assertEqual(p_231, 5)

        p_321 = f(v_0=3, v_1=2, v_2=1)
        self.assertEqual(p_321, 3)

        p312 = f(v_0=3, v_1=1, v_2=2)
        self.assertEqual(p312, 4)


if __name__ == "__main__":
    unittest.main()
