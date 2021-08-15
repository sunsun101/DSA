# declaring empty list
list = []
take_input = True
# taking input for the list
while take_input:
    try:
        element = int(input("Please enter a number for the list :"))
        list.append(element)
    except ValueError:
        print("Please provide a valid number")
    condition = False
    while not condition:
        yes_no = input("Do you want to provide another value?(y/n)")
        if yes_no == 'y':
            take_input = True
            condition = True
        elif yes_no == 'n':
            take_input = False
            condition = True
        else:
            print("Incorrect input! Please enter (y/n)")

print("List you provided is :", list)

for j in range (1, len(list)):
    # determine the key
    key = list[j]
    # set i to find preceeding element
    i = j - 1

    while i >= 0 and list[i] > key:
        # replace the suceeding element by preceeding if it is greater than key
        list[i + 1] = list[i]
        i = i - 1
    list[i + 1] = key

print("List Sorted in ascending order is :", list)