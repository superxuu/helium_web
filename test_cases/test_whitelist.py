import time
import allure
import pytest
from helium import *
from common.assert_with_screenshoot import screenshoot
from data.whitelist_data import whitelist_search_data, whitelist_add_data, whitelist_add__user_data


@pytest.mark.run(order=8)
@allure.feature('白名单管理')
class TestWhitelist(object):

    @allure.story('白名单搜索')
    @pytest.mark.parametrize('data', whitelist_search_data)
    def test_whitelist_search(self, data, open_close_browser_with_admin_data):
        driver = open_close_browser_with_admin_data
        allure.dynamic.description(data['name'])
        refresh()
        click('机构管理')
        wait_until(Text('白名单管理').exists)
        click('白名单管理')
        wait_until(Text('所属机构').exists)
        if data['params'].get('org', None):
            # highlight(TextField('全部', to_right_of='所属机构'))
            click(TextField('全部', to_right_of='所属机构'))
            write(data['params'].get('org'))
            click(ListItem(data['params'].get('org')))
        if data['params'].get('start_time', None):
            write(data['params'].get('start_time'), into='起始时间')
        if data['params'].get('end_time', None):
            write(data['params'].get('end_time'), into='截止时间')
        if data['params'].get('keywords', None):
            write(data['params'].get('keywords'), into='搜索白名单')
        click('筛选')
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

    @allure.story('白名单创建')
    @pytest.mark.parametrize('data', whitelist_add_data)
    def test_whitelist_add(self, data, open_close_browser_with_admin_data):
        driver = open_close_browser_with_admin_data
        allure.dynamic.description(data['name'])
        refresh()
        click('机构管理')
        wait_until(Text('白名单管理').exists)
        click('白名单管理')
        wait_until(Button('创建白名单').exists)
        click('创建白名单')
        if data['params'].get('org', None):
            click(TextField('请选择', to_right_of='所属机构'))
            write(data['params'].get('org'))
            click(ListItem(data['params'].get('org')))
        if data['params'].get('name', None):
            write(data['params'].get('name'), into='设置一个白名单名称')
        click(Button('确 定'))
        try:
            assert eval(data['expected_result'])
        except AssertionError as e:
            screenshoot(driver, f'{data["name"]}')
            raise e

    @allure.story('白名单添加用户')
    @pytest.mark.parametrize('data', whitelist_add__user_data)
    def test_whitelist_add_user(self, data, open_close_browser_with_admin_data):
        driver = open_close_browser_with_admin_data
        allure.dynamic.description(data['name'])
        refresh()
        click('机构管理')
        wait_until(Text('白名单管理').exists)
        click('白名单管理')
        wait_until(Button('创建白名单').exists)
        write('web自动过程中创建的白名单', into='搜索白名单')
        click('筛选')
        click(Text('详情', below='功能'))
        click(Button('添加用户'))
        t = find_all(S('.el-input__inner'))
        if data['params'].get('phone', None):
            write(data['params'].get('phone'), into='请输入电话号码')
        if data['params'].get('name', None):
            write(data['params'].get('name'), into=t[-4])
        if data['params'].get('company', None):
            write(data['params'].get('company'), into=t[-3])
        if data['params'].get('department', None):
            write(data['params'].get('department'), into=t[-2])
        if data['params'].get('position', None):
            write(data['params'].get('position'), into=t[-1])
        click(Button('确 定'))
        time.sleep(0.2)
        try:
            assert eval(data['expected_result'])
        except AssertionError as e:
            screenshoot(driver, f'{data["name"]}')
            raise e



