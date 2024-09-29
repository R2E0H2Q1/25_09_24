# 1. Lists part B:

# a. Generate an empty list of decimal numbers of temperatures and:

temperatures = []

# b. Enter temperatures from the user until the number minus 999 is entered for each temperature received add to list.
# We will not add a temperature greater than 50 or less than minus 50

while True:
    temp = float(input("Enter the temperature(999 to exit): "))
    if temp == 999:
        break

    if temp < -50 or temp > 50:
        print('The temperature is out of range')
        continue
    temperatures.append(temp)
print(f'The list of temperatures is: {temperatures}')

# c. Add the following list of temperatures at the end of the current list: [18.5, 39.1 -20.0] (extend hint)

temperatures.extend([18.5, 39.1, -20.0])
print(f'The list after extending it is: {temperatures}')

"""d. What is the difference between extend and operation (+) between lists: for example [4,5,6]+[1,2,3]?
Answer: When using '.extend' the new list will be added at the end of the original, doesn't return anything.
 The operator (+) will returns a new list by fusing(concatenating) both lists, but the original list won't change."""

# e. Print the temperature: the highest (hint max), the lowest (hint min)

print(f'The maximum temperature of the list is: {max(temperatures)}')
print(f'The minimum temperature of the list is: {min(temperatures)}')

# f. Check if the temperature is 18.5 in the list (hint in). If so print True else False

checkup: bool = False
for temp in temperatures:
    if temp == 18.5:
        checkup = True
    print(f'18.5 is {checkup} in the list of temperatures!')

# if 18.5 in temperatures:
#     print('True')
#
# else:
#     print('False')

# g. Count how many times the temperature returns -20.0 (hint count)

min_20 = -20.0
count = temperatures.count(min_20)
print(f'Temp {min_20} appears {count} times in temperatures')

# h. Print the average of the temperatures using sum and len

average: float = sum(temperatures) / len(temperatures)
print(f'The average temperature on the list is: {average}!')

# i. Print each temperature in a separate line (hint: each for)

for temp in temperatures:
    print(temp)

# j. Find the index of the temperature 39.1 (hint index)

idxtofind = 39.1
index = temperatures.index(idxtofind)
print(f'The index for {idxtofind} is {index}')

# k. Remove the temperature at index 0 (del hint)

rmvd_index0 = temperatures.pop(0)#pop removes an specific index.
print(f'The list after popping index 0 is: {temperatures}')

# l. Remove the temperature in each even index (hint: 2 del)

for i in range(len(temperatures)):
    if i % 2 == 0:
        del temperatures[i]
print(f'The list after removing the even numbers is {temperatures}')




# m. Remove the temperature 18.5 (hint remove). Why should you check if it exists before remove?
# n. Extract the last temperature in the list into a memory cell named last_temp (hint pop)
# o. Duplicate the list using copy, sort the new list you created
# p. Duplicate the list again using copy, sort the new list you created in reverse order