from datetime import datetime, timedelta

def display_current_datetime():
    curent_date = datetime.datetime.now()
    print("Todays date is", curent_date)

def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    today = datetime.datetime.now()
    future_date = today + datetime.timedelta(days = days)
    formatted_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print("The future date is: ", formatted_date)
    
calculate_future_date()