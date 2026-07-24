from django.test import SimpleTestCase

from methods.methods.NonLinearEquationsMethods import NonLinearEquationsMethods
from methods.utils.ResponseManager import ResponseManager


class ResponseManagerTests(SimpleTestCase):
    def test_warning_response_includes_headers(self):
        response = ResponseManager.warning_response([[0, 1]], "Limit reached", ["Iteration", "x"])

        self.assertEqual(response["status"], "warning")
        self.assertEqual(response["table_headers"], ["Iteration", "x"])


class BisectionMethodTests(SimpleTestCase):
    def test_bisection_returns_an_endpoint_root(self):
        response = NonLinearEquationsMethods.bisection(
            2.0,
            8.0,
            lambda x: x * x - 4,
            tolerance=5e-5,
            iterations_limit=10,
        )

        self.assertEqual(response["status"], "success")
        self.assertEqual(response["table"][-1][3], 2.0)


class FalsePositionMethodTests(SimpleTestCase):
    def test_false_position_reports_an_invalid_interval_without_crashing(self):
        response = NonLinearEquationsMethods.false_position(
            -3.0, 3.0, lambda x: x * x - 4, tolerance=5e-5, iterations_limit=100
        )

        self.assertEqual(response["status"], "error")
        self.assertIn("opposite signs", response["message"])

    def test_false_position_converges_for_a_bracketing_interval(self):
        response = NonLinearEquationsMethods.false_position(
            -3.0, 0.0, lambda x: x * x - 4, tolerance=5e-5, iterations_limit=100
        )

        self.assertEqual(response["status"], "success")
        self.assertAlmostEqual(response["table"][-1][3], -2.0, places=3)


class FixedPointMethodTests(SimpleTestCase):
    def test_divergent_iteration_returns_an_actionable_error(self):
        response = NonLinearEquationsMethods.fixed_point(
            lambda x: x * x - 4,
            initial_guess=-3.0,
            tolerance=5e-5,
            iterations_limit=100,
        )

        self.assertEqual(response["status"], "error")
        self.assertIn("diverged", response["message"])
