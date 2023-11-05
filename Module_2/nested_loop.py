def nested_loop():
    for x in range(2):
        print("This is the outer loop iteration number", str(x))        
        for y in range(4):
            print("This is the inner loop iteration number", str(y))            
    print("Exit inner loop")
nested_loop()