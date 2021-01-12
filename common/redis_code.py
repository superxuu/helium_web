import requests
from redis.sentinel import Sentinel
import json

REDIS = {"host": '11.8.37.73', "port": 6379,
         "password": "ztone",
         "nodes": [('11.8.36.59', 26379),  # 哨兵集群
                   ('11.8.37.73', 26379),  # 主
                   ('11.8.37.28', 26379)],
         "mode": "Sentinel"}


def get_captcha_code(captchaToken):
    """根据captureToken从redis集群中获取验证码"""
    key = "sc_credential_value:captcha:"
    s = requests.session()
    headers = {"Accept": "application/json"}
    # response = s.get(host+"/captcha/send",headers=headers).json()
    # captchaToken = response["captchaToken"]
    sentinel = Sentinel(REDIS["nodes"])
    red = sentinel.slave_for('mymaster', socket_timeout=0.5, password=REDIS["password"])
    captcha_code = red.get(key + captchaToken)
    return captcha_code.decode()


def get_captcha_token(driver, url):
    """Selenium Wire获取底层响应"""
    import json
    for request in driver.requests:
        if request.url == url:
            res = request.response.body.decode('UTF8')
            return json.loads(res)
    print(f'未找到指定url:{url}')
    return None


# def get_captcha_token1(result):
#     """代理方法获取验证码的captureToken"""
#     for entry in result['log']['entries']:
#         # print(entry)
#         _url = entry['request']['url']
#         # print(_url)
#         if "http://11.8.40.108:8083/ztone/captcha/send" in _url:
#             _response = entry['response']['content']['text']
#             return json.loads(_response)
#
#
# def get_response(driver, url):
#     """webdriver API方法获取验证码的captureToken，使用这个"""
#     import json
#     request_log = driver.get_log('performance')
#     # print(request_log)
#     for i in range(len(request_log)):
#         message = json.loads(request_log[i]['message'])
#         message = message['message']['params']
#         # .get() 方式获取是了避免字段不存在时报错
#         request = message.get('request')
#         if (request is None):
#             continue
#
#         _url = request.get('url')
#         if (_url == url):
#             # 得到requestId
#             # print(message['requestId'])
#             # 通过requestId获取接口内容
#             content = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': message['requestId']})
#             return json.loads(content['body'])
#
#     print(f'未找到指定url:{url}')
#     return None


if __name__ == '__main__':
    captcha_code = get_captcha_code()
    print(captcha_code)
