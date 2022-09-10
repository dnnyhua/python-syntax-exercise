def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """
    stop = stop + 1
    
    for n in range(start, stop):
        print(n)


    # Springboard's solution
    # while start <= stop:
    #     print(start)
    #     start = start + 1

