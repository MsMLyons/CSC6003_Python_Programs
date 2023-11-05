def nested_loop():
    for x in range(2):
        print("This is the outer loop iteration number", str(x))        
        for y in range(4):
            print("This is the inner loop iteration number", str(y))            
    print("Exit inner loop")
nested_loop()

def nested_loop2():
    num1 = 0
    num2 = 0

    for x in range(5):
        num1 = x
        print(num1)
        for y in range(14):
            num2 = y + 3
            print(num2)
    print(num1 + num2)
nested_loop2()