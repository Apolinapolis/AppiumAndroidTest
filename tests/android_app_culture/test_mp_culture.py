import logging
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be



logger = logging.getLogger(__name__)


class Locators:
    PROFILE_TAB = (AppiumBy.ID, 'ru.gosuslugi.culture.test:id/vcbn_ll_profile')
    PROFILE_BUTTONS = (AppiumBy.ID, 'ru.gosuslugi.culture.test:id/vsc_tv_title')
    FAVORITE_TAB = (AppiumBy.ID, 'ru.gosuslugi.culture.test:id/vcbn_inc_favorites')
    ONBOARDING_NEXT_BUTTON = (AppiumBy.ID, 'ru.gosuslugi.culture.test:id/root')
    PERMISSION_ALLOW_BUTTON = (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')
    PERMISSION_ONE_TIME_BUTTON = (AppiumBy.ID,'com.android.permissioncontroller:id/permission_allow_one_time_button')
    CLOSE_BUTTON = (AppiumBy.ID, 'ru.gosuslugi.culture.test:id/fbb_iv_close')
    POPULAR_LIST_TITLE = (AppiumBy.ID, 'ru.gosuslugi.culture.test:id/ipl_tv_title')
    WIDGET_BUTTON = (AppiumBy.XPATH, '//android.widget.Button')
    FAVORITE_BUTTONS = '//android.widget.ImageView[@resource-id="ru.gosuslugi.culture.test:id/ip_iv_favorite_btn"]'
    LOGIN_WINDOW = (AppiumBy.ID, 'ru.gosuslugi.culture.test:id/title_template')
    AUTH_ABORT_BUTTON = (AppiumBy.ID, 'android:id/button2')
    AUTH_BUTTON = (AppiumBy.ID, 'android:id/button2')
    FAVORITE_PLACES_TAB = (AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="места"]')
    EMPTY_FAVORITE_TEXT = (AppiumBy.ID, 'ru.gosuslugi.culture.test:id/vce_tv_title')
    BLACK_THEME_BTH = (AppiumBy.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]')
    WHITE_THEME_BTH = (AppiumBy.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]')
    BACKGROUND_ELEMENT = (AppiumBy.ID, 'ru.gosuslugi.culture.test:id/am_fl_tooltip_container')


def skip_onboarding():
    logger.info("Starting onboarding skipping...")
    with step('Skipping onboarding'):
        for _ in range(4):
            browser.element(Locators.ONBOARDING_NEXT_BUTTON).click()

        browser.element(Locators.WIDGET_BUTTON).click()
        browser.element(Locators.PERMISSION_ALLOW_BUTTON).click()
        browser.element(Locators.WIDGET_BUTTON).click()
        browser.element(Locators.PERMISSION_ONE_TIME_BUTTON).click()
        browser.element(Locators.CLOSE_BUTTON).click()


def switch_color_theme():
    browser.element(Locators.PROFILE_TAB).click()
    browser.all(Locators.PROFILE_BUTTONS)[1].click()
    #Проверяю темную тему
    browser.element(Locators.BLACK_THEME_BTH).click()
    background_element = browser.element(Locators.BACKGROUND_ELEMENT)
    background_color = background_element.get('background')
    assert background_color == '#000000', f"Background color is not black: {background_color}"
    #Проверяю светлую тему
    browser.element(Locators.WHITE_THEME_BTH).click()
    background_element = browser.element(Locators.BACKGROUND_ELEMENT)
    background_color = background_element.get_attribute('background')  # или другой атрибут
    assert background_color == '#FFFFFF', f"Background color is not white: {background_color}"


def test_search():
    skip_onboarding()
    with step('Verify that the popular list contains "Пушкинские премьеры"'):
        results = browser.all(Locators.POPULAR_LIST_TITLE)
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Пушкинские премьеры'))

    with step('try to add favorite'):
        favorite_buttons = browser.all(('xpath', Locators.FAVORITE_BUTTONS))
        favorite_buttons[0].click()
        browser.element(Locators.LOGIN_WINDOW).should(be.visible)
        browser.element(Locators.AUTH_BUTTON).should(be.visible)
        browser.element(Locators.AUTH_ABORT_BUTTON).click()

    with step('check favorite list'):
        empty_favorite_events_text = 'Авторизуйтесь, чтобы увидеть избранные события'
        empty_favorite_places_text = 'Авторизуйтесь, чтобы увидеть избранные места проведения'
        browser.element(Locators.FAVORITE_TAB).click()
        browser.element(Locators.EMPTY_FAVORITE_TEXT).should(have.text(empty_favorite_events_text))
        browser.element(Locators.FAVORITE_PLACES_TAB).click()
        browser.element(Locators.EMPTY_FAVORITE_TEXT).should(have.text(empty_favorite_places_text))

    with step('switch_color_theme'):
        switch_color_theme()