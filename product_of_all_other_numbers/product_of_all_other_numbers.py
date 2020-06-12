"""
[1, 7, 3, 4] ==> [84, 12, 28, 21]

[7*3*4, 1*3*4, 1*7*4, 1*7*3]
"""


def calculate_product(nums):
    product = 1
    for i in range(len(nums)):
        product *= nums[i]
    return product


def product_of_all_other_numbers(arr):
    '''
    Input: a List of integers
    Returns: a List of integers
    '''
    product_arr = [None] * len(arr)
    for i in range(len(arr)):
        excluded = arr[i + 1:] + arr[:i]
        product = calculate_product(excluded)
        product_arr[i] = product

    return product_arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]
    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
