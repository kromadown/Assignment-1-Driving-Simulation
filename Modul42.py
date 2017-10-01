n = int(10)

def formula():
    data = []
    for i in range(n):
        text = int(input())
        ans = text % 42
        data.append(ans)
    myset = len(set(data))
    print (myset)
#That's what I'm counting
