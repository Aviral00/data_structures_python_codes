def array(x, d):

    b = []
    c = []
    for i in range(d):
        b.append(x[i])

    for i in range(d,len(x)):
        c.append(x[i])

    a = c + b
    return a


x = [1, 2, 3, 4, 5, 6, 7]
d = 2
print(array(x, d))



