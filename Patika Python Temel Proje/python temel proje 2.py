l = [[2, 4], [6, 8], [10, 12, 14]]
for i in range(len(l)):
        if type(l[i]) == type([]):
            l[i].reverse()
        
l.reverse()
print(l)