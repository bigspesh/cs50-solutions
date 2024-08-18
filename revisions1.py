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

s = "SIMPLILEARN"
for i in s:
    print(i, end="")

list2 = ['ctrl', 'John', "David"]
for i in range(len(list2)):
    print(f"Hello:{list2[i]}")


a = "aaa,bbb,ccc"
b = Counter(a)
print(list(a))


cities_in_F = {'New York': 32, 'Boston': 55, 'Denver': 65, 'Los_Angeles': 34}
a = Counter(cities_in_F)
print(a)


user_input = (input("Enter Change:"))
print("HELLO" + user_input)


car = 4.2
print("this is %d" %car )

text = input()
for i in text.split():
    print(i)

