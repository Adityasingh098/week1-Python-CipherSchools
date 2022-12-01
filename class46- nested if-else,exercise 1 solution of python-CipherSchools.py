winning_number=27
user_input=int(input("guess any number b/w 1  & 100:"))
if user_input==winning_number:
    print("YOU WIN!")
else:
    if user_input<winning_number:
        print("to low")
    else:
        print("too high")
