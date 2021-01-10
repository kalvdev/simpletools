import platform
import subprocess

print(':D')
print('EASYPINGER')
print(':D')

def ping(host):
   
    param = '-n' if platform.system().lower()=='windows' else '-c'

    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0