###wap to display a pattern
##for i in range(4,0,-1):
##    for a in range(1,6):
##        print(i,a,end=' ')
##    print()

n=5
for i in range(1,n+1):
    print(f"{'* '*i:>10}")

print()


n=5
for i in range(n,0,-1):
    print(f"{'* '*i:>10}")

for i in range(1,n+1):
    print(f"{'* '*i:^10}")
print()
for i in range(n,0,-1):
    print(f"{'* '*i:^10}")
