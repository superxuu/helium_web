import time
import allure
import pytest
from helium import *

from common.assert_with_screenshoot import screenshoot
from data.ai_search_data import ai_search_data

@pytest.mark.run(order=5)
@allure.feature('会议管理')
class TestAISearch(object):

    @allure.story('会议列表查询')
    @pytest.mark.parametrize('data', ai_search_data)
    def test_ai_search(self, data, open_close_browser_with_admin_data):
        allure.dynamic.description(data['name'])
        d = open_close_browser_with_admin_data
        # refresh()
        click(Text('AI速记', below='音频管理'))  # 进入音频管理界面
        wait_until(Text('下载').exists)
        click('清空')
        if data['params'].get('org', None):
            highlight(find_all(S('.el-input__inner'))[1])
            click(find_all(S('.el-input__inner'))[1])  # 所属机构
            write(data['params'].get('org'))  # 在所属机构框输入进行模糊搜索
            click(ListItem(data['params'].get('org')))
        if data['params'].get('start_time', None):
            write(data['params'].get('start_time'), into='起始时间')
        if data['params'].get('end_time', None):
            write(data['params'].get('end_time'), into='截止时间')
        if data['params'].get('title', None):
            write(data['params'].get('title'), into='关联会议主题')
        click('筛选')
        time.sleep(1)
        try:
            el = Text(to_left_of=S('.el-icon-arrow-left'))
            highlight(el)
            value = el.value
        except:
            value = '共 0 条'
        try:
            assert value == data['expected_result']
        except AssertionError as e:
            screenshoot(d, f'{data["name"]}')
            raise e
