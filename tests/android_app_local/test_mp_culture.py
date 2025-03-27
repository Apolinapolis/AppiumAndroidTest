from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search():
    with step('skipping onboarding'):
        browser.element((AppiumBy.ID, 'ru.gosuslugi.culture.test:id/root')).click()
        browser.element((AppiumBy.ID, 'ru.gosuslugi.culture.test:id/root')).click()
        browser.element((AppiumBy.ID, 'ru.gosuslugi.culture.test:id/root')).click()
        browser.element((AppiumBy.ID, 'ru.gosuslugi.culture.test:id/root')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.Button')).click()
        browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.Button')).click()
        browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_one_time_button')).click()
        browser.element((AppiumBy.ID, 'ru.gosuslugi.culture.test:id/fbb_iv_close')).click()

    with step('check list popular'):
        results = browser.all((AppiumBy.ID, 'ru.gosuslugi.culture.test:id/ipl_tv_title'))
        results.first.should(have.text('Пушкинские премьеры'))