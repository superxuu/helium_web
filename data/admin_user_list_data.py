
# time_count = MysqlDB().sql_query("SELECT count(*) FROM user u, user_detail d WHERE u.create_time>='2020-12-01' and u.create_time<'2020-12-31' and u.deleted=0 and u.id = d.user_id")[0]
time_sql = "SELECT count(*) FROM user u, user_detail d WHERE u.create_time>='2020-12-01' and u.create_time<'2020-12-31' and u.deleted=0 and u.id = d.user_id"
# all_count = MysqlDB().sql_query("SELECT count(*) FROM user u, user_detail d WHERE  u.deleted=0 and u.id = d.user_id")[0]
all_sql = "SELECT count(*) FROM user u, user_detail d WHERE  u.deleted=0 and u.id = d.user_id"
# not_active_count = MysqlDB().sql_query("SELECT count(*) FROM user u, user_detail d WHERE u.active=0 and u.deleted=0 and u.id = d.user_id")[0]
not_active_sql = "SELECT count(*) FROM user u, user_detail d WHERE u.active=0 and u.deleted=0 and u.id = d.user_id"
# active_count = MysqlDB().sql_query("SELECT count(*) FROM user u, user_detail d WHERE u.active=1 and u.deleted=0 and u.id = d.user_id")[0]
active_sql = "SELECT count(*) FROM user u, user_detail d WHERE u.active=1 and u.deleted=0 and u.id = d.user_id"
# keywords_count1 = MysqlDB().sql_query("SELECT count(*) FROM user u, user_detail d WHERE u.id = d.user_id and u.deleted=0 and (u.phone_number='jimmy' or d.nick_name='jimmy')")[0]
keywords_sql1 = "SELECT count(*) FROM user u, user_detail d WHERE u.id = d.user_id and u.deleted=0 and (u.phone_number='jimmy' or d.nick_name='jimmy')"
# keywords_count2 = MysqlDB().sql_query("SELECT count(*) FROM user u, user_detail d WHERE u.id = d.user_id and u.deleted=0 and (u.phone_number='86-13564265102' or d.nick_name='13564265102')")[0]
keywords_sql2 = "SELECT count(*) FROM user u, user_detail d WHERE u.id = d.user_id and u.deleted=0 and (u.phone_number='86-13564265102' or d.nick_name='13564265102')"

user_list_search_data = [
    {'name': '根据创建时间范围搜索用户列表', 'params': {'start_time': '2020-12-01', 'end_time': '2020-12-30'}, 'expected_result': f'{time_sql}'},
    {'name': '根据激活状态：全部，搜索用户列表', 'params': {'active':'全部'}, 'expected_result': f'{all_sql}'},
    {'name': '根据激活状态：未激活，搜索用户列表', 'params': {'active':'未激活'}, 'expected_result': f'{not_active_sql}'},
    {'name': '根据激活状态：已激活，搜索用户列表', 'params': {'active':'已激活'}, 'expected_result': f'{active_sql}'},
    {'name': '根据用户名关键词搜索用户列表', 'params': {'keywords':'jimmy'}, 'expected_result': f'{keywords_sql1}'},
    {'name': '根据手机号关键词搜索用户列表', 'params': {'keywords':'13564265102'}, 'expected_result': f'{keywords_sql2}'},

]