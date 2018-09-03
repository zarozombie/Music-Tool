import notes

def majscale(note):
    root = notes.con_note(note.upper())
    first = root
    second = root +2
    third = root + 4
    fourth = root + 5
    fifth = root + 7 
    sixth = root + 9
    seventh = root + 11
    return [notes.num_to_note(first), notes.num_to_note(second), notes.num_to_note(third), notes.num_to_note(fourth), notes.num_to_note(fifth), notes.num_to_note(sixth), notes.num_to_note(seventh)
]
    # print(notes.num_to_note(first), notes.num_to_note(second), notes.num_to_note(third), notes.num_to_note(fourth), notes.num_to_note(fifth), notes.num_to_note(sixth), notes.num_to_note(seventh))

def minscale(note):
    root = notes.con_note(note.upper())
    first = root
    second = root + 2
    third = root + 3
    fourth = root + 5
    fifth = root + 7 
    sixth = root + 8
    seventh = root + 10
    print(notes.num_to_note(first), notes.num_to_note(second), notes.num_to_note(third), notes.num_to_note(fourth), notes.num_to_note(fifth), notes.num_to_note(sixth), notes.num_to_note(seventh))

def harminscale(note):
    root = notes.con_note(note.upper())
    first = root
    second = root + 2
    third = root + 3
    fourth = root + 5
    fifth = root + 7 
    sixth = root + 8
    seventh = root + 11
    print(notes.num_to_note(first), notes.num_to_note(second), notes.num_to_note(third), notes.num_to_note(fourth), notes.num_to_note(fifth), notes.num_to_note(sixth), notes.num_to_note(seventh))

def majpenscale(note):
    root = notes.con_note(note.upper())
    first = root
    second = root +2
    third = root + 4
    fifth = root + 7 
    sixth = root + 9
    print(1,2,3,5,6)
    print(notes.num_to_note(first), notes.num_to_note(second), notes.num_to_note(third), notes.num_to_note(fifth), notes.num_to_note(sixth))

# minscale("A")
# majscale("c")
# harminscale("C")
# majpenscale("C")