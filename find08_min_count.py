def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    min_num=data[0]
    count=0
    for num in data:
        if num < min_num:
            min_num=num
            count=1
        elif num ==min_num:
            count +=1

    return count


num=[1,1,1,2,3]
print(find_min_count(num))

