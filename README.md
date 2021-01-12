最新版优化失败截图逻辑，使用装饰器，使运行过程中的任何异常都可以触发截图，不仅限于断言失败，同时也简化了断言的写法：
helium_web\common\screen_shoot.py

为了兼容@screenshoot装饰器，如果案例不使用数据驱动，在case函数人为添加data参数，并设置默认值：data={'name': '这是本条案例的名称'}

例如：
```python
@screenshoot
@allure.story('编辑套餐模板')
def test_edit_template(self, open_close_browser_with_admin_data, data={'name': '禁用与启用套餐模板'}):
    pass
```

2021-01-12：
1.增加命令行参数 -B，控制浏览器选项
2.增加兼容Firefox浏览器
3.优化conftest.py