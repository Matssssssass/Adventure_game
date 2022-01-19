def directions():
    while True:
        doorchoice = input('''
You have three doors in front of you type which one you choose!

Right (r)
Left (l)
forward (f)
    
:''')
        doorchoice = doorchoice.lower()

        if doorchoice == "r":
            print("You went through the right door")
        elif doorchoice == "l":
            print("Your went through the left door")
        elif doorchoice == "f":
            print("You wnet through the front door")

    

        