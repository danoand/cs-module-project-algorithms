'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Declare two working lists (arrays)
    wrk_arr1 = []
    wrk_arr2 = []

    # Iterate through the array
    for elm in arr:
        if elm != 0:
            wrk_arr1.append(elm)
        else:
            wrk_arr2.append(elm)

    # Return a list of nonzero and zero elements (in that order)
    return [*wrk_arr1, *wrk_arr2]


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")