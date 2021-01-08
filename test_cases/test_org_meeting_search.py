import time
import allure
import pytest
from helium import *
from common.mysql_connect import MysqlDB
from common.screen_shoot import screenshoot
from data.org_meeting_search_data import org_meeting_search_data


@pytest.mark.org
@pytest.mark.run(order=3)
@allure.feature('机构会议管理')
class TestOrgMeetingSearch(object):

    @screenshoot
    @allure.story('机构会议列表查询')
    @pytest.mark.parametrize('data', org_meeting_search_data)
    def test_org_meeting_search(self, data, open_close_browser_with_org_data):
        allure.dynamic.description(data['name'])
        refresh()
        if data['params'].get('start_time', None):
            write(data['params'].get('start_time'), into='起始时间')
        if data['params'].get('end_time', None):
            write(data['params'].get('end_time'), into='截止时间')
        if data['params'].get('type', None):
            # click(find_all(S('.el-input__inner'))[4])  # 会议类型
            click(TextField('全部', to_right_of='会议类型'))  # 会议类型
            time.sleep(0.5)
            click(ListItem(data['params'].get('type')))
        if data['params'].get('status', None):
            click(find_all(S('.el-input__inner'))[1])  # 会议状态
            time.sleep(0.5)
            click(ListItem(data['params'].get('status')))
        if data['params'].get('keywords', None):
            write(data['params'].get('keywords'), into='会议主题或会议室号')
        click('筛选')
        click('筛选')  # 应对linux中会议类型查询异常，添加一个筛选动作后正常
        time.sleep(1)
        try:
            el = S('.el-pagination__total')
            highlight(el)
            value = el.web_element.text
        except:
            value = '共 0 条'
        sql_data = MysqlDB().sql_query(data['expected_result'])[0]
        assert value == f'共 {sql_data} 条'
