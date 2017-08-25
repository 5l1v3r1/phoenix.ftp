apt-get install wine
wine msiexec /i python stuff/python-2.7.13.msi /L*v logs.txt
wine ~/.wine/drive_c/Python27/python.exe Scripts/pip.exe install pyinstaller
wine ~/.wine/drive_c/Python27/python.exe Scripts/pip.exe install pyftpdlib
wine ~/.wine/drive_c/Python27/python.exe reqs/pyftpdlib-1.5.2/setup.py install

