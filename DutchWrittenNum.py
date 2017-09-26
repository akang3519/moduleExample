from telwoord import cardinal, ordinal

boo = True

while(boo):
    choice = int(input("Enter 1 for cardinal translation, 2 for ordinal translation, or 0 to quit: "))
    if choice == 1:
        number = int(input("Enter a number to translate to cardinal Dutch Written Form (0 to quit): "))
        print(cardinal(number, friendly = False))
        if(number == 0):
            break;
    elif choice == 2:
        number = int(input("Enter a number to translate to ordinal Dutch Written Form (0 to quit): "))
        print(ordinal(number, friendly = False))
        if(number == 0):
            break;
    elif choice == 0:
        break;