import time
import allure
import pytest
from helium import *

from common.screen_shoot import screenshoot
from common.redis_code import get_captcha_code, get_response
from common.config import admin_host
from data.admin_login_data import login_data


@pytest.mark.admin
@pytest.mark.run(order=1)
@allure.feature('登录')
class TestLogin(object):

    @screenshoot
    @allure.story('登录页面验证')
    @pytest.mark.parametrize('data', login_data)
    def test_login(self, data, open_close_browser):
        allure.dynamic.description(data['name'])
        driver = open_close_browser
        driver.get(admin_host)
        captcha_url = f"{admin_host}/ztone/captcha/send"
        write(data['params']['name'], into='请输入账号')
        write(data['params']['pwd'], into='请输入密码')
        if data['params']['capture'] == None:
            captcha_code = get_captcha_code(get_response(driver, captcha_url)['captchaToken'])
        else:
            captcha_code = data['params']['capture']
        write(captcha_code, into='请输入验证码')
        press(ENTER)
        time.sleep(1)
        assert eval(data['expected_result'])
