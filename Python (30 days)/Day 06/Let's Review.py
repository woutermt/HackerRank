cases = int(input())

for i in range(cases):
    s = input()
    N = len(s)
    pt1 = ''
    pt2 = ''

    for i in range(N):
        if i % 2 == 0:
            pt1 += s[i]

        elif i % 2 != 0:
            pt2 += s[i]

    print(pt1 + ' ' + pt2)

