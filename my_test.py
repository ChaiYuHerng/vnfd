#! /usr/bin/env python3
import sys
import os
import paramiko
import time
#sys.path.append("..")
def ssh_jump(target_addr,cmds):

    print("now in the ssh_jump")
    key=paramiko.RSAKey.from_private_key_file('cloud.key')

    print("key is OK")

    jumpbox=paramiko.SSHClient()
    jumpbox.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    jumpbox.connect('192.168.1.250', username='chris', password='ci9761')

    jumpbox_transport = jumpbox.get_transport()
    src_addr = ('192.168.1.250', 22)
    dest_addr = (target_addr, 22)
    jumpbox_channel = jumpbox_transport.open_channel("direct-tcpip", dest_addr, src_addr)

    target=paramiko.SSHClient()
    target.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    target.connect(target_addr, username='ubuntu', pkey=key, sock=jumpbox_channel)
    ssh = target.invoke_shell()
    for cmd in cmds:
        if cmd=='sudo nohup ./bin/free5gc-upfd\n':
            time.sleep(20)
        else:
            time.sleep(1)
        ssh.send(cmd)
        #out=ssh.recv(1024)
        #print out
    time.sleep(1)

    target.close()
    jumpbox.close()
if __name__=="__main__":
    print('start')
    cmds = ['ls\n','sudo mkdir test\n','git clone https://github.com/ChaiYuHerng/free5gc-stage3.git\n','exit\n']
    IP = '172.24.4.85'
    ssh_jump(IP,cmds)
    print('end')