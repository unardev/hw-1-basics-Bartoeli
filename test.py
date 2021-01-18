import unittest
from main import sum_list, get_first_and_last, check_parity, solve_quadratic_equation


class TestSum(unittest.TestCase):
    def test_sum_list(self):
        self.assertEqual(sum_list([1, 2, 3]), 8)
        self.assertEqual(sum_list([200, 300, 400]), 1100)
        self.assertEqual(sum_list([-1, -351, 444444]), 888537)
        self.assertEqual(sum_list([100000, 23456781, 999999999999]), 2000023456779)

    def test_check_parity(self):
        self.assertEqual(check_parity(2), True)
        self.assertEqual(check_parity(3), False)
        self.assertEqual(check_parity(0), True)
        self.assertEqual(check_parity(2222222222222221), False)

    def test_get_first_and_last(self):
        self.assertEqual(get_first_and_last([1, 2, 3]), [1, 3])
        self.assertEqual(get_first_and_last([200, 300, 400]), [200, 400])
        self.assertEqual(get_first_and_last([-1, -351, 444444]), [-1, 444444])
        self.assertEqual(get_first_and_last([0]), [])

    def test_solve_quadratic_equation(self):
        self.assertEqual(solve_quadratic_equation(1, 2, 1), (-1.0, -1.0))
        self.assertEqual(solve_quadratic_equation(2, 3, -1), (0.281, -1.781))
        self.assertEqual(solve_quadratic_equation(2, 3, -1), (0.281, -1.781))
        self.assertEqual(solve_quadratic_equation(12, -9.6, 1.44), (0.600, 0.200))


if __name__ == '__main__':
    unittest.main()
