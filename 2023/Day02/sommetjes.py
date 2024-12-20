# sommetjes.py
from random import randint, choice

goed = ['Goedzo!', 'Yeah!', 'cool', 'frenk','banaaaaaaaaaaan','hoi hoi']
fout = ['Jammer!', 'Boooeeehh', 'helaas pindakaas','ha ha lekker voor je']


N = int(input('Hoeveel sommen wil je maken? '))
score = 0
for _ in range(N):
    a = randint(0,0)
    b = randint(0,0)
    c = int(input(f'Wat is de uitkomst van {a} x {b}? '))
    if c == a*b:
        print(choice(goed))
        score = score + 1
    else:
        print(choice(fout))

print(f'\nGoed gedaan, je score was {score}')
