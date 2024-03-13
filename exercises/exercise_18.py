# Your solution to Exercise 18
remember_name = input("Remember the name: ")
if remember_name == "Yes":
    is_ex = input("Is it an ex: ")
    if is_ex == "Yes":
        are_you_drunk = input("Are you drunk: ")
        if are_you_drunk == "Yes":
            rekindle = input("Do you want to rekindle: ")
            if rekindle == "No":
                decision = "Don't say hi"
            else:
                decision = "Make your own decision"
        else:
            decision = "Make your own decision"
    else:
        decision = "Make your own decision"
else:
    time_to_flee = input("Is there time to flee: ")
    if time_to_flee == "Yes":
        decision = "Run for it"
    else:
        decision = "Make your own decision"
print(decision)
