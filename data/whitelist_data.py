from common.mysql_connect import MysqlDB
from common.generate_phone import generate_phone
import time

org_list = MysqlDB().sql_query("SELECT * FROM whitelist WHERE customer_id='4861736231813292032' and deleted=0")
time_list = MysqlDB().sql_query("SELECT * FROM whitelist WHERE create_time>='2020-09-09' and create_time<'2020-10-30' and deleted=0")
keywords_list = MysqlDB().sql_query("SELECT * FROM whitelist WHERE name like '%测试%' and deleted=0")
all_list = MysqlDB().sql_query("SELECT * FROM whitelist WHERE customer_id='4861736231813292032' and create_time>='2020-09-09' and create_time<'2020-12-30' and name like '%科技%' and deleted=0")

whitelist_search_data = [
    {'name': '根据所属机构搜索白名单', 'params': {'org': '北鼎股份'}, 'case_status': True, 'expected_result': f'共 {len(org_list)} 条'},
    {'name': '根据创建时间范围搜索白名单', 'params': {'start_time': '2020-09-09', 'end_time':'2020-10-29'}, 'case_status': True, 'expected_result': f'共 {len(time_list)} 条'},
    {'name': '根据关键词搜索白名单', 'params': {'keywords': '测试'}, 'case_status': True, 'expected_result': f'共 {len(keywords_list)} 条'},
    {'name': '根据全部条件搜索白名单', 'params': {'org': '北鼎股份','start_time': '2020-09-09', 'end_time':'2020-12-29','keywords': '科技'}, 'case_status': True, 'expected_result': f'共 {len(all_list)} 条'},

]

whitelist_add_data = [
    {'name': '正常创建白名单', 'params': {'org': '北鼎股份','name':f'web自动过程中创建的白名单-{time.strftime("%Y%m%d%H%M%S", time.localtime())}'}, 'expected_result': "Text('操作成功').exists()"},
    {'name': '机构为空创建白名单', 'params': {'name':f'web自动过程中创建的白名单-{time.strftime("%Y%m%d%H%M%S", time.localtime())}'}, 'expected_result': "Text('必填项',above=TextField('设置一个白名单名称')).exists()"},
    {'name': '名称创建白名单', 'params': {'org': '北鼎股份'}, 'expected_result': "Text('必填项',below=TextField('设置一个白名单名称')).exists()"},

]

whitelist_add__user_data = [
    {'name': '正常创建白名单-全数据',  'params': {'phone': f'{generate_phone()}', 'name': f'web自动化-{time.strftime("%Y%m%d%H%M%S", time.localtime())}','company':'web自动化','department':'测试部','position':'测试管理'}, 'expected_result': "Text('操作成功').exists()"},
    {'name': '正常创建白名单-只有必填项',  'params': {'phone': f'{generate_phone()}', 'name': f'web自动化-{time.strftime("%Y%m%d%H%M%S", time.localtime())}'}, 'expected_result': "Text('操作成功').exists()"},
    {'name': '创建白名单-手机号为空',  'params': {'name': f'web自动化-{time.strftime("%Y%m%d%H%M%S", time.localtime())}'}, 'expected_result': "Text('必填项', above=t[-4]).exists()"},
    {'name': '创建白名单-姓名为空',  'params': {'phone': f'{generate_phone()}',}, 'expected_result': "Text('请输入用户名', below=t[-4]).exists()"},

]