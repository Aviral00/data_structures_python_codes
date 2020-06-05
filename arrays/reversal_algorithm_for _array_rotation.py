def reverse(f, start, end):

    while start < end:
        temp = f[start]
        f[start] = f[end]
        f[end] = temp
        start += 1
        end = end - 1


def array_rotation(y, z):

    n = len(y)
    reverse(y, 0, z-1)
    reverse(y, z, n-1)
    reverse(y, 0, n - 1)


def printArray(e):
    for i in range(0, len(e)):
        print(e[i]),


arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
array_rotation(arr, d)
printArray(arr)

