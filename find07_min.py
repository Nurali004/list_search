def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """
    min_num =data[0]
    for num in data:
        if num<min_num:
            min_num=num



    return min_num

num=[1,2,3,4,5]
print(find_min(num))