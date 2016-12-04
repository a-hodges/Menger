s,q=[["██"]],range
for i in q(int(input())):s=[["  " if x==y==1 else c for c in r for y in q(3)] for r in s for x in q(3)]
print("\n".join("".join(r) for r in s))
