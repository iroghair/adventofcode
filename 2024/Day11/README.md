# day11

## Part 1

My initial attempt was to build a long array following the rules provided. For 25 steps, this took a bit of time but resulted in the correct answer. Note that inserting a number into the array while traversing it does not play nice. In principle, the new stones could be added to the end of the list (there is no connection between neighbors).

## Part 2

Making a compete list again failed at step ~28. So I build a global dictionary map to track how a particular stone number would evolve in the next step:

```{python}
def check_and_add(stone: int) -> None:
    if stone not in blink.keys():
        strnum = str(stone)
        if len(strnum)%2 == 0: # Split stone into left and right
            left = int(strnum[:len(strnum)//2])
            right = int(strnum[len(strnum)//2:])
            blink[stone] = {"result":  [left,right], "count": 0}
            check_and_add(left)
            check_and_add(right)
        else:
            blink[stone] = {"result": [stone * 2024], "count": 0}
            check_and_add(stone * 2024)
    return
```

Then, I add a counter to the dictionary `blink` and visit for every stone recursively the resulting stones, adding 1 to the count once the 75th step is reached:

```{python}
def recurse_stone_to_step(stone,step):
    resulting_stones = blink[stone]["result"]
    for rs in resulting_stones:
        if step == 1:
            blink[rs]["count"] += 1
        else:
            recurse_stone_to_step(rs,step-1)
```

This is quite slow, but doesn't run out of memory. 

My last attempt is keeping much less information (a pity, it would be nice to know how many of each stone exist):

```{python}
def recurse_stone_to_step(stone,step) -> int:
    resulting_stones = blink[stone]["result"]
    if step == 1:
        return len(resulting_stones)
    else:
        return sum([recurse_stone_to_step(rs,step-1) for rs in resulting_stones])
```

Still takes long, except with function caching from `functools`:

```{python}
def recurse_stone_to_step(stone,step) -> int:
    ...
```

Then, the run times are as follows:

```
(jupyterlab) ivo@wslap:~/Development/GitHub/adventofcode/2024/Day11$ time python3 day11.py 
[6563348, 67, 395, 0, 6, 4425, 89567, 739318]
Part 1: 0
Part 2: 220357186726677

real    0m0.442s
user    0m0.600s
sys     0m0.977s

```