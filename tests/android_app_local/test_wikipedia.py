from time import sleep

from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search():
    with step('skipping onboarding'):
        SuccessOnboardingFlow()
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
        sleep(4)




    # with step('Type search'):
    #     browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    #     browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')
    #
    # with step('Verify content found'):
    #     results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
    #     results.should(have.size_greater_than(0))
    #     results.first.should(have.text('Appium'))
