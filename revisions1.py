allvalues = (1,2,3,4,3,5,6,4)
newvalues = []
for number in allvalues:
    if number not in newvalues:
       newvalues.append(number)
noduplicates = newvalues
print(noduplicates)
    

allvalues = [1,2,3,4,3,5,6,4]
newvalues = []
for number in allvalues:
    if allvalues.count(number) > 1:
        allvalues.remove(number)
newvalues1 = allvalues
print(newvalues1)

my_tuple = (1,2,3,4,5)
print(list(my_tuple))
