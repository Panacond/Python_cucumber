from behave import *
from features.environment import BaseTest


# 1 scenario
@given('User opens homePage page')
def step_impl(context):
    BaseTest.get_home_page(context)


@when('User clicks news button')
def step_impl(context):
    home_page = BaseTest.get_home_page(context)
    home_page.go_news_page()


@Then('User check news list items visibility')
def step_impl(context):
    news_page = BaseTest.get_news_page(context)
    news_page.implicitly_wait(BaseTest.DEFAULT_TIMEOUT)
    news_page.is_element_news_visible()


# 2 scenario
@when('User makes search by keyword {text}')
def step_impl(context, text):
    home_page = BaseTest.get_home_page(context)
    home_page.input_field_search(text)


@when('User clicks Search button')
def step_impl(context):
    home_page = BaseTest.get_home_page(context)
    home_page.click_button_search()


@Then('User checks that each item in results list contains keyword "{text}" visible')
def step_impl(context, text):
    search_page = BaseTest.get_search_page(context)
    list_title = search_page.get_search_result_title()
    expected = False
    for element in list_title:
        if text in element.text:
            expected = True
    assert expected


# 3 scenario
@given('User clicks Xiaomi button')
def step_impl(context):
    home_page = BaseTest.get_home_page(context)
    home_page.click_button_xiaomi()


@given('User clicks Vacuum cleaners button')
def step_impl(context):
    xiaomi_page = BaseTest.get_xiaomi_page(context)
    xiaomi_page.click_button_vacuum_cleaners()


@when('User clicks Price button')
def step_impl(context):
    xiaomi_vacuum_cleaners_page = BaseTest.get_xiaomi_vacuum_cleaners_page(context)
    xiaomi_vacuum_cleaners_page.click_button_price()


@when('User selects a price range 150-350')
def step_impl(context):
    xiaomi_vacuum_cleaners_page = BaseTest.get_xiaomi_vacuum_cleaners_page(context)
    xiaomi_vacuum_cleaners_page.click_select_price_range150_350()


@Then('User checks prices in the range 150-350 {designations}')
def step_impl(context, designations):
    xiaomi_vacuum_cleaners_page = BaseTest.get_xiaomi_vacuum_cleaners_page(context)
    list_price = xiaomi_vacuum_cleaners_page.get_list_check_prise()
    expected = True
    for element in list_price:
        correct_text = element.text.replace(designations, "")
        correct_text = correct_text.split(" to ")[0]
        price_value = float(correct_text)
        if price_value < 150:
            expected = False
        elif price_value > 350:
            expected = False
    assert expected


# 4 scenario
@when('User clicks View button')
def step_impl(context):
    xiaomi_vacuum_cleaners_page = BaseTest.get_xiaomi_vacuum_cleaners_page(context)
    xiaomi_vacuum_cleaners_page.implicitly_wait(BaseTest.DEFAULT_TIMEOUT)
    xiaomi_vacuum_cleaners_page.click_button_view()


@when('User clicks List view button')
def step_impl(context):
    xiaomi_vacuum_cleaners_page = BaseTest.get_xiaomi_vacuum_cleaners_page(context)
    xiaomi_vacuum_cleaners_page.click_button_view_list()


@Then('User check view change a list of items visibility')
def step_impl(context):
    xiaomi_vacuum_cleaners_page = BaseTest.get_xiaomi_vacuum_cleaners_page(context)
    xiaomi_vacuum_cleaners_page.is_element_view_list_visible()


# 5 scenario
@given('User clicks first list item')
def step_impl(context):
    xiaomi_vacuum_cleaners_page = BaseTest.get_xiaomi_vacuum_cleaners_page(context)
    xiaomi_vacuum_cleaners_page.implicitly_wait(BaseTest.DEFAULT_TIMEOUT)
    xiaomi_vacuum_cleaners_page.click_first_element_list()


@given('User clicks Add to Watchlist button')
def step_impl(context):
    product_page = BaseTest.get_product_page(context)
    product_page.input_field_number_product(BaseTest.DEFAULT_TIMEOUT)
    product_page.click_button_add_to_watchlist()


@when('User types {user_name} in input field')
def step_impl(context, user_name):
    login_page = BaseTest.get_login_page(context)
    login_page.implicitly_wait(BaseTest.DEFAULT_TIMEOUT)
    login_page.input_field_user_name(user_name)


@when('User clicks Continue button')
def step_impl(context):
    login_page = BaseTest.get_login_page(context)
    login_page.click_button_continue()


@Then('User checks Error message')
def step_impl(context):
    login_page = BaseTest.get_login_page(context)
    login_page.is_error_message_visible()


# 6 scenario
@Then('User checks that message No exact matches found visible')
def step_impl(context):
    search_page = BaseTest.get_search_page(context)
    search_page.is_no_exact_matches_message_visible()


# 7 scenario
@when('User clicks Quantity field')
def step_impl(context):
    product_page = BaseTest.get_product_page(context)
    product_page.click_field_number_product()


@when('User inputs value {number}')
def step_impl(context, number):
    product_page = BaseTest.get_product_page(context)
    product_page.input_field_number_product(number)


@Then('User checks message "Please enter quantity of 1 or more" visibility')
def step_impl(context):
    product_page = BaseTest.get_product_page(context)
    product_page.is_error_number_message()


# 8 scenario
@when('User in Vacuum cleaners page makes search by keyword {input_text} and presses ENTER')
def step_impl(context, input_text):
    xiaomi_vacuum_cleaners_page = BaseTest.get_xiaomi_vacuum_cleaners_page(context)
    xiaomi_vacuum_cleaners_page.input_search_field(input_text)


@Then('User checks list items contain {result_search} on Vacuum cleaners page')
def step_impl(context, result_search):
    xiaomi_vacuum_cleaners_page = BaseTest.get_xiaomi_vacuum_cleaners_page(context)
    list_title = xiaomi_vacuum_cleaners_page.get_list_result_title()
    expected = False
    for element in list_title:
        if result_search in element.text:
            expected = True
    assert expected


# 9 scenario
@when('User inputs text {input_price} in minimum price field')
def step_impl(context, input_price):
    search_page = BaseTest.get_search_page(context)
    search_page.set_minimum_price(input_price)


@Then('User checks that message "Please provide a valid price range" visible')
def step_impl(context):
    search_page = BaseTest.get_search_page(context)
    search_page.error_input_price_value()


# 10 scenario
@when('User clicks {related_search} select button')
def step_impl(context, related_search):
    search_page = BaseTest.get_search_page(context)
    search_page.set_related_search(related_search)


@Then('User checks that each item in results list contains keyword {result_search} visible')
def step_impl(context, result_search):
    search_page = BaseTest.get_search_page(context)
    list_title = search_page.get_search_result_title()
    expected = False
    for element in list_title:
        if result_search in element.text:
            expected = True
            break
    assert expected
