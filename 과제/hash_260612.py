def hash(str):
    r = 31
    M = 1234567891
    sum = 0
    for i in range(len(str)):
        sum += ((ord(str[i])-96) * (r ** i))
        sum %= M
    return sum

str = list(input().lower())
print(hash(str))