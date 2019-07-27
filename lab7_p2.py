def ordered3(x,y,z):
    '''
    Variable x,y,z should be in order from smallest to largest.
    The next variable should be same or bigger than the previous one.
    Return True if they are in order, and False if they are not
    '''
    if (x<=y) and (y<=z):
        return True
    else:
        return False