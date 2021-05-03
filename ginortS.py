def a(b) -> str:
    odd = ""
    even = ""
    upper = ""
    lower = ""
    b = sorted(b)
    for x in b:
        if(x.islower()):
            lower += x
        elif(x.isupper()):
            upper += x
        elif(int(x)%2 != 0):
            odd += x
        elif(int(x)%2 == 0):
            even += x
    return (lower + upper + odd + even)
sent = str(input())
print(a(sent))