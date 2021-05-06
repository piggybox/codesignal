def firstNotRepeatingCharacter(s):
    hash = {}

    # build count hash
    for i in s:
        hash[i] = hash.get(i, 0) + 1

    # scan s again to find out the result
    for i in s:
        if hash[i] == 1:
            return i

    return '_'
