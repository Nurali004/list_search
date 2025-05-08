def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """


   
    even= [num for num in data if num %2 ==0]
    return min(even)
        

   


num=[2,3,5,6,7]
print(find_min_even(num))

