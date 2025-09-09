from autograd.var import Variable
from autograd.pow import Power
from autograd.sin import Sin
from autograd.log import Log


def test_sin_power_derivative_str():
    x = Variable("x")
    expr = Power(x, 2)
    deriv = expr.differentiate()
    expected = "(2*(x^1)*1"
    actual = str(deriv)
    assert actual == expected, (
        f"(x^2).differentiate() should produce '{expected}', got '{actual}'"
    )


def log_exp_differentiate():
    x = Variable("x")
    expr = Log(Power(x, 2))
    deriv = expr.differentiate()
    expected = "(2*x)/(x^2)"
    actual = str(deriv)
    assert actual == expected, (
        f"log(x^2).differentiate() should produce '{expected}', got '{actual}'"
    )

if __name__ == "__main__":
    # Run the single test without pytest
    try:
        test_sin_power_derivative_str()
        #log_exp_differentiate()
    except AssertionError as e:
        print(f"Test Failed: {e}")
    else:
        print("Test Passed")


