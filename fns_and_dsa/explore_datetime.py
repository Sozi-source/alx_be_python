import datetime

def display_current_datetime():
    curent_date = datetime.datetime.now()
    print("Todays date is", curent_date)

def calculate_future_date():
    days = int(input("Enter number of days: "))
    today = datetime.datetime.now()
    future_date = today + datetime.timedelta(days = days)
    formatted_date = future_date.strftime("%Y-%m-%d")
    print("The future date is: ", formatted_date)
    
calculate_future_date()