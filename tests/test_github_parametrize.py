import pytest
from selene.support.conditions import be
from selene.support.shared import browser


@pytest.fixture(params=['desktop', 'mobile'])
def window_size(request):
    if request.param == "desktop":
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    elif request.param == "mobile":
        browser.config.window_width = 375
        browser.config.window_height = 667


desktop = pytest.mark.parametrize('window_size', ['desktop'], indirect=True)
mobile = pytest.mark.parametrize('window_size', ['mobile'], indirect=True)


@desktop
def test_github_desktop(window_size):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"][value="Sign in"]').should(be.visible)


@mobile
def test_github_mobile(window_size):
    browser.open('https://github.com/')
    browser.element('[type="button"].Button--link[aria-label="Toggle navigation"]').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"][value="Sign in"]').should(be.visible)



