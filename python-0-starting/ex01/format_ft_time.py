import time as t
import datetime as dt


# retrieve epoch time
# epoch time: the number of seconds that have elapsed since Jan 1, 1970)
epoch_time = t.time()
# get today's date and format it
# %b = abbreviated month name
# %d = day of the month
# %Y = four digit year
today_date = dt.date.today().strftime("%b %d %Y")

# ,.4f = display four decimal places
# .2d = scientific notation with two decimal places
print(f"Seconds since January 1, 1970: {epoch_time:,.4f} or {epoch_time:.2e} in scientific notation")
print(today_date)
