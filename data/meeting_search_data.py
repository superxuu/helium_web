from common.mysql_connect import MysqlDB

#根据机构查询会议
customerid = MysqlDB().query('customer', 'name="北鼎股份"')[0].id
org_meetings = MysqlDB().query('meeting', f'customer_id="{customerid}" and deleted=0')

#根据预约时间范围查询会议
time_meetings = MysqlDB().query('meeting', 'order_start_time>="2020-12-02" and order_end_time<"2020-12-16" and deleted=0')

#根据会议类型-机构全公开查询
type_meetings1 = MysqlDB().query('meeting', 'type=2 and deleted=0')
#根据会议类型-平台全公开查询
type_meetings2 = MysqlDB().query('meeting', 'type=0 and deleted=0')
#根据会议类型-白名单查询
type_meetings3 = MysqlDB().query('meeting', 'type=1 and deleted=0')

# status:0未开始1已准备2，进行中8.已结束9.已取消
#根据会议状态-未开始查询
status_meetings1 = MysqlDB().query('meeting', 'status=0 or status=1 and deleted=0')
#根据会议状态-会议中查询
status_meetings2 = MysqlDB().query('meeting', 'status=2 and deleted=0')
#根据会议状态-已结束查询
status_meetings3 = MysqlDB().query('meeting', 'status=8 and deleted=0')

# 根据会议主题关键词查询查询
keywords_meetings1 = MysqlDB().query('meeting', 'title like "%测试%" and deleted=0')
# 根据会议号关键词查询查询
room_number = MysqlDB().query('meeting', '1 limit 1')[0].room_number

#所有条件一起查询
all_query_meetings = MysqlDB().query('meeting', f'customer_id="{customerid}" and order_start_time>="2020-08-02" and order_end_time<"2020-12-15" and type=0 and status=8 and title like "%测试%" and deleted=0')




meeting_search_data = [
    {'name': '根据所属机构查询', 'params': {'org': '北鼎股份'}, 'case_status': True, 'expected_result': f'共 {len(org_meetings)} 条'},
    {'name': '根据预约时间范围查询', 'params': {'start_time': '2020-12-02', 'end_time': '2020-12-15'}, 'case_status': True, 'expected_result': f'共 {len(time_meetings)} 条'},
    {'name': '根据会议类型-平台全公开查询', 'params': {'type': '平台全公开'}, 'case_status': True, 'expected_result': f'共 {len(type_meetings2)} 条'},
    {'name': '根据会议类型-机构全公开查询', 'params': {'type': '机构全公开'}, 'case_status': True, 'expected_result': f'共 {len(type_meetings1)} 条'},
    {'name': '根据会议类型-白名单查询', 'params': {'type': '白名单'}, 'case_status': True, 'expected_result': f'共 {len(type_meetings3)} 条'},
    {'name': '根据会议状态-未开始查询', 'params': {'status': '未开始'}, 'case_status': True, 'expected_result': f'共 {len(status_meetings1)} 条'},
    {'name': '根据会议状态-会议中查询', 'params': {'status': '会议中'}, 'case_status': True, 'expected_result': f'共 {len(status_meetings2)} 条'},
    {'name': '根据会议状态-已结束查询', 'params': {'status': '已结束'}, 'case_status': True, 'expected_result': f'共 {len(status_meetings3)} 条'},
    {'name': '根据会议主题关键词查询', 'params': {'keywords': '测试'}, 'case_status': True, 'expected_result': f'共 {len(keywords_meetings1)} 条'},
    {'name': '根据会议号关键词查询', 'params': {'keywords': f'{room_number}'}, 'case_status': True, 'expected_result': f'共 1 条'},
    {'name': '根据所有条件一起查询', 'params': {'org': '北鼎股份','start_time': '2020-08-02', 'end_time': '2020-12-15','type': '平台全公开','status': '已结束','keywords': '测试'}, 'case_status': True, 'expected_result': f'共 {len(all_query_meetings)} 条'},

]
