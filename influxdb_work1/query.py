from influxdb import InfluxDBClient

if __name__ == '__main__':
    host, port = "192.168.37.128", 8086
    username, password = "root", "123456"
    database = "test_hello_world"
    # headers = {
    #     'User-Agent': 'python-requests/2.24.0',
    #     'Accept': '*/*',
    #     'Connection': 'keep-alive',
    #     'Content-Type': 'application/json',
    #     'Authorization': 'Basic cm9vdDpyb290'
    # }
    client = InfluxDBClient(host=host, username=username, port=port, database=database, password=password)
    # 获取所有measurements
    # print(client.get_list_measurements())
    # 执行语句
    # sql = "SELECT value FROM table1"
    # print(list(client.query(sql).get_points()))

    result = client.query('select value from table1;', database='test_hello_world')
    print(result)
    client.close()
