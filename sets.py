#Sets 
'''
my_sets = {1, 2, 3, 4, 5}

print(my_sets)

my_sets.add(6)  #adding a value
print(my_sets)

my_sets.remove(3) #removing a value
print(my_sets)
'''

set1 = {1, 2, 3}
set2 = {3, 5, 6}

union_set = set1.union(set2)  #Uniom - add both sets together and remove any duplicates
print(union_set)

inter_set = set1.intersection(set2)  #Intersection find the common element between the sets
print(inter_set)
 
diff_set = set1.difference(set2)   #Difference finds the element that are present in one but not the other
print(diff_set)