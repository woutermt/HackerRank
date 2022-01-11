import statistics


def calc_mode(n, arr):
    unique = sorted(set(arr))
    dic_mode = {}
    max_occur = (0, 0)

    for i in unique:
        dic_mode[i] = arr.count(i)

    for key in dic_mode.keys():
        if dic_mode[key] > max_occur[1]:
            max_occur = (key, dic_mode[key])

    return max_occur[0]


if __name__ == '__main__':
    n = input()
    arr = list(map(int, input().strip().split()))

    mean = statistics.mean(arr)
    median = statistics.median(arr)
    mode = calc_mode(n, arr)

    print(mean)
    print(median)
    print(mode)

