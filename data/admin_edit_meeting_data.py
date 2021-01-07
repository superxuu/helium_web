import datetime
import time

time_plus_120 = (datetime.datetime.now()+datetime.timedelta(minutes=120)).strftime("%Y-%m-%d %H:%M:%S")

admin_edit_meeting_data = [
    {'name': '编辑已结束会议', 'params': {'status': '已结束', 'title':f'web自动化测试会议改-{time.strftime("%Y%m%d%H%M%S", time.localtime())}','introduce':f'web自动化测试会议介绍改-{time.strftime("%Y%m%d%H%M%S", time.localtime())}','guest':f'web自动化测试会议嘉宾介绍改-{time.strftime("%Y%m%d%H%M%S", time.localtime())}'},'expected_result': '共 1 条'},
    {'name': '编辑会议中会议', 'params': {'status': '会议中', 'title':f'web自动化测试会议改-{time.strftime("%Y%m%d%H%M%S", time.localtime())}','introduce':f'web自动化测试会议介绍改-{time.strftime("%Y%m%d%H%M%S", time.localtime())}','guest':f'web自动化测试会议嘉宾介绍改-{time.strftime("%Y%m%d%H%M%S", time.localtime())}'},'expected_result': '共 1 条'},
    {'name': '编辑未开始会议', 'params': {'status': '未开始', 'title':f'web自动化测试会议改-{time.strftime("%Y%m%d%H%M%S", time.localtime())}','introduce':f'web自动化测试会议介绍改-{time.strftime("%Y%m%d%H%M%S", time.localtime())}','guest':f'web自动化测试会议嘉宾介绍改-{time.strftime("%Y%m%d%H%M%S", time.localtime())}', 'type':'机构全公开', 'start_time': time_plus_120, 'num': '100', 'way': 'self', 'audio': 'off','AI': 'off'},'expected_result': '共 1 条'},

]