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

rom classautomation import get_validated_time
from docx import Document

document = Document()


def study_count():
    while True:
        try:
            class_count = int(input('Enter number of study periods in a day (3 or 4): '))
            if class_count == 4:
                table = document.add_table(5, 4)
                return table, class_count
            elif class_count == 3:
                table = document.add_table(5, 3)
                return table, class_count
            else:
                print('Study period should be 3 or 4.')
        except ValueError:
            print('Invalid input. Enter 3 or 4.')

# to unpack because calling the study_count() dunction alone returns a tuple in this form
# (<docx.table.Table object at 0x0000024CCC221AE0>, 4) and so table = <docx.table.Table object at 0x0000024CCC221AE0>
# which will then be used by then be used by the document app 
# and class_count = 4
# the essence of this is to assign values to our variables so you can reuse them anywhere within the code space
# eg print(f" the class count is : {class_count}")
# >> the class count is 4

table, class_count = study_count()



class_times = [
    'Enter the time interval for the first study period (e.g., 00:00AM/PM - 00:00AM/PM):',
    'Enter the time interval for the second study period (e.g., 00:00AM/PM - 00:00AM/PM):',
    'Enter the time interval for the third study period (e.g., 00:00AM/PM - 00:00AM/PM):',
    'Enter the time interval for the fourth study period (e.g., 00:00AM/PM - 00:00AM/PM):',
]

# To store the time intervals that have been used
used_intervals = set()

# Populate the first row with time intervals
# also while there is no unpacking going on here, we are using the each entry in the used intervals to set the text in the cell
# which is happening at runtime

for col in range(len(class_times)):
    if col < class_count:
        table.cell(0, col).text = get_validated_time(class_times[col], used_intervals)
