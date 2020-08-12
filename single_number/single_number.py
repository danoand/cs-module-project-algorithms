'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    wrk_dict = {}

    # Iterate through the array
    for elm in arr:
        if elm in wrk_dict:
            del wrk_dict[elm]
        else:
            wrk_dict[elm] = 0
    
    # Return the only key from the dict (presumably)
    for key in wrk_dict:
        return key

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")