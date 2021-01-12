import time
import allure
import pytest
from helium import *

from common.screen_shoot import screenshoot
from common.redis_code import get_captcha_code, get_captcha_token
from common.config import org_host
from data.org_login_data import org_login_data


@pytest.mark.org
@pytest.mark.run(order=1)
@allure.feature('机构登录')
class TestLogin(object):

    @screenshoot
    @allure.story('登录页面验证')
    @pytest.mark.parametrize('data', org_login_data)
    def test_org_login(self, data, open_close_browser):
        allure.dynamic.description(data['name'])
        driver = open_close_browser
        driver.get(org_host)
        captcha_url = f"{org_host}/ztone/captcha/send"
        write(data['params']['name'], into='请输入账号')
        write(data['params']['pwd'], into='请输入密码')
        if data['params']['capture'] == None:
            captcha_code = get_captcha_code(get_captcha_token(driver, captcha_url)['captchaToken'])
        else:
            captcha_code = data['params']['capture']
        write(captcha_code, into='请输入验证码')
        press(ENTER)
        time.sleep(1)
        assert eval(data['expected_result'])
