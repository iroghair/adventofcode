import numpy as np

def thetest(array):
    # Initialize the variables
    cumulative_sum = 0
    index = 0
    
    # Use a while loop to sum the elements until the cumulative sum exceeds $a
    while cumulative_sum <= 223:
        cumulative_sum += array[index]
        index += 1
    
    # Calculate the sum of the remaining elements
    sum_of_remaining = np.sum(array[index:])
    return sum_of_remaining

def sum_remaining_elements(array):
    s = 0
    while True:
        s += array.pop(0)
        if s > 223:
            break
    return sum(array)

    
a = [200,20,1,2,3,4,2]
print(sum_remaining_elements(a.copy()), thetest(np.array(a)))