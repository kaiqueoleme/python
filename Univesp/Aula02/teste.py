x = 4
n = [3.6, 8.9, 10]
print(len(n))
h = (len(n) / ((1/(n[0] + x)) + (1/(n[1] + x)) + (1/(n[2] + x)))) - x
print(h)