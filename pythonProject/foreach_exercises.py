""" # input names from the user and append to the list
# if a name was entered twice then continue
# if the given name was 'exit' then ==> break"""

lst_names = []

while True:
    name: str = input('Please enter your name: ')
    if name == 'exit':
        break
    if name in lst_names:
        print(f"{name} has already been entered. Please enter a different name: ")
        continue  # Skip the rest of the loop if the name is a duplicate
    lst_names.append(name)
print(lst_names)


