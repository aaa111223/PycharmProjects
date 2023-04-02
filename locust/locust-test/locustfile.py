# coding ="utf-8"
from locust import HttpUser, task, between, FastHttpUser, run_single_user
import logging,sys



class MyUser(FastHttpUser):
    # wait_time = between(1, 3)
    host = "http://appfront.huice.com"

    @task(1)
    def index(self):
        """
        首页
        """
        host = "http://appfront.huice.com"
        # url = "/"
        with self.client.get(host, catch_response=True ) as res:
            if res.status_code == 200:
                res.success()
            else:
                res.failure(f"首页打开失败 Failure {res.status_code}")

    @task(1)
    def login(self):
        """
        表单数据：
        editForm[email]: 3@test.cn
        editForm[password]: 12345678
        _csrf: UHFs_GujO8QaCzeo84RdSylSDWjUk8DCFFumUe1xOjsJLh6pMcJOqlJSX-KR9yk_Qjg-Ba768LIidugWrkRzcQ==
        """

        json = {"editForm[email]": "3@test.cn",
                "editForm[password]": 12345678,
                "_csrf": "UHFs_GujO8QaCzeo84RdSylSDWjUk8DCFFumUe1xOjsJLh6pMcJOqlJSX-KR9yk_Qjg-Ba768LIidugWrkRzcQ=="
                }

        url = "http://appfront.huice.com/customer/account/login"
        header = {"Cookie":"_csrf=e620e9bd2500d3c96b34e5cda7cb23bae295c96dd175b9f292bdb49b741572e2a:2:{i:0;s:5:\"_csrf\";i:1;s:32:\"MCPHiGcwXKnFjmLG8Xv39PcJlRqctUPQ\";}; PHPSESSID=e6e02d5e69e786936296071e5f805de3"}
        with self.client.post(url, json, header=header, catch_response=True) as res2:
            if res2.status_code == 200:
                res2.success()

                res2.headers
            else:
                res2.failure(f"用户登录失败 Failure {res2.status_code}")
                # logging.info(f"/customer/account/login错误信息:" f"{res2.headers}")


# if launched directly, e.g. "python3 debugging.py", not "locust -f debugging.py"
if __name__ == "__main__":

    run_single_user(MyUser)
