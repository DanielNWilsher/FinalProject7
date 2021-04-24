'''
sequential
'''
'''
cs-1410
project 7
Daniel Wilsher
this is my original work
'''

time.perf_counter()

import random
import subprocess
from pathlib import Path

def main():
    with open('flags.txt', 'r') as f:
        flagList = f.read().splitlines()

    allFlags = list()

    for theFlag in flagList:
        allFlags.append(theFlag)

'''
while len(allFlags) < len(flagList):
    random_flag = random.choice(flagList)
    if random_flag not in allFlags:
        allFlags.append(random_flag)
'''

    for Flag in allFlags:
        pipe = subprocess.run(["curl",'https://www.countryflags.com/wp-content/uploads/' + Flag + '-flag-png-large.png',"-o","flags/" + Flag], stderr=open('EmptyFile'))

    byteTotal = 0
    filePath = './flags/'
    for Flag in allFlags:
    '''byteCount = os.stat(Flag).st_size '''
        byteCount = Path(filePath + Flag).stat().st_size
        byteTotal += byteCount

    print('Total bytes downloaded: ' + str(byteTotal))




if __name__ == '__main__':
    main()


'''
import os
https://www.countryflags.com/wp-content/uploads/VARIABLE-flag-png-large.png
import subprocess
subprocess.run()
for num in _:
    with open('num.png', 'w') as f:
        p1 = subprocess.run(['ls, lr'], stdout=f, text=True)
'''




