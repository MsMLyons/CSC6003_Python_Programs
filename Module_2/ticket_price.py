def ticket_price():
    print("Hello there! We're glad you're visiting out theme park. \n")
    print("Let's get you set up with some tickets. \n")
    print("Children under 3 are free. \n")
    under_3 = float(input("How many tickets for children under 3 would you like? "))
    print()
    print("Children 3 - 12 pay $10. \n")
    kids_12 = float(input("How many tickets for children 3 - 12 would you like? "))
    print()
    print("Anyone over 12 pays $15. \n")
    over_12 = float(input("How many tickets for visitors over 13 would you like? "))

    tickets_cost = (kids_12 * 10) + (over_12 * 15)
    tickets_txt = "The total cost of the tickets is ${:.2f}."

    print("You ordered", int(under_3), "tickets for children under 3,", int(kids_12), "tickets for children aged 3 - 12, and", int(over_12), "tickets for visitors over 12 years of age.")
    print(tickets_txt.format(tickets_cost))
    print("Thank you for purchasing tickets and visiting our establishment!")

ticket_price()

