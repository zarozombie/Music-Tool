import notes


start = input("Enter Starting Note: \n")

s = start.upper()

root = notes.con_note(s)
# print(root)
# root = int(root)

first = root
third = root + 4
fifth = root + 7
seventh = root + 11

# print(first, third, fifth)

print (notes.num_to_note(first), notes.num_to_note(third), notes.num_to_note(fifth), notes.num_to_note(seventh))