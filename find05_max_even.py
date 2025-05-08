def max_even(data):
    """
    Return the maximum even number in the list using a simple for loop.
    Args:
        data: list of numbers
    Returns:
        int or None: maximum even number, or None if not found
    """
    max_even_num = 0

    for num in data:
        if num % 2 == 0:
            max_even_num=num
           
                

    return max_even_num


numbers = [3, 7, 2, 8, 5, 10, 1]
print(max_even(numbers))  

