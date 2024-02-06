"""Produce new square adding two inputs squares.

Two simple squares can be added::

    >>> s1 = 0
    >>> s2 = 1

    >>> add(s1, s2)
    1

A simple square and a split square can be added::

    >>> s1 = 0
    >>> s2 = [1, 0, 1, 0]

    >>> add(s1, s2)
    [1, 0, 1, 0]

Two split squares can be added::

    >>> s1 = [0, 0, 0, 1]
    >>> s2 = [0, 1, 0, 1]

    >>> add(s1, s2)
    [0, 1, 0, 1]

Nested squares can be added::

    >>> s1 = [0, [1, 1, 1, [0, 0, 0, 0]], [0, 0, 0, 0], 1]
    >>> s2 = [1, [1, 0, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]

    >>> add(s1, s2)
    [1, [1, 1, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]

Unevenly-nested squares can be added::

    >>> s1 = [0, [1, 1, 1, 0           ], [0, 0, 0, 0], 1]
    >>> s2 = [1, [1, 0, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]

    >>> add(s1, s2)
    [1, [1, 1, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]

    >>> s1 = [0, [1, 1, 1, 1                      ], [0, 0, 0, 0], 1]
    >>> s2 = [1, [1, 0, 1, [0, [0, 0, 0, 0], 1, 1]], [1, 0, 1, 0], 1]

    >>> add(s1, s2)
    [1, [1, 1, 1, [1, [1, 1, 1, 1], 1, 1]], [1, 0, 1, 0], 1]
"""


def add(s1, s2, acc = None):
    """Produce new split square adding two input squares."""
    # make acc a list
    if acc is None:
        acc = []

    # params are ints case
    if(isinstance(s1, int) and isinstance(s2,int)):
        if(s1 == 1 or s2 == 1):
            return 1
        else:
            return 0
    
    # confirm that params are list, convert if otherwise
    if(isinstance(s1, int)):
        # print("s1 is int")
        f_list = [s1 for i in range(4)]
    else:
        f_list = s1
    
    if(isinstance(s2, int)):
        # print("s2 is int")
        s_list = [s2 for i in range(4)]
    else:
        s_list = s2
    
    # print(f"f_list: {f_list}, s_list: {s_list}")

    # iterate through lists
    for i in range(4):
        # val vars
        f_val = f_list[i]
        s_val = s_list[i]

        # print(f"f_val: {f_val}, s_val: {s_val}")

        if(isinstance(f_val, int) and isinstance(s_val, int)):
            # print("f_val and s_val are ints")
            if((f_val == 1) or (s_val == 1)):
                acc.append(1)
            else:
                acc.append(0)
            # print(f"acc: {acc}")
        
        if(isinstance(f_val, list) or isinstance(s_val, list)):
            # print("f_val or s_val are ints")
            acc.append(add(f_val, s_val))
            # print(f"acc: {acc}")
    
    return acc
        
    
        

        

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS; YOU'RE A RECURSION WIZARD!\n")
