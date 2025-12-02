with open('2025/day01/input.txt','r') as f:
    data = f.readlines()

part1 = 0
part2 = 0
n0 = 50
for i in data:
    if i[0] == 'L':
        n0 -= int(i[1:])
        # The while-loop counts how often we pass zero while rotating
        while n0 < 0:
            # But be careful; if our previous end position was already at 0, we should not count it when the left-turn gives a negative number
            if n0 != -int(i[1:]):
                part2 += 1
            n0 += 100

    if i[0] == 'R':
        n0 += int(i[1:])
        while n0 >= 100:
            n0 -= 100
            if n0 != 0:
                part2 += 1
    print(n0)

    if n0 == 0:
        part1 += 1

# The solution p1 is the number of times it ends at 0
print(part1)
# The solution pt2 is the number it ENDS at 0, and the number it crosses through 0 together
print(part1+part2)