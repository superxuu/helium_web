import time
import allure
import pytest
from helium import *

from common.assert_with_screenshoot import screenshoot
from data.meeting_search_data import meeting_search_data

@pytest.mark.run(order=2)
@allure.feature('会议管理')
class TestMeetingSearch(object):

    @allure.story('会议列表查询')
    @pytest.mark.parametrize('data', meeting_search_data)
    def test_meeting_search(self, data, open_close_browser_with_admin_data):
        allure.dynamic.description(data['name'])
        refresh()
        d = open_close_browser_with_admin_data
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
            time.sleep(0.5)
            click(ListItem(data['params'].get('type')))
        if data['params'].get('status', None):
            click(find_all(S('.el-input__inner'))[5])  # 会议状态
            time.sleep(0.5)
            click(ListItem(data['params'].get('status')))
        if data['params'].get('keywords', None):
            write(data['params'].get('keywords'), into='会议主题或会议室号')
        click('筛选')
        time.sleep(1)
        try:
            el = Text(to_left_of=S('.el-icon-arrow-left'))
            # highlight(el)
            value = el.value
        except:
            value = '共 0 条'
        try:
            assert value == data['expected_result']
        except AssertionError as e:
            screenshoot(d, f'{data["name"]}')
            raise e
