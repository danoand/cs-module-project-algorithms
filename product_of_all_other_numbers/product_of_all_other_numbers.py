'''
Input: a List of integers
Returns: a List of integers
'''
def foo():
    pass

def product_of_all_other_numbers(arr):
    #* Special Case: just one element in arr
    if len(arr) == 0 or len(arr) == 1:
        return [1]

    #* Special Case: just two elements in arr
    if len(arr) == 2:
        return [arr[1], arr[0]]

    #* General Case: three or more elements in arr
    # working dict/map multiplying consecutive array elements - going forward in the array
    fwd_dict                = {}
    # working dict/map multiplying consecutive array elements - going backward in the array
    bwd_dict                = {}
    # Declare the return array object
    ret_arr                 = []

    # Iterate through the array 
    for idx in range(len(arr)):
        # Treat the first element as special case
        if idx == 0:
            fwd_dict[0]          = arr[0]
            bwd_dict[len(arr)-1] = arr[len(arr)-1]
            continue

        # Treat subsequent elements
        fwd_dict[idx]               = arr[idx]*fwd_dict[idx-1]
        bwd_dict[len(arr)-1-idx]    = arr[len(arr)-1-idx]*bwd_dict[len(arr)-idx]

    # Handle all indices EXCEPT the first array index and the last
    for idx in range(1, len(arr)-1):
        # For each indexed position in the array...
        #   calculate the product of all of the values BEFORE the array position
        #   times all of the values AFTER the array position 
        ret_arr.append(fwd_dict[idx-1]*bwd_dict[idx+1])
    
    # Add the first array index and the last array index values
    ret_arr.insert(0, bwd_dict[1])
    ret_arr.append(fwd_dict[len(arr)-2])

    # Return the array
    return ret_arr

#if __name__ == '__main__':
#    # Use the main function to test your implementation
#    # arr = [1, 2, 3, 4, 5]
#    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]
#
#    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
