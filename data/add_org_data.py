import time
from common.generate_phone import generate_phone


add_org_data = [
    {'name': '正常创建新机构', 'params': {'org_name':f'web自动化随便创建的机构-{time.strftime("%Y%m%d%H%M%S", time.localtime())}','type': '私募基金', 'name': 'web自动化','phone':f'{generate_phone()}'}, 'case_status': True, 'expected_result': "Text('保存成功').exists()"},
    {'name': '机构名称为空', 'params': {'type': '私募基金', 'name': 'web自动化','phone':f'{generate_phone()}'}, 'case_status': False, 'expected_result': "Text('必填项', above=TextField(to_right_of='机构类型')).exists()"},
    {'name': '机构类型为空', 'params': {'org_name':f'web自动化随便创建的机构-{time.strftime("%Y%m%d%H%M%S", time.localtime())}', 'name': 'web自动化','phone':f'{generate_phone()}'}, 'case_status': False, 'expected_result': "Text('必填项', below=TextField(to_right_of='机构类型')).exists()"},
    {'name': '联系人姓名为空', 'params': {'org_name':f'web自动化随便创建的机构-{time.strftime("%Y%m%d%H%M%S", time.localtime())}','type': '私募基金','phone':f'{generate_phone()}'}, 'case_status': False, 'expected_result': "Text('必填项', above=TextField('请输入联系人手机号码...')).exists()"},
    {'name': '联系人手机号为空', 'params': {'org_name':f'web自动化随便创建的机构-{time.strftime("%Y%m%d%H%M%S", time.localtime())}','type': '私募基金','name': 'web自动化'}, 'case_status': False, 'expected_result': "Text('必填项', below=TextField('请输入联系人手机号码...')).exists()"},
    {'name': '联系人手机号不合法', 'params': {'org_name':f'web自动化随便创建的机构-{time.strftime("%Y%m%d%H%M%S", time.localtime())}','type': '私募基金','name': 'web自动化','phone':'54321'}, 'case_status': False, 'expected_result': "Text('请输入正确的手机号', below=TextField('请输入联系人手机号码...')).exists()"},

]


