from common.mysql_connect import MysqlDB

time_count = MysqlDB().sql_query("SELECT count(*) FROM user u, user_detail d WHERE u.create_time>='2020-12-01' and u.create_time<'2020-12-31' and u.deleted=0 and u.id = d.user_id")[0]
all_count = MysqlDB().sql_query("SELECT count(*) FROM user u, user_detail d WHERE  u.deleted=0 and u.id = d.user_id")[0]
not_active_count = MysqlDB().sql_query("SELECT count(*) FROM user u, user_detail d WHERE u.active=0 and u.deleted=0 and u.id = d.user_id")[0]
active_count = MysqlDB().sql_query("SELECT count(*) FROM user u, user_detail d WHERE u.active=1 and u.deleted=0 and u.id = d.user_id")[0]
keywords_count1 = MysqlDB().sql_query("SELECT count(*) FROM user u, user_detail d WHERE u.id = d.user_id and u.deleted=0 and (u.phone_number='miaojy' or d.nick_name='miaojy')")[0]
keywords_count2 = MysqlDB().sql_query("SELECT count(*) FROM user u, user_detail d WHERE u.id = d.user_id and u.deleted=0 and (u.phone_number='13564265102' or d.nick_name='13564265102')")[0]


user_list_search_data = [
    {'name': '根据创建时间范围搜索用户列表', 'params': {'start_time': '2020-12-01', 'end_time': '2020-12-30'}, 'expected_result': f'共 {time_count} 条'},
    {'name': '根据激活状态：全部，搜索用户列表', 'params': {'active':'全部'}, 'expected_result': f'共 {all_count} 条'},
    {'name': '根据激活状态：未激活，搜索用户列表', 'params': {'active':'未激活'}, 'expected_result': f'共 {not_active_count} 条'},
    {'name': '根据激活状态：已激活，搜索用户列表', 'params': {'active':'已激活'}, 'expected_result': f'共 {active_count} 条'},
    {'name': '根据用户名关键词搜索用户列表', 'params': {'keywords':'miaojy'}, 'expected_result': f'共 {keywords_count1} 条'},
    {'name': '根据手机号关键词搜索用户列表', 'params': {'keywords':'13564265102'}, 'expected_result': f'共 {keywords_count2} 条'},

]