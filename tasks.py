#1
def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L) > 1:
        return L[1]
    else:
        return None

print(select_second(L=[[1]]))