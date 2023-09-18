import time as t
import datetime as dt

epoch_time = t.time()
today_date = dt.date.today().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {epoch_time:,.4f} or {epoch_time:.2e} in scientific notation")
print(today_date)
