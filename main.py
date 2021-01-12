import os
import subprocess

import click
import pytest
import platform

current_dir = os.getcwd()  # 生成报告和错误截图时使用
main_dir = os.path.dirname(os.path.abspath(__file__))
print('当前路径：', current_dir)
print('案例查找路径：', main_dir)

@click.command()
@click.option("-m", default='admin', help="pytest mark")
@click.option("-B", default='Chrome', help="browser option: Firefox or Chrome")
def main(m,b):
    args = [main_dir,'-m', m,'-B',b, f'--alluredir={current_dir}/report/allure-results', '--clean-alluredir']
    pytest.main(args)
    if (platform.system() == 'Windows'):
        subprocess.Popen(['allure', 'generate', f'{current_dir}/report/allure-results', '--clean', '-o',
                          f'{current_dir}/report/allure-report'], shell=True)
    elif (platform.system() == 'Linux'):
        subprocess.Popen(['allure', 'generate', f'{current_dir}/report/allure-results', '--clean', '-o',
                          f'{current_dir}/report/allure-report'], shell=False)
    print('Done!!!')

if __name__ == '__main__':
    main()

