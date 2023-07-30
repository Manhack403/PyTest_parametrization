import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser:'--browser_name=chrome or firefox'")
    parser.addoption('--language', action='store', default=None,
                     help="Choose browser language:'--language=ru or en'")

@pytest.fixture(scope="class")
def browser(request):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': ru, en}) #выбор языка для Хром

    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", ru, en) #выбор языка для Фаерфокс

    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(10)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
