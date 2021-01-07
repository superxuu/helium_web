from common.mysql_connect import MysqlDB

#根据机构查询会议
customerid = MysqlDB().query('customer', 'name="web自动化测试机构"')[0].id
# org_meetings = MysqlDB().query('meeting', f'customer_id="{customerid}" and deleted=0')
# org_meetings_sql = F"SELECT COUNT(1) FROM meeting WHERE customer_id={customerid} and deleted=0"

#根据预约时间范围查询会议
# time_meetings = MysqlDB().query('meeting', 'order_start_time>="2020-12-02" and order_end_time<"2020-12-16" and deleted=0')
time_sql = f'SELECT COUNT(1) FROM meeting WHERE customer_id={customerid} and order_start_time>="2020-12-02" and order_end_time<"2021-01-01" and deleted=0'

#根据会议类型-机构全公开查询
# type_meetings1 = MysqlDB().query('meeting', 'type=2 and deleted=0')
type_sql_1 = f'SELECT COUNT(1) FROM meeting WHERE customer_id={customerid} and type=2 and deleted=0'
#根据会议类型-平台全公开查询
# type_meetings2 = MysqlDB().query('meeting', 'type=0 and deleted=0')
type_sql_2 = f'SELECT COUNT(1) FROM meeting WHERE customer_id={customerid} and type=0 and deleted=0'
#根据会议类型-白名单查询
# type_meetings3 = MysqlDB().query('meeting', 'type=1 and deleted=0')
type_sql_3 = f'SELECT COUNT(1) FROM meeting WHERE customer_id={customerid} and type=1 and deleted=0'

# status:0未开始1已准备2，进行中8.已结束9.已取消
#根据会议状态-未开始查询
# status_meetings1 = MysqlDB().query('meeting', 'status=0 or status=1 and deleted=0')
status_sql_1 = f'SELECT COUNT(1) FROM meeting WHERE customer_id={customerid} and status=0 or status=1 and deleted=0'
#根据会议状态-会议中查询
# status_meetings2 = MysqlDB().query('meeting', 'status=2 and deleted=0')
status_sql_2 = f'SELECT COUNT(1) FROM meeting WHERE customer_id={customerid} and status=2 and deleted=0'
#根据会议状态-已结束查询
# status_meetings3 = MysqlDB().query('meeting', 'status=8 and deleted=0')
status_sql_3 = f'SELECT COUNT(1) FROM meeting WHERE customer_id={customerid} and status=8 and deleted=0'

# 根据会议主题关键词查询查询
# keywords_meetings1 = MysqlDB().query('meeting', 'title like "%测试%" and deleted=0')
keywords_sql = f'SELECT COUNT(1) FROM meeting WHERE customer_id={customerid} and title like "%测试%" and deleted=0'
# 根据会议号关键词查询查询
room_number = MysqlDB().query('meeting', f'customer_id={customerid} limit 1')[0].room_number
room_number_sql = f'SELECT COUNT(1) FROM meeting WHERE room_number={room_number} and deleted=0'
#所有条件一起查询
# all_query_meetings = MysqlDB().query('meeting', f'customer_id="{customerid}" and order_start_time>="2020-08-02" and order_end_time<"2020-12-15" and type=0 and status=8 and title like "%测试%" and deleted=0')
all_query_sql = f'SELECT COUNT(1) FROM meeting WHERE customer_id={customerid} and order_start_time>="2020-08-02" and order_end_time<"2021-01-01" and type=0 and status=8 and title like "%测试%" and deleted=0'


org_meeting_search_data = [
    {'name': '根据预约时间范围查询', 'params': {'start_time': '2020-12-02', 'end_time': '2020-12-31'}, 'case_status': True, 'expected_result': f'{time_sql}'},
    {'name': '根据会议类型-平台全公开查询', 'params': {'type': '平台全公开'}, 'case_status': True, 'expected_result': f'{type_sql_2}'},
    {'name': '根据会议类型-机构全公开查询', 'params': {'type': '机构全公开'}, 'case_status': True, 'expected_result': f'{type_sql_1}'},
    {'name': '根据会议类型-白名单查询', 'params': {'type': '白名单'}, 'case_status': True, 'expected_result': f'{type_sql_3}'},
    {'name': '根据会议状态-未开始查询', 'params': {'status': '未开始'}, 'case_status': True, 'expected_result': f'{status_sql_1}'},
    {'name': '根据会议状态-会议中查询', 'params': {'status': '会议中'}, 'case_status': True, 'expected_result': f'{status_sql_2}'},
    {'name': '根据会议状态-已结束查询', 'params': {'status': '已结束'}, 'case_status': True, 'expected_result': f'{status_sql_3}'},
    {'name': '根据会议主题关键词查询', 'params': {'keywords': '测试'}, 'case_status': True, 'expected_result': f'{keywords_sql}'},
    {'name': '根据会议号关键词查询', 'params': {'keywords': f'{room_number}'}, 'case_status': True, 'expected_result': f'{room_number_sql}'},
    {'name': '根据所有条件一起查询', 'params': {'org': 'web自动化测试机构','start_time': '2020-08-02', 'end_time': '2020-12-31','type': '平台全公开','status': '已结束','keywords': '测试'}, 'case_status': True, 'expected_result': f'{all_query_sql}'},

]
