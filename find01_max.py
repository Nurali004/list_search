def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    max_num=data[0]
    for num in data:
        if num>max_num:
            max_num=num
    return max_num



num=[1,2,3,4,5,6]
print(find_max(num))
    