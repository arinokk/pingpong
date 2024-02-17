x = 6
y = x + 1


for i in range(x):
    m = str(11 ** i)
    a = ""
    for j in m:
        a+=j+" "
    print((x-i)* " " + a)
