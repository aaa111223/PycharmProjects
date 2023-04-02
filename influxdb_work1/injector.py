

from influxdb import InfluxDBClient

if __name__ == '__main__':

    host, port = "192.168.37.128", 8086
    # 如果没有开启用户名和密码，则不需要填写这两个参数
    username, password = "root", "123456"
    database = "test_hello_world"
    client = InfluxDBClient(host=host, username=username, port=port, database=database, password=password)
    #client.create_database("test_hello_world")

    points = [
        {
            'measurement': 'table2',
            'tags': {
                'host': 'server01',
                'region': 'us-west'
            },
            'time': '2022-10-24T12:00:00Z',
            'fields': {
                'value': 0.64
            }
        },
        {
            'measurement': 'table3',
            'tags': {
                'host': 'server01',
                'region': 'us-west'
            },
            'time': '2022-10-24T13:00:00Z',
            'fields': {
                'value': 0.88
            }
        }
    ]
    #写入库
    client.write_points(points, database=database)
    client.close()

