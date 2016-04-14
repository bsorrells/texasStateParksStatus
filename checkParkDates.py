import time
from datetime import date, timedelta
from stateParkQuery import getSites

def saveParks(parks):
	f = open('Available Parks', 'w')
	for i in parks:
			f.write("{0}: {1}\n".format(i[0], i[1]))
	f.close
	return
		
def checkParkDates():
	#initialize variables
	nextWeeks = 3; #number of weekends to look into the future
	d = date.today()
	oneDay = timedelta(1)
	sixDays = timedelta(6)
	days =[]

	#get upcomimng Friday and Saturday
	days.append(d + timedelta((4-d.weekday()+7)%7))
	days.append(days[0]+oneDay)

	#get the nextWeeks Fridays and Saturdays
	for i in range(nextWeeks):
		days.append(days[-1]+sixDays)
		days.append(days[-1]+oneDay)

	campsitesAvailable = []
	for day in days:
		day = day.strftime('%m/%d/%y')
		campsitesAvailable.append((day,getSites(day)))

	for c in campsitesAvailable:
		print(c)

	saveParks(campsitesAvailable)
	return campsitesAvailable
	
if __name__ == "__main__":
	checkParkDates()
