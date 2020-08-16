'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    wrk_arr = nums
    ret_arr = []

    # Process the work array?
    while len(wrk_arr) >= k:
        # More "windows" to process
        tmp_arr = []
        for elm in wrk_arr[:k]:
            tmp_arr.append(elm)

        # Determine the largest value in our window
        ret_arr.append(max(tmp_arr))

        # Pop off the first element in the work array
        wrk_arr.pop(0)
    
    return ret_arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
