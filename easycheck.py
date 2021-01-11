import platform
import subprocess

systemcheck = platform.uname()

print('easycheck :D')

print(f'System: {systemcheck.system}')
print(f'Node Name: {systemcheck.node}')
print(f"Release: {systemcheck.release}")
print(f"Version: {systemcheck.version}")
print(f"Machine: {systemcheck.machine}")
print(f"Processor: {systemcheck.processor}")