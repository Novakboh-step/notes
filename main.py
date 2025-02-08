from Note import Note

notes = []
while True:
    print("What do you want to do?")
    print("1 - show notes")
    print("2 - add note")
    print("3 - delete note")
    print("4 - exit")
    a = input()
    if a == "1":
        for i in range(len(notes)):
            notes[i].printNote()
    elif a == "2":
        notes.append(Note(input("Enter head"), input("Enter text")))
    elif a == "3":
        notes.pop(int(input("Enter index")) - 1)
    elif a == "4":
        print("Goodbye")
        break