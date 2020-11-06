import requests,json,time
import sys
#sys.path.append("..")
from my_jump import ssh_jump
if __name__=="__main__":
    cmds = ['sudo mkdir test','git clone https://github.com/ChaiYuHerng/free5gc-stage3.git']
    IP = '172.24.4.85'
    ssh_jump(IP,cmds)