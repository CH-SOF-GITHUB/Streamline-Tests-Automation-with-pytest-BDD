import pytest
from pytest_bdd import given, when, then, scenarios

from Tests.resources.cucumbers import CucumberBasket

scenarios('../Tests/features/cuke_basket.feature')


@pytest.fixture(scope='module')
def basket():
    return CucumberBasket(initial_count=0, max_count=10)


@given("the basket has 2 cucumbers")
def step_impl(basket):
    basket.add(2)


@when("4 cucumbers are added to the basket")
def step_impl(basket):
    basket.add(4)


@then("the basket contains 6 cucumbers")
def step_impl(basket):
    assert basket.count == 6
