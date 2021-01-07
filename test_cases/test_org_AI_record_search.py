import time
import allure
import pytest
from helium import *
from common.mysql_connect import MysqlDB
from common.assert_with_screenshoot import screenshoot
from data.org_ai_search_data import ai_search_data


@pytest.mark.org
@pytest.mark.run(order=5)
@allure.feature('机构会议管理')
class TestOrgAISearch(object):

    @screenshoot
    @allure.story('机构会议列表查询')
    @pytest.mark.parametrize('data', ai_search_data)
    def test_org_ai_search(self, data, open_close_browser_with_org_data):
        allure.dynamic.description(data['name'])
        # refresh()
        click(Text('AI速记', below='音频管理'))  # 进入音频管理界面
        wait_until(Text('下载').exists)
        click('清空')
        if data['params'].get('start_time', None):
            write(data['params'].get('start_time'), into='起始时间')
        if data['params'].get('end_time', None):
            write(data['params'].get('end_time'), into='截止时间')
        if data['params'].get('title', None):
            write(data['params'].get('title'), into='关联会议主题')
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
