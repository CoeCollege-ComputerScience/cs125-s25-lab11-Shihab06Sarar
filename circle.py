set1= set("abdcklmij")
set2=set("djiefghnop")
set3= set("klmnopqrstij")

print(set1.intersection(set2).intersection(set3))
print(sorted(set1.difference(set2).difference(set3)))
print(sorted(set3.intersection(set2)))
print(sorted(set1.intersection(set2).difference(set3)))
print(sorted(set1.union(set2).intersection(set3).difference(set1.intersection(set2).intersection(set3))))
