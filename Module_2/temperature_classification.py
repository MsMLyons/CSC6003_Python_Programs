temperature = float(input("Please enter a temperature in Fahrenheit: "))

if temperature <= 0:
    print("It's polar weather!")
elif temperature > 0 and temperature <= 32:
    print("It's freezing outside!")
elif temperature > 33 and temperature <= 50:
    print("It's cold outside!")
elif temperature > 51 and temperature <= 80:
    print("It's warm outside!")
elif temperature > 81 and temperature <= 100:
    print("It's hot outside!")
else:
    if temperature >= 101:
        print("It's unbearable outside!")
