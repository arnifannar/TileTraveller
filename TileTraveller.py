room = 11
while room != 31:
    while room == 11:
        direction = input("You can travel (N)orth.\n Direction: ")
        if direction == 'n':
            room += 1
        else:
            print('Not a valid direction!')
    while room == 12:
        direction = input("You can travel (N)orth or (E)ast or (S)outh.\n Direction: ")
        if direction == 'n':
            room += 1
        elif direction == 'e':
            room += 10
        elif direction == 's':
            room -= 1
        else:
            print('Not a valid direction!')
    while room == 13:
        direction = input("You can travel (E)ast or (S)outh.\n Direction: ")
        if direction == 'e':
            room += 10
        elif direction == 's':
            room -= 1
        else:
            print('Not a valid direction!')
    while room == 23:
        direction = input("You can travel (W)est or (E)ast.\n Direction: ")
        if direction == 'w':
            room -= 10
        elif direction == 'e':
            room += 10
        else:
            print('Not a valid direction!')
    while room == 33:
        direction = input("You can travel (W)est or (S)outh.\n Direction: ")
        if direction == 'w':
            room -= 10
        elif direction == 's':
            room -= 1
        else:
            print('Not a valid direction!')
    while room == 32:
        direction = input("You can travel (N)orth or (S)outh.\n Direction: ")
        if direction == 'n':
            room += 1
        elif direction == 's':
            room -= 1
        else:
            print('Not a valid direction!')
    while room == 22:
        direction = input("You can travel (W)est or (S)outh.\n Direction: ")
        if direction == 'w':
            room -= 10
        elif direction == 's':
            room -= 1
        else:
            print('Not a valid direction!')
    while room == 21:
        direction = input("You can travel (N)orth.\n Direction: ")
        if direction == 'n':
            room += 1
        else:
            print('Not a valid direction!')
else:
    print("Victory!")

    
        

