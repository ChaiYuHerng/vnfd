import requests,json,time
import sys
#sys.path.append("..")
from my_jump import ssh_jump
if __name__=="__main__":
    cmds = ['ls\n','sudo mkdir test\n','git clone https://github.com/ChaiYuHerng/free5gc-stage3.git\n','exit\n']
    IP = '172.24.4.85'
    ssh_jump(IP,cmds)