from datetime import datetime, timedelta, date
def display_current_datetime():
    current_date = datetime.today()
    print(current_date)
display_current_datetime()

def calculate_future_date():
    num_of_days = int(input("enter a number of days:"))
    current_date = date.today()
    future_date = current_date + timedelta(days=num_of_days)
    print("future date is:",future_date)
calculate_future_date()
