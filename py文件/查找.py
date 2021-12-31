def binary_search(li, value):
    left = 0
    right = len(li) - 1
    while left <= right:  # 候选区有值
        mid = (left + right) // 2
        if li[mid] == value:
            return mid
        elif li[mid] > value:
            right = mid - 1
        elif li[mid] < value:
            left = mid + 1
    return None
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))

