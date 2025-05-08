def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    
    odd=[num for num in data if num%2==1]

    return min(odd)

num=[5,7,9,8]
print(find_min_odd(num))
