import logging, time
from allure_commons._allure import step
from selene import browser, have, be
from PIL import Image
from tests.android_app_culture.locators import Locators


logger = logging.getLogger(__name__)



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


def get_pixel_color_from_screenshot(screenshot_path, x, y):
    image = Image.open(screenshot_path)
    pixel_color = image.getpixel((x, y))
    return pixel_color


def test_switch_color_theme():
    # Определяем координаты для проверки цвета
    screen_width, screen_height = browser.driver.get_window_size().values()
    x, y = screen_width // 2, screen_height // 2  # Центр экрана

    with step('Switch to black theme'):
        browser.element(Locators.PROFILE_TAB).click()
        browser.all(Locators.PROFILE_BUTTONS)[1].click()
        browser.element(Locators.BLACK_THEME_BTH).click()

        # Ожидание для рендера цвета и скриншот
        time.sleep(1)
        screenshot_path = "black_theme.png"
        browser.driver.save_screenshot(screenshot_path)

        background_color = get_pixel_color_from_screenshot(screenshot_path, x, y)
        assert background_color[:3] == (0, 0, 0), f"Background color is not black: {background_color}"

    with step('Switch to white theme'):
        browser.element(Locators.WHITE_THEME_BTH).click()

        # Ожидание для рендера цвета и скриншот
        time.sleep(1)
        screenshot_path = "white_theme.png"
        browser.driver.save_screenshot(screenshot_path)

        background_color = get_pixel_color_from_screenshot(screenshot_path, x, y)
        assert background_color[:3] == (255, 255, 255), f"Background color is not white: {background_color}"



def test_app_culture_smoke():
    skip_onboarding()
    with step('Main page verify'):
        results = browser.all(Locators.POPULAR_LIST_TITLE)
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Пушкинские премьеры'))

    with step('Try to add favorite'):
        favorite_buttons = browser.all(('xpath', Locators.FAVORITE_BUTTONS))
        favorite_buttons[0].click()
        browser.element(Locators.LOGIN_WINDOW).should(be.visible)
        browser.element(Locators.AUTH_BUTTON).should(be.visible)
        browser.element(Locators.AUTH_ABORT_BUTTON).click()

    with step('Check favorite list'):
        empty_favorite_events_text = 'Авторизуйтесь, чтобы увидеть избранные события'
        empty_favorite_places_text = 'Авторизуйтесь, чтобы увидеть избранные места проведения'
        browser.element(Locators.FAVORITE_TAB).click()
        browser.element(Locators.EMPTY_FAVORITE_TEXT).should(have.text(empty_favorite_events_text))
        browser.element(Locators.FAVORITE_PLACES_TAB).click()
        browser.element(Locators.EMPTY_FAVORITE_TEXT).should(have.text(empty_favorite_places_text))

    with step('Switch_color_theme'):
        test_switch_color_theme()