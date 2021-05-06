def isCryptSolution(crypt, solution):
    # convert solution to hash
    hash = {}
    for i in solution:
        hash[i[0]] = i[1]

    def convert_crypt(s, hash):
        result = []
        for i, c in enumerate(s):
            # leading 0 is illegal unless it's a single 0
            if i == 0 and hash[c] == '0' and len(s) > 1:
                return -1
            else:
                result.append(hash[c])

        return int("".join(result))

    if convert_crypt(crypt[0], hash) == -1 or convert_crypt(
            crypt[1], hash) == -1 or convert_crypt(crypt[2], hash) == -1:
        return False

    if convert_crypt(crypt[0], hash) + convert_crypt(
            crypt[1], hash) == convert_crypt(crypt[2], hash):
        return True
    else:
        return False