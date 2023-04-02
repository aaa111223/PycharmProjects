# coding ="utf-8"
from locust import task, between, FastHttpUser, run_single_user
import logging



class MyUser(FastHttpUser):
    wait_time = between(1, 3)
    host = "http://appserver.huice.com"

    @task(1)
    def index(self):
        url = "/"
        with self.client.get(url=url, name="打开首页", catch_response=True ) as res:
            if res.status_code == 200:
                res.success()
            else:
                res.failure(f"首页打开失败 Failure {res.status_code}")

    @task(1)
    def login(self):
        json = {
                    "email": "3@test.cn",
                    "password": "12345678",
                    "captcha":""
                }
        url = "/customer/login/account"
        with self.client.post(url=url, json=json, name="登录", catch_response=True) as res2:
            if res2.status_code == 200:
                res2.success()
                logging.info(f'/customer/account/login错误信息:{res2.content}')
            else:
                res2.failure(f"用户登录失败 Failure {res2.status_code}")
                # logging.info(f"/customer/account/login错误信息:" f"{res2.headers}")




# if launched directly, e.g. "python3 debugging.py", not "locust -f debugging.py"
# if __name__ == "__main__":
#     run_single_user(MyUser)
