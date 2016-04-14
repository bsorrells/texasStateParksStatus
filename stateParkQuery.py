#Queries a set of state parks defined in the variable stateParks to see how many campsites that allow dogs are available for the given date

import requests
from lxml import html
from sys import *

def nextDate(thisDate):
	[x,y,z] = thisDate.split('/')
	[x,y,z] = [int(i) for i in [x,y,z]]
	lastDay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if int(z)%4 == 0 and not( int(z)%100==0 and int(z)%400!=0):
		lastDay[1] = 29
	
	if y==lastDay[x-1]:
		y=1
		x+=1
		if x>12:
			x=1
			z+=1
	else:
		y+=1
	return str(x)+'/'+str(y)+'/'+str(z)

def getSites(date):
	datePlusOne = nextDate(date)

	stateParks = [('Blanco',1), ('Colorado Bend',169), ('Inks Lake',102), ('McKinney',25), ('Perdenales',77), ('Enchanted Rock',79)]
	#other stateParks: ('Lost Maples',95)
	results = []
	for x in stateParks:
		campsites = []
		page = requests.get('http://texas.reserveworld.com/GeneralAvailabilityCalendar.aspx?campId='+str(x[1])+'&arrivalDate='+date+'&DepartureDate='+datePlusOne)
		tree = html.fromstring(page.content)
		i=3; #starting row of campsites
		while tree.xpath('//*[@id="ctl07_tblMain"]/tr[' + str(i) + ']/td[6]/text()'):
			#check if dogs are allowed
			if(tree.xpath('//*[@id="ctl07_tblMain"]/tr[' + str(i) + ']/td[2]/text()') == ['Yes']):
				campsites.append(int(tree.xpath('//*[@id="ctl07_tblMain"]/tr[' + str(i) + ']/td[6]/text()')[0]))
			i+=1
		campsites = sum(campsites)
		if campsites:
			results.append(x[0]+': '+str(campsites))
	if results: return results
	return