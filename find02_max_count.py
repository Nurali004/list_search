def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    max_num=data[0]
    count=1
    for num in data[1:]:
        if num>max_num:
            max_num=num
            count=1
        elif num==max_num:
            count+=1
    return count

num=[1,2,3,4,5,5,5]
print(find_max_count(num))
