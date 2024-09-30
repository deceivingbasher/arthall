#!/usr/bin/python3
from random import randint,choice
name = ['ALEX', 'KEVIN', 'ART', 'KAT', 'ASHLEY', 'LUCAS', 'RYDER']

for i in range(50):
    base = '00' + str(randint(1,9))
    number = randint(1,26)
    with open('{} {}_{}'.format(base,choice(name),number), 'w') as file:
        file.write('')
