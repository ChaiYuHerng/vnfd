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
    jumpbox.connect('192.168.1.250', username='openstack', password='ci9761')

    print("check1")

    jumpbox_transport = jumpbox.get_transport()
    src_addr = ('192.168.1.250', 22)
    dest_addr = (target_addr, 22)
    jumpbox_channel = jumpbox_transport.open_channel("direct-tcpip", dest_addr, src_addr)

    print("check2")

    target=paramiko.SSHClient()
    target.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    target.connect(target_addr, username='ubuntu', pkey=key, sock=jumpbox_channel)
    ssh = target.invoke_shell()

    print("start reading cmds")
    for cmd in cmds:
        print("now cmd is " + cmd)
        if cmd=='sudo nohup ./bin/free5gc-upfd\n':
            time.sleep(10)
        elif cmd == 'make -j`nproc`':
            time.sleep(20)
        else:
            time.sleep(2)
        cmd = cmd + '\n'
        ssh.send(cmd)
        #out=ssh.recv(1024)
        #print out
    time.sleep(1)

    target.close()
    jumpbox.close()
if __name__=="__main__":
    vnf_list = ['mongodb','upf1','upf2','upf3','nrf','amf','smf1','smf2','smf3','udr','pcf','udm','nssf','ausf']
    #vnf_list = ['test','upf3']
    print("start")
    for vnf in vnf_list:
        if vnf == 'mongodb':
            cmds=['sudo systemctl unmask mongodb','sudo systemctl restart mongod','exit']
            IP = '172.24.4.110'
        elif vnf == 'test':
            cmds=['mkdir test','exit']
            IP = '172.24.4.23'
        elif vnf == 'upf1':
            cmds=['cd gtp5g','make','sudo make install','cd ../free5gc-stage3/src/upf','mkdir build','cd build','cmake ..','make -j`nproc`','cd config','rm upfcfg.yaml','cd ../../../..','mv upf1.yaml src/upf/build/config/upfcfg.yaml','cd src/upf/build','sudo sysctl -w net.ipv4.ip_forward=1','sudo iptables -t nat -A POSTROUTING -o ens3 -j MASQUERADE','sudo systemctl stop ufw','sudo nohup ./bin/free5gc-upfd & ','exit']
            IP = '172.24.4.111'
        elif vnf == 'upf2':
            cmds=['cd gtp5g','make','sudo make install','cd ../free5gc-stage3/src/upf','mkdir build','cd build','cmake ..','make -j`nproc`','cd config','rm upfcfg.yaml','cd ../../../..','mv upf2.yaml src/upf/build/config/upfcfg.yaml','cd src/upf/build','sudo sysctl -w net.ipv4.ip_forward=1','sudo iptables -t nat -A POSTROUTING -o ens3 -j MASQUERADE','sudo systemctl stop ufw','sudo nohup ./bin/free5gc-upfd & ','exit']
            IP = '172.24.4.112'
        elif vnf == 'upf3':
            cmds=['cd gtp5g','make','sudo make install','cd ../free5gc-stage3/src/upf','mkdir build','cd build','cmake ..','make -j`nproc`','cd config','rm upfcfg.yaml','cd ../../../..','mv upf3.yaml src/upf/build/config/upfcfg.yaml','cd src/upf/build','sudo sysctl -w net.ipv4.ip_forward=1','sudo iptables -t nat -A POSTROUTING -o ens3 -j MASQUERADE','sudo systemctl stop ufw','sudo nohup ./bin/free5gc-upfd & ','exit']
            IP = '172.24.4.113'
        elif vnf == 'upf1':
            cmds=['cd gtp5g','make','sudo make install','cd ../free5gc-stage3/src/upf','mkdir build','cd build','cmake ..','make -j`nproc`','cd config','rm upfcfg.yaml','cd ../../../..','mv upf4.yaml src/upf/build/config/upfcfg.yaml','cd src/upf/build','sudo sysctl -w net.ipv4.ip_forward=1','sudo iptables -t nat -A POSTROUTING -o ens3 -j MASQUERADE','sudo systemctl stop ufw','sudo nohup ./bin/free5gc-upfd & ','exit']
            IP = '172.24.4.114'
        elif vnf == 'upf1':
            cmds=['cd gtp5g','make','sudo make install','cd ../free5gc-stage3/src/upf','mkdir build','cd build','cmake ..','make -j`nproc`','cd config','rm upfcfg.yaml','cd ../../../..','mv upf5.yaml src/upf/build/config/upfcfg.yaml','cd src/upf/build','sudo sysctl -w net.ipv4.ip_forward=1','sudo iptables -t nat -A POSTROUTING -o ens3 -j MASQUERADE','sudo systemctl stop ufw','sudo nohup ./bin/free5gc-upfd & ','exit']
            IP = '172.24.4.115'
        elif vnf == 'upf1':
            cmds=['cd gtp5g','make','sudo make install','cd ../free5gc-stage3/src/upf','mkdir build','cd build','cmake ..','make -j`nproc`','cd config','rm upfcfg.yaml','cd ../../../..','mv upf6.yaml src/upf/build/config/upfcfg.yaml','cd src/upf/build','sudo sysctl -w net.ipv4.ip_forward=1','sudo iptables -t nat -A POSTROUTING -o ens3 -j MASQUERADE','sudo systemctl stop ufw','sudo nohup ./bin/free5gc-upfd & ','exit']
            IP = '172.24.4.116'
        elif vnf == 'nrf':
            cmds=['cd free5gc-stage3','sudo nohup ./bin/nrf & ','exit']
            IP = '172.24.4.101'
        elif vnf == 'amf':
            cmds=['cd free5gc-stage3','sudo nohup ./bin/amf & ','exit']
            IP = '172.24.4.102'
        elif vnf == 'smf1':
            cmds=['cd free5gc-stage3','sudo nohup ./bin/smf & ','exit']
            IP = '172.24.4.103'
        elif vnf == 'smf2':
            cmds=['cd free5gc-stage3','sudo nohup ./bin/smf & ','exit']
            IP = '172.24.4.114'
        elif vnf == 'smf3':
            cmds=['cd free5gc-stage3','sudo nohup ./bin/smf & ','exit']
            IP = '172.24.4.115'
        elif vnf == 'udr':
            cmds=['cd free5gc-stage3','sudo nohup ./bin/udr & ','exit']
            IP = '172.24.4.104'
        elif vnf == 'pcf':
            cmds=['cd free5gc-stage3','sudo nohup ./bin/pcf & ','exit']
            IP = '172.24.4.105'
        elif vnf == 'udm':
            cmds=['cd free5gc-stage3','sudo nohup ./bin/udm & ','exit']
            IP = '172.24.4.106'
        elif vnf == 'nssf':
            cmds=['cd free5gc-stage3','sudo nohup ./bin/nssf & ','exit']
            IP = '172.24.4.107'
        elif vnf == 'ausf':
            cmds=['cd free5gc-stage3','sudo nohup ./bin/ausf & ','exit']
            IP = '172.24.4.108'
        ssh_jump(IP,cmds)
    print("end")