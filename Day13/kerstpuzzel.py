from caesarcipher import CaesarCipher
from math import perm
# 
for i in range(26):
    cipher2 = CaesarCipher('DDGGKLSC',offset=i)
    cipher = CaesarCipher('BGNJMKY BMLBCPQ ECZYYLB EYLENYB IYLBCCJ JYQQGLE QJGBGLE YEMEGCI',offset=i)
    print(cipher2.decoded)
# a = cipher.decoded.split()
# b = perm(a)
# print(cipher.decoded.split())

# print(cipher2.cracked)
# print(cipher.cracked)
