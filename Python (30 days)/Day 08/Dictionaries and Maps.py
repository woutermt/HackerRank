
if __name__ == '__main__':
    phonebook = {}
    n = int(input().strip())

    for i in range(n):
        nam_num = input().split(' ')
        phonebook[nam_num[0]] = nam_num[1]

    while True:
        try:
            query = input()
            if query in phonebook.keys():
                output = (query + '=' + phonebook[query])
            else:
                output = "Not found"
            print(output)

        except:
            break
