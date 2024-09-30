#!/usr/bin/python3
from random import randint,choice
name = ['ALEX', 'KEVIN', 'ART', 'KAT', 'ASHLEY', 'LUCAS', 'RYDER']

for i in range(20):
    base = str(randint(100,999)) + ' ' + str(randint(100,999)) + '-' + str(randint(100,999))
    number = randint(1,26)
    with open('{} {}_{}.wav'.format(base,choice(name),number), 'w') as file:
        file.write('')

for i in range(20):
    base = str(randint(100,999))
    number = randint(1,26)
    with open('{} {}_{}.wav'.format(base,choice(name),number), 'w') as file:
        file.write('')

for i in range(10):
    base = '00' + str(randint(1,9))
    number = randint(1,26)
    with open('{} {}_{}.wav'.format(base,choice(name),number), 'w') as file:
        file.write('')

# 178 101-102 SOFIA_01.wav	180 101-102 SOFIA_02.wav
# 178 101-102 SOFIA_02.wav	180 101-102 SOFIA_03.wav
# 178 101-102 SOFIA_03.wav	file-renaming-python.py
# 178 101-102 SOFIA_04.wav