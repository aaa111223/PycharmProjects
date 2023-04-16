import paramiko

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect('192.168.37.128', 22, username='root', password='12345678', timeout=4)
