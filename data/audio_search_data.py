from common.mysql_connect import MysqlDB

customerid = MysqlDB().query('customer', 'name="北鼎股份"')[0].id
org_audio =  MysqlDB().sql_query(f"SELECT * from meeting where auto_record=1 and customer_id='{customerid}' and  status=8 and deleted =0")
time_audio =  MysqlDB().sql_query(f"SELECT * from meeting where auto_record=1 and order_start_time>='2020-11-20' and order_start_time<'2020-12-16' and status=8 and  deleted =0")
title_audio =  MysqlDB().sql_query(f"SELECT * from meeting where auto_record=1 and title like '%测试%' and status=8 and deleted =0")
all_audio =  MysqlDB().sql_query(f"SELECT * from meeting where auto_record=1 and customer_id='{customerid}' and order_start_time>='2020-11-20' and order_start_time<'2020-12-16' and title like '%测试%' and status=8 and deleted =0")



audio_search_data = [
    {'name': '根据所属机构查询', 'params': {'org': '北鼎股份'}, 'case_status': True, 'expected_result': f'共 {len(org_audio)} 条'},
    {'name': '根据预约时间范围查询', 'params': {'start_time': '2020-11-20', 'end_time': '2020-12-15'}, 'case_status': True, 'expected_result': f'共 {len(time_audio)} 条'},
    {'name': '根据会议主题查询', 'params': {'title': '测试'}, 'case_status': True, 'expected_result': f'共 {len(title_audio)} 条'},
    {'name': '所有条件一起查询', 'params': {'org': '北鼎股份', 'start_time': '2020-11-20', 'end_time': '2020-12-15','title': '测试'}, 'case_status': True, 'expected_result': f'共 {len(all_audio)} 条'},

]
