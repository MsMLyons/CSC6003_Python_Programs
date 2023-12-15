import datetime as datetime

time_of_deposit = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print("Hey, thanks for the cash", time_of_deposit)