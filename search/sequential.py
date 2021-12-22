def Sequential_Search(dlist, item):
    print('_______________')
    print('SEQUENTIAL SEARCH')
    print('_______________')
    pos = 0
    found = False
    comparisions = 0
    while pos < len(dlist) and not found:
        comparisions = comparisions +1
        if dlist[pos] == item:    
            found = True
        else:
            pos = pos + 1
    print(f'No of Comparisions in SEQUENTIAL SEARCH: {comparisions}')
    return found, pos