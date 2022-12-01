name , char =input("enter comma separated name and character :").split(",")
print(f"length of your name is {len(char)}")
print(f"character count :{name.lower().count(char.lower())}")