def moving_zeroes(arr):
    '''
    Input: a List of integers
    Returns: a List of integers
    '''
    sorted_arr = [0] * len(arr)
    current_index = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            sorted_arr[current_index] = arr[i]
            current_index += 1

    return sorted_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
