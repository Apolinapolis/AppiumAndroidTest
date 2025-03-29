import os
import allure
import pytest
import allure_commons
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene import browser, support
from selene_in_action.utils.file import abs_path_from_project


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    apk_path = abs_path_from_project('app-gms-release_test.2.19.0.1414.apk')

    options = UiAutomator2Options().load_capabilities({
        'deviceName': 'R58R33ANL0T',
        'app': apk_path
    })


    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            'http://127.0.0.1:4723',
            options=options
        )

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )

    allure.attach(
        browser.driver.page_source,
        name='screen xml dump',
        attachment_type=allure.attachment_type.XML,
    )


    with allure.step('tear down app session'):
        browser.quit()