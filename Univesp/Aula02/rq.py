
x = 27
c = x
p = 2
s = []
while c > 1: 
    while (p / p != 1) and (p / 1 == p):
        p += 1
    if c % p == 0:
        s.append(p)
        c /= p
    else:
        p += 1

res = []
factors = []
rest = []
for ele in range(0, len(s),2):
    if s[ele + 1]:
        if s[ele] == s[ele + 1]:
            factors.append(s[ele])
        else:
            rest.append(s[ele])
            factors.append(s[ele+1])


print(s)
