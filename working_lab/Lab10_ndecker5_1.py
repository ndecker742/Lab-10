'''
Lab10_ndecker5-1
Nathaniel Decker
This program finds the current degree rotation based off an user input
06JUL2025
'''

def degree_rotation(number: int) -> int:
    '''
    Returns the current degrees adjusted to remove a full rotation

    Args:
        number (int): the number of total degrees rotated

    Raises:
        TypeError: If empty or not an int

    Returns:
        The adjusted degrees of rotation
    '''
    if number is None:
        raise TypeError('Number must be an int or a float')
    if isinstance(number, str):
        raise TypeError('Number must be an int or float')
    if isinstance(number, bool):
        raise TypeError('Number must be an int or float')
    if number >= 0:
        return number % 360
    
    if number <= 0:
        return 360 + (number % 360)


