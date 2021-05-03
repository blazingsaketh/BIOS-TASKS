a = input()
b = tuple(a.split(' '))
c = list(map(int,b))
c.sort()
flag = False
if c[0] < 0:
    pass
elif (c[0]) < 10:
    flag = True
else:
    for num in c:
        if str(num) == str(num)[::-1]:
            flag = True
print(flag)