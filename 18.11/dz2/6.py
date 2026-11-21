def merge_lists(list1, list2):
    result = []
    for item in list1:
        result.append(item)
    for item in list2:
        result.append(item)
    return result
print(merge_lists([1, 3, 5], [2, 4, 6]))