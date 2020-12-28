import os
import subprocess

import click
import pytest
import platform

current_dir = os.getcwd()  # 生成报告和错误截图时使用
main_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
print(main_dir)

@click.command()
@click.option("-m", default='admin', help="pytest mark")
def main(m):
    args = [main_dir,'-m', f'{m}', f'--alluredir={current_dir}/report/allure-results', '--clean-alluredir']
    # args = ['-m', f'{m}']
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

