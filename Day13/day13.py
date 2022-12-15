def is_int(inp):
    return type(inp) == type(int())

def is_list(inp):
    return type(inp) == type(list())

def convert_int_item(i,j):
    """Convert the int-item i or j to a list"""
    if is_int(i):
        i = [i]
    elif is_int(j):
        j = [j]
    else:
        print('Error: should call function for int items only')
        exit()
    return [i, j]
    
def compare_lists(pair,order):
    value_check = False

    for k,(i,j) in enumerate(zip(pair[0],pair[1])):
        test_list = [is_list(i), is_list(j)]
        if all(test_list):
            order = compare_lists([i,j],order)
        elif any(test_list):
            order = compare_lists(convert_int_item(i,j),order)
        elif i<j:
            value_check = True
        elif i>j:
            return False
    
    # Edge cases:
    # Second list is empty, first one is not
    # if len(pair[0]) > len(pair[1]) and k>=0:   
    #     return False

    # Second list has equal numbers as first but is shorter
    if not value_check and len(pair[0]) > len(pair[1]):
        return False

    if not (bool(pair[1])):
        return False

    return order
    # if k<=max(pair[0])
    # if len(pair[1]) >= len(pair[0]):
    # else:

    
    # # Finally test if the pair[1] was exhausted before pair[0]:
    # if not bool(pair[1]):
    #     return False


    # if len(pair[1]) >= len(pair[0]):
    #     # print('Pair: ', pair, 'is in the right order')
    #     return order
    # elif not bool(pair[1]):
    #     return False
    # else:
    #     return order

myfile = 'input.txt'
with open(myfile, 'r') as file:
    data = file.read().split('\n\n')

pair_data = list()

while data:
    single_pair_data= eval(str(data[0].split()))
    pair_data.append([eval(single_pair_data[0]), eval(single_pair_data[1]) ])
    # print(pair_data)
    data.pop(0)

order_is_right = [True]*len(pair_data)
for i,pair in enumerate(pair_data):
    order_is_right[i] = compare_lists(pair,order_is_right[i])

print(sum([i+1 for i, x in enumerate(order_is_right) if x == True]))
      
