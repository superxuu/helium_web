import time
import allure
import pytest
from helium import *
from common.assert_with_screenshoot import screenshoot
from common.mysql_connect import MysqlDB
from data.admin_user_list_data import user_list_search_data


@pytest.mark.admin
@pytest.mark.run(order=9)
@allure.feature('用户管理')
class TestUserList(object):

    @screenshoot
    @allure.story('用户搜索')
    @pytest.mark.parametrize('data', user_list_search_data)
    def test_user_list_search(self, data, open_close_browser_with_admin_data):
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
            el = S('.el-pagination__total')
            highlight(el)
            value = el.web_element.text
        except:
            value = '共 0 条'
        sql_data = MysqlDB().sql_query(data['expected_result'])[0]
        assert value == f'共 {sql_data} 条'
