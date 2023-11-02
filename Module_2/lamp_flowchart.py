lamp = input("Is the lamp on (yes/no): ")
plugged = input("Is the lamp plugged in (yes/no): ")
burnt = input("Is the bulb burnt out (yes/no): ")

if lamp != "yes":
    if plugged == "yes":
        if burnt == "yes":
            print("replace bulb")
        else:
            print("replace lamp")
    else:
        print("plug in lamp")
else:
    print("enjoy the light 💡")