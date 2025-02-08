from Note import Note

notes = []
while True:
    print("What do you want to do?")
    print("1 - show notes")
    print("2 - add note")
    print("3 - delete note")
    print("4 - change head")
    print("5 - change text")
    print("6 - exit")
    a = input()
    if a == "1":
        for i in range(len(notes)):
            notes[i].printNote()
    elif a == "2":
        notes.append(Note(input("Enter head"), input("Enter text")))
    elif a == "3":
        notes.pop(int(input("Enter index")) - 1)
    elif a == "4":
        notes[int(input("Enter index")) - 1].changeHead(input("Enter head"))
    elif a == "5":
        notes[int(input("Enter index")) - 1].changeText(input("Enter text"))
    elif a == "6":
        print("Goodbye")
        break