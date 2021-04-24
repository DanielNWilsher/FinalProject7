'''
concurrently using processes
'''
'''
cs-1410
project 7
Daniel Wilsher
this is my original work
'''
import random
import subprocess
from pathlib import Path


with open('flags.txt', 'r') as f:
    flagList = f.read().splitlines()

tenFlags = list()

while len(tenFlags) < 10:
    random_flag = random.choice(flagList)
    if random_flag not in tenFlags:
        tenFlags.append(random_flag)

for Flag in tenFlags:
    pipe = subprocess.run(["curl",'https://www.countryflags.com/wp-content/uploads/' + Flag + '-flag-png-large.png',"-o","flags/" + Flag], stderr=open('EmptyFile'))

byteTotal = 0
filePath = './flags/'
for Flag in tenFlags:
    '''byteCount = os.stat(Flag).st_size '''
    byteCount = Path(filePath + Flag).stat().st_size
    byteTotal += byteCount

print('Total bytes downloaded: ' + str(byteTotal))


'''
import os
https://www.countryflags.com/wp-content/uploads/VARIABLE-flag-png-large.png
import subprocess
subprocess.run()
for num in _:
    with open('num.png', 'w') as f:
        p1 = subprocess.run(['ls, lr'], stdout=f, text=True)
'''
