def prime_calc(n):
    is_prime = True

    if n > 1:
        for j in range(2, round(n ** 0.5 + 1)):
            if n % j == 0:
                is_prime = False
                break
    else:
        is_prime = False

    return is_prime


def prime_efficient_calc(n):
    if n < 1:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    # Source: https://stackoverflow.com/questions/1801391/how-to-create-the-most-compact-mapping-n-%E2%86%92-isprimen-up-to-a-limit-n
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


if __name__ == "__main__":

    # Number of cases
    T = int(input().strip())

    # Get all data points
    for i in range(T):
        data_point = int(input())

        is_prime = prime_calc(T, data_point)

        if is_prime:
            print("Prime")
        else:
            print("Not prime")