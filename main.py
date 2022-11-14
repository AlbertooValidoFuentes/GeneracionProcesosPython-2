import platform
import sys
import subprocess

sistema = platform.system()

if (sistema == 'Windows') :
    print(subprocess.run('ping 8.8.8.8', shell=True))
elif (sistema == 'Linux'):
    print(subprocess.run('ping 8.8.8.8 -c 3', shell=True))

