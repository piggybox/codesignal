def firstDuplicate(a):
    hash = {}
    has_duplicate = False

    for i in a:
        if i not in hash:
            hash[i] = True
        elif has_duplicate == False:
            # found the first duplicate
            has_duplicate = True
            return i

    if has_duplicate == False:
        return -1
