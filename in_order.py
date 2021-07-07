def in_order(nums):
    # Type Your code here.
    new_list =[]
    for num in nums:
        new_list.append(num)
    new_list.sort()
    if nums == new_list:
        return True
    else:
        return False


if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In order')
    else:
        print('Not in order')

    # Test in-order example
    nums2 = [5, 6, 7, 8, 10]
    if in_order(nums2):
        print('In order')
    else:
        print('Not in order')
