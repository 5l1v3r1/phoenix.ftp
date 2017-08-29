import sys
import os
from core import colors


def execute(command):
    os.system(command)


def install():
    #execute("apt-get update")
    print colors.color.GREEN + "** Installing wine.."+ colors.color.ENDC
    execute("apt-get install wine")
    print colors.color.GREEN + "** Python setup.."+ colors.color.ENDC
    execute("wine msiexec /i reqs/python-2.7.13.msi /L*v log.txt")
    print colors.color.GREEN + "** Downloading modules.."+ colors.color.ENDC
    execute("cd reqs/ && wget https://pypi.python.org/packages/a5/ff/81c54c9f68294ee0b410f2c6efcbfc58791305460228e417657b720b0306/pyftpdlib-1.5.2.tar.gz")
    print colors.color.GREEN +"** Extarcting pyftpdlib-1.5.2.tar.gz .."+ colors.color.ENDC
    execute("tar -xvzf reqs/pyftpdlib-1.5.2.tar.gz")
    print colors.color.GREEN +"** Installing pyftpdlib.."+ colors.color.ENDC
    execute("cd pyftpdlib-1.5.2/ && pwd && wine python setup.py install")
    print colors.color.GREEN +"** Installing pyinstaller.."+ colors.color.ENDC
    execute("wine python ~/.wine/drive_c/Python27/Scripts/pip.exe install pyinstaller")
    print colors.color.GREEN + "** Installing filezilla ftp client.." + colors.color.ENDC
    execute("apt-get install filezilla")
    print colors.color.GREEN +"** Setup compete."+ colors.color.ENDC


install()
