s,q=[["██"]],[0,1,2]
for i in range(int(input())):s=[["  " if x==y==1 else c for c in r for y in q] for r in s for x in q]
print("\n".join(map("".join, s)))
