import datetime

curr_time = datetime.datetime.now()
print(f"The current time is: {curr_time}")
print(f"Day: {curr_time.day}, Month: {curr_time.month}, Year: {curr_time.year}")

christmas = datetime.datetime(2021, 12, 25)
print(f"Christmas occurs on: {christmas}")

new_years = datetime.datetime(2022, 1, 1)
formatted_date = new_years.strftime("%A, %B %d, %Y")
print(f"New Year's occurs on {formatted_date}")  # Saturday, January 01, 2022
