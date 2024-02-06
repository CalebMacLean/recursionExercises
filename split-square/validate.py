"""Validate that a given square is valid.

Checks that this is either a simple square (``0`` or ``1``), or
a split square (a list of 4 items, each being a simple square or
a split square).

A simple square is valid::

    >>> validate(0)
    True

A split square of four simple filled squares is valid::

    >>> validate([1, 1, 1, 1])
    True

We can nest split and simple squares::

    >>> validate([1, 0, [1, [0, 0, 0, 0], 1, [1, 1, 1, 1]], 1])
    True

    >>> validate([1, [1, 0, 1, [0, [0, 0, 0, 0], 1, 1]], [1, 0, 1, 0], 1])
    True

Simple squares must be either 0 (empty) or 1 (filled)::

    >>> validate(2)
    False

Split squares must contain exactly four parts::

    >>> validate([1, 1, 1, 1, 1])
    False

    >>> validate([1, 0, [1, [0, 0, 0, 0, 1], 1, [1, 1, 1, 1]], 1])
    False

    >>> validate([1, [1, 0, 1, [0, [0, 0, 0], 1, 1]], [1, 0, 1, 0], 1])
    False

"""


def validate(s):
    """Validate that a given square is valid.."""
    # int is passed case
    if(isinstance(s, int)):
        # print(f"{s} is an int")
        if(s == 0 or s == 1):
            # print(f"{s} is 1 or 0")
            return True
        else:
            # print(f"{s} is not 1 or 0")
            return False
    
    # iterate through s if len is 4
    if len(s) == 4:
        # print(f"{s} has {len(s)} items")

        for square in s:
            if(isinstance(square, list)):
                # print(f"{square} is a list")
                return validate(square)
            
            elif(not (square == 0 or square == 1)):
                # print(f"{square} is not 0 or 1")
                return False
    else :
        return False
    
    return True
         

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS; THAT'S SUPER-VALID WORK!\n")
