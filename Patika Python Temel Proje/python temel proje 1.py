l = [3, 6, ['balık'], [[7, 6],12], 13]
a = []
def Control(x):
    for i in range(len(x)):
        if type(x[i]) != type([]):
            a.append(x[i])
        else: 
            Control(x[i])
for i in range(len(l)):
        if type(l[i]) != type([]):
            a.append(l[i])
        else: 
            Control(l[i])
print(a)



