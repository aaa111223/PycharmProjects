import paramiko
import telnetlib
import time
import logging

def cmpt(s1,s2):
    fmt = '%Y-%m-%d'
    t1 = time.strptime(s1,fmt)
    t2 = time.strptime(s2,fmt)
    return time.mktime(t1) - time.mktime(t2)


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.248.128","22","lw","123456")
cmd = "pwd" \
      "ls -al" \
      "ifconfig"

stdin,stdout,stderr = ssh.exec_command(cmd)
sarr = []
for line in stdout:
    print ('***' + line)
ssh.close()




