import datetime


current_date = datetime.datetime.now()

print("Current date and time: ", current_date.strftime("%Y-%m-%d %H:%M:%S"))
print("Current day of the week: ", current_date.strftime("%A"))