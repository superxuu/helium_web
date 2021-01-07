import random
import time
import allure
import pytest
from helium import *

from common.assert_with_screenshoot import screenshoot
from data.admin_price_template_data import price_template_data


@pytest.mark.admin
@pytest.mark.run(order=6)
@allure.feature('套餐模板总览')
class TestPriceTemplate(object):

    @screenshoot
    @allure.story('创建新套餐模板')
    @pytest.mark.parametrize('data', price_template_data)
    def test_price_template(self, data, open_close_browser_with_admin_data):
        allure.dynamic.description(data['name'])
        click('资源管理')
        time.sleep(0.5)
        click('套餐模板总览')
        time.sleep(0.5)
        click(Button('创建新套餐'))
        time.sleep(1)
        if data['params'].get('name', None):
            write(data['params'].get('name') + str(random.randint(0, 99)), into='设置一个套餐名称')
        if data['params'].get('desc', None):
            write(data['params'].get('desc'), into='添加一段套餐描述')
        if data['params'].get('price', None):
            write(data['params'].get('price'), into=TextField(to_right_of='会议服务费'))
        click('保存并启用')
        time.sleep(0.5)
        assert eval(data['expected_result'])

    @screenshoot
    @allure.story('禁用与启用套餐模板')
    def test_disable_enable_template(self, open_close_browser_with_admin_data, data={'name': '禁用与启用套餐模板'}):
        allure.dynamic.description(data['name'])
        refresh()
        click('资源管理')
        time.sleep(0.5)
        click('套餐模板总览')
        time.sleep(0.5)
        # highlight(Text('查看', below='功能'))
        click(Text('查看', below='功能'))
        el1 = Text('套餐：启用中')
        el2 = Text('套餐：已禁用')
        wait_until(Text('套餐：').exists)
        if el1.exists():
            click(Button('禁用'))
            time.sleep(0.5)
            assert el2.exists()
            click(Button('启用'))
            time.sleep(0.5)
            assert el1.exists()
        elif el2.exists():
            click(Button('启用'))
            time.sleep(0.5)
            assert el1.exists()
            click(Button('禁用'))
            time.sleep(0.5)
            assert el2.exists()
        else:
            assert False

    @screenshoot
    @allure.story('编辑套餐模板')
    def test_edit_template(self, open_close_browser_with_admin_data, data={'name': '禁用与启用套餐模板'}):
        allure.dynamic.description(data['name'])
        refresh()
        click('资源管理')
        # wait_until(Text('套餐模板总览').exists)
        click('套餐模板总览')
        time.sleep(1)
        # highlight(Text('查看', below='功能'))
        click(Text('查看', below='功能'))
        time.sleep(0.5)
        wait_until(Button('返回上一页').exists)
        click('编辑')
        write(f'web自动化新增套餐-{time.strftime("%Y%m%d%H%M%S", time.localtime())}' + str(random.randint(0, 99)),
              into='设置一个套餐名称')
        write(f'web自动化过程中创建的套餐-{time.strftime("%Y%m%d%H%M%S", time.localtime())}', into='添加一段套餐描述')
        click('保存')
        time.sleep(0.5)
        assert Text("操作成功").exists()
