
login_data = [
        {'name': '所有参数正确，登陆成功', 'params': {'name': 'test', 'pwd': '123zxc', 'capture': None}, 'case_status': True, 'expected_result': 'Button("预约会议").exists()'},
        {'name': '用户名错误，登陆失败', 'params': {'name': 'test1', 'pwd': '123zxc', 'capture': None}, 'case_status': False, 'expected_result': 'Text("用户名或密码错误").exists()'},
        {'name': '密码错误，登陆失败', 'params': {'name': 'test', 'pwd': '123zxc1', 'capture': None}, 'case_status': False, 'expected_result': 'Text("用户名或密码错误").exists()'},
        {'name': '验证码错误，登陆失败', 'params': {'name': 'test', 'pwd': '123zxc', 'capture': '0000'}, 'case_status': False, 'expected_result': 'Text("验证码输入错误").exists()'},
        {'name': '用户名为空，登陆失败', 'params': {'name': '', 'pwd': '123zxc', 'capture': None}, 'case_status': False, 'expected_result': 'Text("请输入用户名").exists()'},
        {'name': '密码为空，登陆失败', 'params': {'name': 'test', 'pwd': '', 'capture': None}, 'case_status': False, 'expected_result': 'Text("密码不能少于3位").exists()'},
        {'name': '验证码为空，登陆失败', 'params': {'name': 'test', 'pwd': '123zxc', 'capture': ''}, 'case_status': False, 'expected_result': 'Text("验证码不对").exists()'},
    ]
