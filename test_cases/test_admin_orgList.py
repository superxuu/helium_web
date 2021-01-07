import time
import allure
import pytest
import random
from helium import *
from common.generate_phone import generate_phone
from common.assert_with_screenshoot import screenshoot
from data.admin_add_org_data import add_org_data


@pytest.mark.admin
@pytest.mark.run(order=7)
@allure.feature('机构列表')
class TestOrgList(object):

    @screenshoot
    @allure.story('创建新机构')
    @pytest.mark.parametrize('data', add_org_data)
    def test_admin_orgList(self, data, open_close_browser_with_admin_data):
        allure.dynamic.description(data['name'])
        refresh()
        click('机构管理')
        time.sleep(1)
        wait_until(Text('机构列表').exists)
        click('机构列表')
        click(Button('创建新机构'))
        if data['params'].get('org_name', None):
            write(data['params'].get('org_name') + str(random.randint(0000, 99999)), into='请输入工商备案公司全称...')
        if data['params'].get('type', None):
            click(TextField(to_right_of='机构类型'))
            click(ListItem(data['params'].get('type')))
        if data['params'].get('name', None):
            write(data['params'].get('name'), into='请输入联系人姓名全称...')
        if data['params'].get('phone', None):
            write(data['params'].get('phone'), into='请输入联系人手机号码...')
        click('保存并启用')
        if data["name"] == '正常创建新机构':
            wait_until(lambda: not Text("保存并启用").exists())
            assert eval(data['expected_result'])
            write(data['params'].get('org_name'), into='搜索机构名称')
            click(find_all(S('.el-icon-search'))[1])
            time.sleep(10)
            el = Text(to_left_of=S('.el-icon-arrow-left'))
            assert el.value == '共 1 条'
        else:
            assert eval(data['expected_result'])

    @screenshoot
    @allure.story('冻结与解冻机构')
    def test_disable_enable_org(self, open_close_browser_with_admin_data, data={'name': '冻结与解冻机构'}):
        allure.dynamic.description(data['name'])
        click('机构管理')
        time.sleep(1)
        wait_until(Text('机构列表').exists)
        click('机构列表')
        click(Text('详情', below='功能'))
        el1 = Text('服务状态： 启动中')
        el2 = Text('服务状态： 已冻结')
        wait_until(Text('服务状态：').exists)
        if el1.exists():
            click(Button('冻结服务'))
            assert el2.exists()
            click(Button('启动服务'))
            assert el1.exists()
        elif el2.exists():
            click(Button('启动服务'))
            assert el1.exists()
            click(Button('冻结服务'))
            assert el2.exists()
        else:
            assert False

    @screenshoot
    @allure.story('编辑机构')
    def test_edit_org(self, open_close_browser_with_admin_data, data={'name': '编辑机构'}):
        allure.dynamic.description(data['name'])
        click('机构管理')
        time.sleep(1)
        wait_until(Text('机构列表').exists)
        click('机构列表')
        click(Text('详情', below='功能'))
        click('编辑')
        write(f'{generate_phone()}', into='请输入联系人姓名全称...')
        write(f'{generate_phone()}', into='请输入联系人手机号码...')
        click('保存')
        wait_until(lambda: not Text("保存").exists())
        assert Text('编辑成功').exists()

    @screenshoot
    @allure.story('机构备注')
    def test_org_notes(self, open_close_browser_with_admin_data, data={'name': '机构备注'}):
        allure.dynamic.description(data['name'])
        click('机构管理')
        time.sleep(1)
        wait_until(Text('机构列表').exists)
        click('机构列表')
        click(Text('备注', below='功能'))
        text = f'这是web自动化增加的备注-{time.strftime("%Y%m%d %H:%M:%S", time.localtime())}'
        write(text, into='点击此处添加一条新备注...')
        click(Button('保 存'))
        assert Text(text, above='备注人：').exists()
