import pytest
from pytest_bdd import given, scenarios, when, then, parsers

from Tests.resources.cucumbers import CucumberBasket

# scenarios
scenarios('../Tests/features/parametrized_cuke_basket.feature')


# fixtures
@pytest.fixture(scope='module')
def basket():
    b = CucumberBasket(initial_count=0, max_count=10)
    return b


@given(parsers.parse('the basket has "{initial:d}" cucumbers'))
def step_impl(basket, initial):
    basket.count = initial


@when(parsers.parse('"{some:d}" cucumbers are added to the basket'))
def step_impl(basket, some):
    basket.add(some)


@then(parsers.parse('the basket contains "{total:d}" cucumbers'))
def step_impl(basket, total):
    assert basket.count == total
