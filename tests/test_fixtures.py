from selene.support.conditions import be
from selene.support.shared import browser


def test_github_desktop(browser_desktop):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"][value="Sign in"]').should(be.visible)


def test_github_mobile(browser_mobile):
    browser.open('https://github.com/')
    browser.element('[type="button"].Button--link[aria-label="Toggle navigation"]').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"][value="Sign in"]').should(be.visible)



