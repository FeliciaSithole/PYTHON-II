 #Tuples - are ordered and unchangeble
 
 
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(my_tuple[0]) #can access indivudual elements by using indexing similar to lists
print(my_tuple[2])
print(my_tuple[-1]) #-1 gives us the last value

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

conc_tuple = tuple1 + tuple2 #to add the tuples together
rep_tuple = tuple1 * 3

print(conc_tuple)