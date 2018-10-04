#https://github.com/arnis18/TileTraveller

room = 11
try_n = 0
while room != 31:
    while room == 11:
        if try_n == 0:
            print("You can travel (N)orth.")
        direction = input("Direction: ")
        try_n +=1
        if direction.lower() == 'n':
            room += 1
            try_n = 0
        else:
            print('Not a valid direction!')
    while room == 12:
        if try_n == 0:
            print("You can travel (N)orth or (E)ast or (S)outh")
        direction = input("Direction: ")
        try_n +=1
        if direction.lower() == 'n':
            room += 1
            try_n = 0
        elif direction.lower() == 'e':
            room += 10
            try_n = 0
        elif direction.lower() == 's':
            room -= 1
            try_n = 0
        else:
            print('Not a valid direction!')
    while room == 13:
        if try_n == 0:
            print("You can travel (E)ast or (S)outh.")
        direction = input("Direction: ")
        try_n +=1
        if direction.lower() == 'e':
            room += 10
            try_n = 0
        elif direction.lower() == 's':
            room -= 1
            try_n = 0
        else:
            print('Not a valid direction!')
    while room == 23:
        if try_n == 0:
            print("You can travel (W)est or (E)ast.")
        direction = input("Direction: ")
        try_n +=1
        if direction.lower() == 'w':
            room -= 10
            try_n = 0
        elif direction.lower() == 'e':
            room += 10
            try_n = 0
        else:
            print('Not a valid direction!')
    while room == 33:
        if try_n == 0:
            print("You can travel (W)est or (S)outh.")
        direction = input("Direction: ")
        try_n +=1
        if direction.lower() == 'w':
            room -= 10
            try_n = 0
        elif direction.lower() == 's':
            room -= 1
            try_n = 0
        else:
            print('Not a valid direction!')
    while room == 32:
        if try_n == 0:
            print("You can travel (N)orth or (S)outh.")
        direction = input("Direction: ")
        try_n +=1
        if direction.lower() == 'n':
            room += 1
            try_n = 0
        elif direction.lower() == 's':
            room -= 1
            try_n = 0
        else:
            print('Not a valid direction!')
    while room == 22:
        if try_n == 0:
            print("You can travel (W)est or (S)outh.")
        direction = input("Direction: ")
        try_n +=1
        if direction.lower() == 'w':
            room -= 10
            try_n = 0
        elif direction == 's':
            room -= 1
            try_n = 0
        else:
            print('Not a valid direction!')
    while room == 21:
        if try_n == 0:
            print("You can travel (N)orth.")
        direction = input("Direction: ")
        try_n +=1
        if direction.lower() == 'n':
            room += 1
            try_n = 0
        else:
            print('Not a valid direction!')
else:
    print("Victory!")

    
        

