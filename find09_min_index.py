def find_min_index(data):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    return data.index(min(data))

num=[9,8,7,2,3,4]
print(find_min_index(num))

