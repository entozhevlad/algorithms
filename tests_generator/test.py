from os import popen
import random

while True:
    test = random.randint(1, 100)
    slow = popen("echo {} | python slow.py".format(test)).read()
    wrong = popen("echo {} | python wrong.py".format(test)).read()

    if int(slow) != int(wrong):
        print('WA')
        print('Slow:', slow)
        print('Wrong:', wrong)
        break
