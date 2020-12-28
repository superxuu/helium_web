import time
import allure
import pytest
from helium import *
from common.assert_with_screenshoot import screenshoot
from data.user_list_data import user_list_search_data


@pytest.mark.run(order=9)
@allure.feature('用户管理')
class TestUserList(object):

    @allure.story('用户搜索')
    @pytest.mark.parametrize('data', user_list_search_data)
    def test_user_list_search(self, data, open_close_browser_with_admin_data):
        driver = open_close_browser_with_admin_data
        allure.dynamic.description(data['name'])
        click('用户管理')
        highlight('用户列表')
        click('用户列表')
        wait_until(Text('是否激活').exists)
        click(Button('清空'))
        if data['params'].get('start_time', None):
            write(data['params'].get('start_time'), into='起始时间')
        if data['params'].get('end_time', None):
            write(data['params'].get('end_time'), into='截止时间')
        if data['params'].get('active', None):
            click(TextField('全部'))
            click(ListItem(data['params'].get('active')))
        if data['params'].get('keywords', None):
            write(data['params'].get('keywords'), into='用户名或手机号码')

        click(Button('筛选'))
        try:
            el = Text(to_left_of=S('.el-icon-arrow-left'))
            # highlight(el)
            value = el.value
        except:
            value = '共 0 条'
        try:
            assert value == data['expected_result']
        except AssertionError as e:
            screenshoot(driver, f'{data["name"]}')
            raise e
