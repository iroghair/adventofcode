import re
from math import floor, prod

class Monkey:
    """Create a monkey playing keep-away
    
    Key parameters:
    items: list of int, items representing worry values
    operation: string literal of the worry value change before inspection
    testvalue: monkey tests against this value to decide the receiver of the item
    throw_true, throw_false: monkey numbers to which the item is thrown
    monkeys: reference list of all monkeys
    """
    def __init__(self,items,operation,test,throw_true,throw_false,monkeys) -> None:
        self.items = items
        self.inspect = lambda old: eval(operation)
        self.testvalue = test
        self.test = lambda item_value: item_value%self.testvalue==0
        self.throw_true = throw_true
        self.throw_false = throw_false
        self.monkeys = monkeys
        self.has_inspected = 0
    
    def round(self):
        """Play a round of keep-away for the current monkey"""
        for item in self.items:
            # Adjust worry value
            worry = self.inspect(item)
            self.has_inspected += 1
            if part==1:
                # Monkey is bored, decrease worry level
                worry = floor(worry/3)
            if part==2:
                # Adjust worry level by product of test values to limit number size
                worry = worry % combined_test_value
            # Test and throw to next monkey
            if self.test(worry):
                monkeys[self.throw_true].items.append(worry)
            else:
                monkeys[self.throw_false].items.append(worry)
        self.items.clear()

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    myfile = 'input.txt'
    part = 2
    monkeys = list()

    with open(myfile, 'r') as file:
        data = file.read().split('\n\n')

    # Parse input
    while data:
        if data[0].split()[0] == "Monkey":
            items = [int(x) for x in re.findall('[0-9]+',data[0].split('\n')[1])]
            operation = data[0].split('=')[1].split('\n')[0]
            test,true_to,false_to =[int(x) for x in re.findall('[0-9]+',data[0].split('Test')[1])]
            new_monkey = Monkey(items,operation,test,true_to,false_to,monkeys)
            monkeys.append(new_monkey)
            data.pop(0)

    if part == 1:
        for _ in range(20):
            for i,monkey in enumerate(monkeys):
                print('Monkey ', i, ' has items: ', monkey)
                monkey.round()

        # Gather all inspection data into array and sort
        insp = [x.has_inspected for x in monkeys]
        insp.sort()
        print('Part 1! Inspected: ',insp, ' Product:', prod(insp[-2:]))

    if part == 2:
        combined_test_value = prod([x.testvalue for x in monkeys])
        for r in range(10000):
            print("Round: ", r)
            for monkey in monkeys:
                monkey.round()

        # Gather all inspection data into array and sort
        insp = [x.has_inspected for x in monkeys]
        insp.sort()
        print('Part 2! Inspected: ',insp, ' Product:', prod(insp[-2:]))