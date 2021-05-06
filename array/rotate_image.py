def rotateImage(a):
    n = len(a[0])

    for i in range(n // 2):
        for j in range(i, (n - i - 1)):
            temp = a[i][j]
            a[i][j] = a[n - j - 1][i]
            a[n - j - 1][i] = a[n - i - 1][n - j - 1]
            a[n - i - 1][n - j - 1] = a[j][n - i - 1]
            a[j][n - i - 1] = temp

    return a
