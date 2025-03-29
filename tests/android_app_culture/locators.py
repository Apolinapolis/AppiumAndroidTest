from appium.webdriver.common.appiumby import AppiumBy



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
    BACKGROUND_ELEMENT = (AppiumBy.ID, 'ru.gosuslugi.culture.test:id/am_fl_tooltip_container')
    EMPTY_FAVORITE_TEXT = (AppiumBy.ID, 'ru.gosuslugi.culture.test:id/vce_tv_title')
    BLACK_THEME_BTH = (AppiumBy.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/'
                                       'android.view.View[2]/android.view.View[1]')
    WHITE_THEME_BTH = (AppiumBy.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/'
                                       'android.view.View[1]/android.view.View[1]')