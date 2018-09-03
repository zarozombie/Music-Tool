# print("A B C D E F G")
# print("A# B C# D# F# G#")
# print("1 2 3 4 5 6 7 8 9 10 11 12")

x = []

x = ["A", "A#", "B", "C", "D", "D#", "E", "F", "F#", "G", "G#"]

def con_note(note):
    if note == "A":
        return 1
    elif note == "A#":
        return 2
    elif note == "B":
        return 3
    elif note == "C":
        return 4
    elif note == "C#":
        return 5
    elif note == "D":
        return 6
    elif note == "D#":
        return 7
    elif note == "E":
        return 8
    elif note == "F":
        return 9
    elif note == "F#":
        return 10
    elif note == "G":
        return 11
    elif note == "G#":
        return 12

def num_to_note(number):
    if number > 12:
        number = number - 12
    if number == 1:
        return "A"
    elif number == 2:
        return "A#"
    elif number == 3:
        return "B"
    elif number == 4:
        return "C"
    elif number == 5:
        return "C#"
    elif number == 6:
        return "D"
    elif number == 7:
        return "D#"
    elif number == 8:
        return "E"
    elif number == 9:
        return "F"
    elif number == 10:
        return "F#"
    elif number == 11:
        return "G"
    elif number == 12:
        return "G#"

# rootnote = "a"
# print(rootnote.upper())
# print(con_note(rootnote.upper()))
# con_note("A")
# print(x[0])
