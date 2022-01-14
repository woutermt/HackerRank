def main():
    ret_d, ret_m, ret_y = list(map(int, input().strip().split(' ')))
    due_d, due_m, due_y = list(map(int, input().strip().split(' ')))

    if (ret_y, ret_m, ret_d) <= (due_y, due_m, due_d):
        print(0)

    elif (ret_y, ret_m) <= (due_y, due_m):
        print(15 * (ret_d - due_d))

    elif ret_y == due_y:
        print(500 * (ret_m - due_m))

    else:
        print(10000)


if __name__ == "__main__":
    main()
