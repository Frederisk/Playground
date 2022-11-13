import os

print('Hello World!')

status = os.system('command -V docker')

if status:
    raise Exception('docker NOT FOUND!')

raise Exception('Force Failed!')
# os.system('command -V ')
