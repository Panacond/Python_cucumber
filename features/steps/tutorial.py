from behave import *

@given('we have behave installed')
def step_impl(context):
    print("1")

@when('we implement a test')
def step_impl(context):
    print("2")

@then('behave will test it for us!')
def step_impl(context):
    print("3")
    b = True
    assert b