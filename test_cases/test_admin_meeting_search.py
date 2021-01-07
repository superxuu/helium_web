import time
import allure
import pytest
from helium import *
from common.mysql_connect import MysqlDB
from common.assert_with_screenshoot import screenshoot
from data.admin_meeting_search_data import meeting_search_data


@pytest.mark.admin
@pytest.mark.run(order=3)
@allure.feature('会议管理')
class TestMeetingSearch(object):

    @screenshoot
    @allure.story('会议列表查询')
    @pytest.mark.parametrize('data', meeting_search_data)
    def test_meeting_search(self, data, open_close_browser_with_admin_data):
        allure.dynamic.description(data['name'])
        refresh()
        if data['params'].get('org', None):
            highlight(find_all(S('.el-input__inner'))[1])
            click(find_all(S('.el-input__inner'))[1])  # 所属机构
            write(data['params'].get('org'))  # 在所属机构框输入进行模糊搜索
            click(ListItem(data['params'].get('org')))
        if data['params'].get('start_time', None):
            write(data['params'].get('start_time'), into='起始时间')
        if data['params'].get('end_time', None):
            write(data['params'].get('end_time'), into='截止时间')
        if data['params'].get('type', None):
            click(find_all(S('.el-input__inner'))[4])  # 会议类型
            time.sleep(1)
            click(ListItem(data['params'].get('type')))
        if data['params'].get('status', None):
            click(find_all(S('.el-input__inner'))[5])  # 会议状态
            time.sleep(0.5)
            click(ListItem(data['params'].get('status')))
        if data['params'].get('keywords', None):
            write(data['params'].get('keywords'), into='会议主题或会议室号')
        click('筛选')
        click('筛选')
        time.sleep(1)
        try:
            el = S('.el-pagination__total')
            highlight(el)
            value = el.web_element.text
        except:
            value = '共 0 条'
        sql_data = MysqlDB().sql_query(data['expected_result'])[0]
        assert value == f'共 {sql_data} 条'
