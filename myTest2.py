#! /usr/bin/env python3
import datetime
from datetime import datetime
from datetime import timedelta

from datetime import date
# today = date.today()
# # dd/mm/YY
# d1 = today.strftime("%d/%m/%Y")
# print("d1 =", d1)
#
# # Textual month, day and year
# d2 = today.strftime("%B %d, %Y")
# print("d2 =", d2)
#
# print(datetime.now())

#Add 1 day
# print((d1 + timedelta(days=90)).strftime("%B %d, %Y"))

start_date = "10/10/11"
date_1 = datetime.strptime(start_date, "%m/%d/%y")

end_date = date_1 + timedelta(days=10)

# date_1 = datetime.strptime(datetime.now(), "%m/%d/%y")
#
# end_date = date_1 + datetime.timedelta(days=10)

print(date_1)
print(end_date)
