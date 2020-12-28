import time
import pytest
from helium import *
from selenium import webdriver
from common.config import admin_host, org_host, admin_user, admin_pwd, org_user, org_pwd
from common.redis_code import get_captcha_code, get_response

caps = {
    'browserName': 'chrome',
    'loggingPrefs': {
        'browser': 'ALL',
        'driver': 'ALL',
        'performance': 'ALL',
    },
    'goog:chromeOptions': {
        'perfLoggingPrefs': {
            'enableNetwork': True,
        },
        'w3c': False,
        'args': ["--incognito", '--headless', '--disable-gpu', '--lang=zh-CN', '--window-size=1680,1050'], #无头模式
        # 'args': ["--incognito", '--disable-gpu','--lang=zh-CN', '--window-size=1680,1050'],     #有头模式
    },
}


@pytest.fixture(scope="function")
def open_close_browser():
    driver = webdriver.Chrome(desired_capabilities=caps)
    # driver.maximize_window()
    # driver.set_window_size(width=1680, height=1050, windowHandle='current')
    set_driver(driver)
    yield driver
    kill_browser()


@pytest.fixture(scope="class")
def open_close_browser_with_admin_data():
    driver = webdriver.Chrome(desired_capabilities=caps)
    # driver.maximize_window()
    # driver.set_window_size(width=1680, height=1050, windowHandle='current')
    set_driver(driver)
    driver.get(admin_host)
    captcha_url = f"{admin_host}/ztone/captcha/send"
    write(admin_user, into='请输入账号')
    write(admin_pwd, into='请输入密码')
    captcha_code = get_captcha_code(get_response(driver, captcha_url)['captchaToken'])
    write(captcha_code, into='请输入验证码')
    press(ENTER)
    time.sleep(1)
    yield driver
    kill_browser()


@pytest.fixture(scope="class")
def open_close_browser_with_org_data():
    driver = webdriver.Chrome(desired_capabilities=caps)
    # driver.maximize_window()
    # driver.set_window_size(width=1680, height=1050, windowHandle='current')
    set_driver(driver)
    driver.get(org_host)
    captcha_url = f"{org_host}/ztone/captcha/send"
    write(org_user, into='请输入账号')
    write(org_pwd, into='请输入密码')
    captcha_code = get_captcha_code(get_response(driver, captcha_url)['captchaToken'])
    write(captcha_code, into='请输入验证码')
    press(ENTER)
    time.sleep(1)
    yield driver
    kill_browser()

# def pytest_generate_tests(metafunc):
#     pass
#     data_py = metafunc.module.__name__.split('.')[1]
#     data_func = metafunc.function.__name__
#     print(data_py)
#     print(data_func)
#     __import__(f'data.{data_py}.{data_func}_data')
#     func = getattr(data, f'{data_func}_data')
#     metafunc.parametrize('params',func.data_func())
