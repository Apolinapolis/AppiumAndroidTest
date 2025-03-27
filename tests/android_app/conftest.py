import os
import allure
import pytest
import config
import allure_commons
from appium.options.android import UiAutomator2Options
from selene import browser, support
from selene_in_action import utils
from appium import webdriver


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options()

    if config.device_name:
        options.set_capability('deviceName', config.device_name)

    if config.appWaitActivity:
        options.set_capability('appWaitActivity', config.appWaitActivity)

    options.set_capability('app', (
        config.app if (config.app.startswith('/') or config.run_on_bstack)
        else utils.file.abs_path_from_project(config.app)
    ))

    if config.run_on_bstack:
        options.set_capability(
            'bstack:options', {
                'projectName': 'First Python project',
                'buildName': 'browserstack-build-1',
                'sessionName': 'BStack first_test',
                'userName': config.bstack_userName,
                'accessKey': config.bstack_accessKey,
            }
        )


    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            'http://hub.browserstack.com/wd/hub',
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

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    if config.run_on_bstack:
        utils.allure.attach_bstack_video(session_id)