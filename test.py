import datetime
from dateutil import relativedelta

import plenumsmail

startdate = datetime.datetime(2013,1,1)
enddate = datetime.datetime(2013,12,31)

date = startdate 

print "These are the thursdays an invite to the plenum will be send out:"

while (date < enddate):
    date = date + relativedelta.relativedelta(days=1)
    if plenumsmail.is_a_plenum_next_tuesday(date):
        print date
