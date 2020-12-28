import os
import time
from main import main_dir


def screenshoot(driver, img_name):
    folder = time.strftime("%Y%m%d%H%M%S", time.localtime())
    os.makedirs(f'{main_dir}/report/screen_shoot/{folder}')
    driver.save_screenshot(
        f'{main_dir}/report/screen_shoot/{folder}/{img_name}-{time.strftime("%Y%m%d%H%M%S", time.localtime())}.png')
