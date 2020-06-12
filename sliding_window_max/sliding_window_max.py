def sliding_window_max(nums, k):
    '''
    Input: a List of integers as well as an integer `k` representing the size of the sliding window
    Returns: a List of integers
    '''
    results = []
    current_index = 0
    for i in range(len(nums) - k + 1):
        results.append(max(nums[i:i + k]))
        current_index += 1
    return results


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(nums, k)}")
