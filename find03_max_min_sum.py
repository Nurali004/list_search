def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
   
    return max(data) + min(data)

num=[1,2,3,4,5,6]
print(find_max_min_sum(num))
