a=set(map(int,input().split()))
b=set(map(int,input().split()))
c=set()
if(b.isdisjoint(a)):
    print("Disjoint set")
if(b.issuperset(a)):
    print("Super set")
if(b.issubset(a)):
    print("Subset")
