import time
import allure
import pytest
from helium import *
from seleniumwire import webdriver
from common.config import admin_host, org_host, admin_user, admin_pwd, org_user, org_pwd
from common.redis_code import get_captcha_code, get_captcha_token

driver = None


def pytest_addoption(parser):
    """添加命令行参数-B"""
    parser.addoption(
        "-B", action="store", default="Chrome", help="browser option:Firefox or Chrome"
    )


@pytest.fixture(scope='session')
def driver(request):
    global driver
    browser = request.config.getoption('-B')
    args = ['-headless', "-incognito", '-disable-gpu', '-lang=zh-C']  # 无头
    # args=["-incognito",'-disable-gpu','-lang=zh-CN']#有头if browser in['Chrome','c','C','chrome','CHROME']:print(’使用Chrome浏览器’)
    if browser in ['Chrome', 'CHROME', 'chrome', 'c', 'C']:
        print('使用Chrome浏览器')
        # 谷歌浏览器设置
        chrome_options = webdriver.ChromeOptions()
        for i in args:
            chrome_options.add_argument(i)
        driver = webdriver.Chrome(options=chrome_options)
    else:
        print('使用Firefox浏览器')
        # 火狐浏览器设置
        firefox_options = webdriver.FirefoxOptions()
        for j in args:
            firefox_options.add_argument(j)
        driver = webdriver.Firefox(options=firefox_options)
    driver.set_window_size(width=1680, height=1050, windowHandle='current')
    set_driver(driver)
    return driver


@pytest.fixture(scope="function")
def open_close_browser(driver):
    yield driver
    kill_browser()


@pytest.fixture(scope="class")
def open_close_browser_with_admin_data(driver):
    driver.get(admin_host)
    captcha_url = f"{admin_host}/ztone/captcha/send"
    write(admin_user, into='请输入账号')
    write(admin_pwd, into='请输入密码')
    captcha_code = get_captcha_code(get_captcha_token(driver, captcha_url)['captchaToken'])
    write(captcha_code, into='请输入验证码')
    press(ENTER)
    time.sleep(1)
    yield driver
    kill_browser()


@pytest.fixture(scope="class")
def open_close_browser_with_org_data(driver):
    driver.get(org_host)
    captcha_url = f"{org_host}/ztone/captcha/send"
    write(org_user, into='请输入账号')
    write(org_pwd, into='请输入密码')
    captcha_code = get_captcha_code(get_captcha_token(driver, captcha_url)['captchaToken'])
    write(captcha_code, into='请输入验证码')
    press(ENTER)
    time.sleep(1)
    yield driver
    kill_browser()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport():
    """获取每个用例状态的钩子函数"""
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        # 添加allure报告截图
        with allure.step('添加失败截图...'):
            allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
