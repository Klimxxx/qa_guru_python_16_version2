import pytest
from selene import browser, have


@pytest.fixture(params=[(1920, 1080), (1600, 900), (1440, 900), (1366, 768), (1280, 800)], scope='function')
def desktop_browser(request):
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield
    browser.quit()


# @pytest.mark.parametrize(
#                         "user, password",
#                          [
#                              pytest.param("Klim", "   ", id="Chrome"),
#                              pytest.param("  ", "qa123"),
#                              pytest.param("", ""),
#                          ]
#                          )
# def test_user_login(user, password):
#     print(user, password)
#     browser.open()
#     browser.element("#user").type(user)
#     browser.element("#password").type(password)
#     browser.element("#submit").click()
#     browser.element("#error_massage").should(have.text("Wrong password for user"))



@pytest.fixture(params=[(360, 640), (375, 667), (414, 896), (360, 780), (360, 720)], scope='function')
def mobile_browser(request):
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield
    browser.quit()


def test_github_desktop(desktop_browser):
    browser.open('/')

    browser.element('[class~="HeaderMenu-link--sign-in"]').click()

    browser.element('[class="auth-form-header p-0"]').should(have.text('Sign in to GitHub'))


def test_github_mobile(mobile_browser):
    browser.open('/')

    browser.element('[class="flex-1 flex-order-2 text-right"] .Button-content').click()
    browser.element('[class~="HeaderMenu-link--sign-in"]').click()

    browser.element('[class="auth-form-header p-0"]').should(have.text('Sign in to GitHub'))
