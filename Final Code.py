from E_Voting import vote_machine
ch1 = "y"
while ch1.lower() == "y":
    print("Welcome to the E - Election Software\nPlease choose an action")
    print("1. Voter list Registration\n2. Candidate Information\n3. Cast your Vote\n4. Results\n5. Help Desk\n6. Exit")
    ch = int(input("Enter your choice[1/2/3/4/5]: "))
    if ch == 1:
        vote_machine.voter_reg()
        print("Thank you for your support.... Until next time")
        pass
    elif ch == 2:
        vote_machine.cand_info()
        print("Thank you for your support.... Until next time")
        pass
    elif ch == 3:
        vote_machine.cast_vote()
        print("Thank you for your support.... Until next time")
        pass
    elif ch == 4:
        vote_machine.result()
        print("Thank you for your support.... Until next time")
        pass
    elif ch == 5:
        vote_machine.faq()
        print("Thank you for your support.... Until next time")
        pass
    else:
        print("Thank you for your support.... Until next time")
        quit()
    ch1 = input("Do you want to continue [y/n]: ")
