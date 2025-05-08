def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    max_odd_num=0
    for num in data:
        if num%2==0:
            max_odd_num=num
    return max_odd_num

num=[1,2,3,4,5,6]
print(find_max_odd(num))