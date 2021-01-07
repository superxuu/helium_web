import time


price_template_data = [
    {'name': '正常增加新套餐模板', 'params': {'name': f'web自动化新增套餐-{time.strftime("%Y%m%d%H%M%S", time.localtime())}','desc':'web自动化过程中创建的套餐，不重要','price':'0.99'}, 'case_status': True, 'expected_result': f'Text("操作成功").exists'},
    {'name': '套餐名称为空', 'params': {'desc':'web自动化过程中创建的套餐，不重要','price':'0.99'}, 'case_status': True, 'expected_result': "Text('必填项', above=TextField('添加一段套餐描述')).exists()"},
    {'name': '套餐描述为空', 'params': {'name':f'web自动化新增套餐-{time.strftime("%Y%m%d%H%M%S", time.localtime())}','price':'0.99'}, 'case_status': True, 'expected_result': "Text('必填项', below=TextField('添加一段套餐描述')).exists()"},
]



