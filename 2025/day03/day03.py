# Algoritme door Tommie!
with open('input.txt', 'r') as f:
    data = f.readlines()

lijst_van_oplossingen = []
for regel in data:
    regel_zonder_laatste = regel.strip()[:-1]
    print(f'{regel.strip()=}')
    
    hoogste1 = 0
    for i,getal in enumerate(map(int,regel_zonder_laatste)):
        if getal > hoogste1:
            hoogste1 = getal
            hoogste2 = 0
            for getal2 in map(int,regel.strip()[i+1:]):
                if getal2 > hoogste2:
                    hoogste2 = getal2
    oplossing_van_de_rij = hoogste1*10 + hoogste2
    lijst_van_oplossingen.append(oplossing_van_de_rij)

print(lijst_van_oplossingen)
print('Totaal: ', sum(lijst_van_oplossingen))
