import datetime
import time

time_plus_120 = (datetime.datetime.now()+datetime.timedelta(minutes=120)).strftime("%Y-%m-%d %H:%M:%S")
add_meeting_data = [
    {'name': '正常预约会议-机构全公开-人工-on', 'params': { 'type': '机构全公开', 'title':f'web自动化测试会议-{time.strftime("%Y%m%d%H%M%S", time.localtime())}', 'introduce':'web自动化测试会议介绍','guest':'web自动化测试会议嘉宾介绍','start_time':True,'num':'50','way':'staff','audio':'on','AI':'on'}, 'case_status': True, 'expected_result': f'共 1 条'},
    {'name': '正常预约会议-白名单-自助-off', 'params': { 'type': '白名单', 'title':f'web自动化测试会议-{time.strftime("%Y%m%d%H%M%S", time.localtime())}', 'introduce':'web自动化测试会议介绍','guest':'web自动化测试会议嘉宾介绍','start_time':True,'num':'25','way':'self','audio':'off','AI':'off'}, 'case_status': True, 'expected_result': f'共 1 条'},
    {'name': '正常预约会议-提前20分钟预约','params': {'type': '机构全公开', 'title': f'web自动化测试会议-{time.strftime("%Y%m%d%H%M%S", time.localtime())}','introduce': 'web自动化测试会议介绍', 'guest': 'web自动化测试会议嘉宾介绍', 'start_time': time_plus_120, 'num': '50', 'way': 'staff','audio': 'on', 'AI': 'on'}, 'case_status': True, 'expected_result': f'共 1 条'},

]