from common.mysql_connect import MysqlDB

customerid = MysqlDB().query('customer', 'name="web自动化测试机构"')[0].id
# org_ai =  MysqlDB().sql_query(f"SELECT * from meeting where asr_flag=1 and customer_id='{customerid}' and  status=8 and deleted =0")
org_sql = f"SELECT count(*) from meeting where asr_flag=1 and customer_id='{customerid}' and  status=8 and deleted =0"
# time_ai =  MysqlDB().sql_query(f"SELECT * from meeting where asr_flag=1 and order_start_time>='2020-11-20' and order_start_time<'2020-12-16' and status=8 and  deleted =0")
time_sql = "SELECT count(*) from meeting where asr_flag=1 and order_start_time>='2020-11-20' and order_start_time<'2021-01-01' and status=8 and  deleted =0"
# title_ai =  MysqlDB().sql_query(f"SELECT * from meeting where asr_flag=1 and title like '%测试%' and status=8 and deleted =0")
title_sql = "SELECT COUNT(*) from meeting where asr_flag=1 and title like '%测试%' and status=8 and deleted =0"
# all_ai =  MysqlDB().sql_query(f"SELECT * from meeting where asr_flag=1 and customer_id='{customerid}' and order_start_time>='2020-11-20' and order_start_time<'2020-12-16' and title like '%测试%' and status=8 and deleted =0")
all_sql = f"SELECT COUNT(*) from meeting where asr_flag=1 and customer_id='{customerid}' and order_start_time>='2020-11-20' and order_start_time<'2021-01-01' and title like '%测试%' and status=8 and deleted =0"



ai_search_data = [
    {'name': '根据所属机构查询', 'params': {'org': 'web自动化测试机构'}, 'case_status': True, 'expected_result': f'{org_sql}'},
    {'name': '根据预约时间范围查询', 'params': {'start_time': '2020-11-20', 'end_time': '2020-12-31'}, 'case_status': True, 'expected_result': f'{time_sql}'},
    {'name': '根据会议主题查询', 'params': {'title': '测试'}, 'case_status': True, 'expected_result': f'{title_sql}'},
    {'name': '所有条件一起查询', 'params': {'org': 'web自动化测试机构', 'start_time': '2020-11-20', 'end_time': '2020-12-31','title': '测试'}, 'case_status': True, 'expected_result': f'{all_sql}'},

]
