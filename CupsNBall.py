def formula():
    first = 1
    second = 0
    third = 0
    data = input().upper()

    for i in data:
        if i == 'A':
            first ^= second
            second ^= first
            first ^= second
        elif i == 'B':
            second ^= third
            third ^= second
            second ^= third
        elif i == 'C':
            third ^= first
            first ^= third
            third ^= first

    if first == 1:
            print(1)
    elif second == 1:
            print(2)
    elif third == 1:
            print(3)
#Now I only want you gone

formula()
#Shoutout to Aldi
