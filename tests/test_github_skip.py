import pytest
from selene.support.conditions import be

from selene.support.shared import browser


@pytest.mark.parametrize('window_size', [pytest.param('desktop'), pytest.param('mobile')])
def test_github_desktop(window_size):
    if window_size == 'mobile':
        pytest.skip('wrong window size for mobile test')
    else:
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        browser.open('https://github.com/')
        browser.element('.HeaderMenu-link--sign-in').click()
        browser.element('[type="submit"][value="Sign in"]').should(be.visible)


@pytest.mark.parametrize('window_size', [pytest.param('desktop'), pytest.param('mobile')])
def test_github_mobile(window_size):
    if window_size == 'desktop':
        pytest.skip('wrong window size for desktop test')
    else:
        browser.config.window_width = 375
        browser.config.window_height = 667
        browser.open('https://github.com/')
        browser.element('[type="button"].Button--link[aria-label="Toggle navigation"]').click()
        browser.element('.HeaderMenu-link--sign-in').click()
        browser.element('[type="submit"][value="Sign in"]').should(be.visible)




