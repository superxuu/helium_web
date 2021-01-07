import functools
import os
import time
from main import main_dir

time_stamp_folder = time.strftime("%Y%m%d%H%M%S", time.localtime())
os.makedirs(f'{main_dir}/report/screen_shoot/{time_stamp_folder}')


def screenshoot(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        global driver, img_name
        try:
            driver = kwargs.get('open_close_browser_with_admin_data', None) or kwargs.get(
                'open_close_browser_with_org_data', None) or kwargs.get('open_close_browser', None)
            img_name = kwargs.get('data', None).get('name', None) if kwargs.get('data', None) else fun.__defaults__[0]['name']
            print(img_name, end=' ')
            fun(*args, **kwargs)
        except Exception as e:
            driver.save_screenshot(
                f'{main_dir}/report/screen_shoot/{time_stamp_folder}/{img_name}-{time.strftime("%Y%m%d%H%M%S", time.localtime())}.png')
            raise e

    return wrapper
