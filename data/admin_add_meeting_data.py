import datetime
import time

time_plus_180 = (datetime.datetime.now()+datetime.timedelta(minutes=180)).strftime("%Y-%m-%d %H:%M:%S")
add_meeting_data = [
    {'name': '正常预约会议-平台全公开-人工-on-on', 'params': {'org': 'web自动化测试机构', 'type': '平台全公开', 'title':f'web自动化测试会议-{time.strftime("%Y%m%d%H%M%S", time.localtime())}', 'introduce':'web自动化测试会议介绍','guest':'web自动化测试会议嘉宾介绍','start_time':True,'num':'50','way':'staff','audio':'on','AI':'on'}, 'case_status': True, 'expected_result': f'共 1 条'},
    {'name': '正常预约会议-机构全公开-自助-on-off', 'params': {'org': 'web自动化测试机构', 'type': '机构全公开', 'title':f'web自动化测试会议-{time.strftime("%Y%m%d%H%M%S", time.localtime())}', 'introduce':'web自动化测试会议介绍','guest':'web自动化测试会议嘉宾介绍','start_time':True,'num':'50','way':'self','audio':'on','AI':'off'}, 'case_status': True, 'expected_result': f'共 1 条'},
    {'name': '正常预约会议-白名单-自助-off-off', 'params': {'org': 'web自动化测试机构', 'type': '白名单', 'title':f'web自动化测试会议-{time.strftime("%Y%m%d%H%M%S", time.localtime())}', 'introduce':'web自动化测试会议介绍','guest':'web自动化测试会议嘉宾介绍','start_time':True,'num':'50','way':'self','audio':'off','AI':'off'}, 'case_status': True, 'expected_result': f'共 1 条'},
    {'name': '正常预约会议-提前50分钟预约', 'params': {'org': 'web自动化测试机构', 'type': '平台全公开', 'title': f'web自动化测试会议-{time.strftime("%Y%m%d%H%M%S",time.localtime())}','introduce': 'web自动化测试会议介绍', 'guest': 'web自动化测试会议嘉宾介绍', 'start_time': time_plus_180, 'num': '50', 'way': 'staff', 'audio': 'on','AI': 'on'}, 'case_status': True, 'expected_result': f'共 1 条'},

]