import random
import time
import allure
import pytest
from helium import *
from common.assert_with_screenshoot import screenshoot
from common.mysql_connect import MysqlDB
from data.org_whitelist_data import whitelist_search_data, whitelist_add__user_data, whitelist_add_data


@pytest.mark.org
@pytest.mark.run(order=6)
@allure.feature('机构白名单管理')
class TestOrgWhitelist(object):

    @screenshoot
    @allure.story('机构白名单搜索')
    @pytest.mark.parametrize('data', whitelist_search_data)
    def test_org_whitelist_search(self, data, open_close_browser_with_org_data):
        allure.dynamic.description(data['name'])
        refresh()
        click('机构管理')
        wait_until(Text('白名单管理').exists)
        click('白名单管理')
        highlight(Button('创建白名单'))
        if data['params'].get('start_time', None):
            write(data['params'].get('start_time'), into='起始时间')
        if data['params'].get('end_time', None):
            write(data['params'].get('end_time'), into='截止时间')
        if data['params'].get('keywords', None):
            write(data['params'].get('keywords'), into='搜索白名单')
        click('筛选')
        try:
            el = S('.el-pagination__total')
            highlight(el)
            value = el.web_element.text
        except:
            value = '共 0 条'
        sql_data = MysqlDB().sql_query(data['expected_result'])
        assert value == f'共 {len(sql_data)} 条'

    @screenshoot
    @allure.story('机构白名单创建')
    @pytest.mark.parametrize('data', whitelist_add_data)
    def test_org_whitelist_add(self, data, open_close_browser_with_org_data):
        allure.dynamic.description(data['name'])
        refresh()
        click('机构管理')
        wait_until(Text('白名单管理').exists)
        click('白名单管理')
        wait_until(Button('创建白名单').exists)
        click('创建白名单')
        if data['params'].get('name', None):
            write(data['params'].get('name') + str(random.randint(0, 99)), into='设置一个白名单名称')
        click(Button('确 定'))
        time.sleep(0.5)
        assert eval(data['expected_result'])

    @screenshoot
    @allure.story('机构白名单添加用户')
    @pytest.mark.parametrize('data', whitelist_add__user_data)
    def test_org_whitelist_add_user(self, data, open_close_browser_with_org_data):
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
            print(data['params'].get('phone'), end=' ')
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
        time.sleep(0.5)
        assert eval(data['expected_result'])
