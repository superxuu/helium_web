import random
import time

import allure
import pytest
from helium import *
from common.assert_with_screenshoot import screenshoot
from data.admin_edit_meeting_data import admin_edit_meeting_data


@pytest.mark.admin
@pytest.mark.run(order=10)
@allure.feature('会议管理')
class TestAdminEditMeeting(object):

    @screenshoot
    @allure.story('会议编辑')
    @pytest.mark.parametrize('data', admin_edit_meeting_data)
    def test_admin_edit_meeting(self, data, open_close_browser_with_admin_data):
        global title
        driver = open_close_browser_with_admin_data
        allure.dynamic.description(data['name'])
        refresh()
        click('会议列表')
        # click(Button('清空'))
        if data['params'].get('status', None):
            click(TextField(to_left_of='关键词'))
            click(ListItem(data['params'].get('status')))
            write('web自动化测试会议', into='会议主题或会议室号')
        click(Button('筛选'))
        click('详情')
        time.sleep(1)
        if data['params'].get('type', None):
            click(data['params'].get('type'))
        if data['params'].get('title', None):
            title = data['params'].get('title') + str(random.randint(0, 99))
            write(title, into=TextField(to_right_of='会议主题'))
        if data['params'].get('introduce', None):
            write(data['params'].get('introduce'), into=TextField(to_right_of='会议介绍'))
        if data['params'].get('guest', None):
            write(data['params'].get('guest'), into=TextField(to_right_of='嘉宾介绍'))
        driver.execute_script("arguments[0].scrollIntoView();", Text('AI速记设置').web_element)
        if data['params'].get('start_time', None):
            if data['params'].get('start_time') == True:
                click('立即开始')
            else:
                write(data['params'].get('start_time'), into='请选择开始时间')
        if data['params'].get('num', None):
            click(TextField('请选择', to_right_of='预计参会人数'))
            click(ListItem(data['params'].get('num')))
        if data['params'].get('way', None):
            click('人工会议') if data['params'].get('way') == 'staff' else click('自助会议')
            # Text('AI速记设置').web_element.location_once_scrolled_into_view  # 翻到下半页，以便于后面操作
        if data['params'].get('audio', None):
            if data['params'].get('audio') == 'on':
                click(Text('启用', to_right_of='录音设置'))
            else:
                click(Text('关闭', to_right_of='录音设置'))
        if data['params'].get('AI', None):
            click(Text('启用', to_right_of='AI速记设置')) if data['params'].get('AI') == 'on' else click(
                Text('关闭', to_right_of='AI速记设置'))
        click('保存')
        wait_until(Button('筛选').exists)
        write(title, into='会议主题或会议室号')
        click('筛选')
        el = Text(to_left_of=S('.el-icon-arrow-left'))
        assert el.value == '共 1 条'
