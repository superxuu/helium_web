import time
import allure
import pytest
from helium import *
from common.mysql_connect import MysqlDB
from common.screen_shoot import screenshoot
from data.org_audio_search_data import audio_search_data


@pytest.mark.org
@pytest.mark.run(order=4)
@allure.feature('会议管理')
class TestOrgAudioSearch(object):

    @screenshoot
    @allure.story('会议列表查询')
    @pytest.mark.parametrize('data', audio_search_data)
    def test_org_audio_search(self, data, open_close_browser_with_org_data):
        allure.dynamic.description(data['name'])
        # refresh()
        click('音频管理')  # 进入音频管理界面
        wait_until(Text('下载').exists)
        click('清空')
        if data['params'].get('start_time', None):
            write(data['params'].get('start_time'), into='起始时间')
        if data['params'].get('end_time', None):
            write(data['params'].get('end_time'), into='截止时间')
        if data['params'].get('title', None):
            write(data['params'].get('title'), into='搜索会议主题')
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
