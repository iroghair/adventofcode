import numpy as np

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
    
def curate_leaf_int(pair):
    new_pair = pair.copy()
    value_check = False

    for k,(i,j) in enumerate(zip(pair[0],pair[1])):
        test_list = [is_list(i), is_list(j)]
        if all(test_list):
            new_pair = curate_leaf_int([i,j])
        elif any(test_list):
            new_pair = curate_leaf_int(convert_int_item(i,j))
    return new_pair

def compare_lists(pair,order):
    for p in range(2):
        for (i,item) in enumerate(pair[p]):
            if type(item)==type(list()):
                pair[p][i] = np.array(item)

        # return np.all(pair[0] <= pair[1])
        
    for (i,j) in enumerate(zip(pair[0],pair[1])):
        test_list = [is_list(i), is_list(j)]
        if all(test_list):
            order = compare_lists([i,j],order)
        elif any(test_list):
            order = compare_lists(convert_int_item(i,j),order)
    
    return 
    # # Second list has equal numbers as first but is shorter
    # if not value_check and len(pair[0]) == 0:
    #     return True

    # if not (bool(pair[1])):
    #     return False

    # return order
    # # if k<=max(pair[0])
    # # if len(pair[1]) >= len(pair[0]):
    # # else:

    
    # # # Finally test if the pair[1] was exhausted before pair[0]:
    # # if not bool(pair[1]):
    # #     return False


    # # if len(pair[1]) >= len(pair[0]):
    # #     # print('Pair: ', pair, 'is in the right order')
    # #     return order
    # # elif not bool(pair[1]):
    # #     return False
    # # else:
    # #     return order

myfile = 'test.txt'
with open(myfile, 'r') as file:
    data = file.read().split('\n\n')

pair_data = list()

while data:
    single_pair_data= eval(str(data[0].split()))
    pair_data.append(np.array([eval(single_pair_data[0]), eval(single_pair_data[1]) ]))
    # print(pair_data)
    data.pop(0)

order_is_right = [True]*len(pair_data)
pair_data_corr = []
for i,pair in enumerate(pair_data):
    order_is_right[i] = compare_lists(pair,order_is_right[i])
    # pair_data_corr.append(curate_leaf_int(pair)) 

print(sum([i+1 for i, x in enumerate(order_is_right) if x == True]))
      
