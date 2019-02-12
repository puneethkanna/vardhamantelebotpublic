import re
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
def cgpa(rno,pas):
	br = RoboBrowser(history=True, parser="html.parser")
	br = RoboBrowser(user_agent='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6')
	br.open('http://studentscorner.vardhaman.org')
	form = br.get_form(action="")
	form["rollno"] = rno
	form["wak"] = pas
	br.submit_form(form)
	br.open("http://studentscorner.vardhaman.org/src_programs/students_corner/CreditRegister/credit_register.php")
	bt=br.parsed()
	th=br.select("th")
	td=br.select("td")
	c=str(br.select)
	try:
		return(str(th[1].text.strip())+":"+str(td[7].text.strip())+"\n"+str(th[24].text.strip()))
	except IndexError:
				return("Something went wrong send the report to vardhamanassistant@gmail.com stating the issue. with your rollno")
def sgpa(rno,pas,semid):
	br = RoboBrowser(history=True, parser="html.parser")
	br = RoboBrowser(user_agent='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6')
	br.open('http://studentscorner.vardhaman.org')
	form = br.get_form(action="")
	form["rollno"] = rno
	form["wak"] = pas
	br.submit_form(form)
	br.open("http://studentscorner.vardhaman.org/src_programs/students_corner/CreditRegister/credit_register.php")
	bt=br.parsed()
	th=br.select("th")
	td=br.select("td")
	c=str(br.select)
	index={"1":"13","2":"17","3":"21","4":"25","5":"29","6":"33","7":"37","8":"41"}
	i=int(index[semid])
	try:
		return(str(th[1].text.strip())+":"+str(td[7].text.strip())+"\n"+str(th[i].text.strip()))
	except IndexError:
				return("I think you have not completed that semester.\nIf you have completed send your rollno to vardhamanassistant@gmail.com stating the issue.")
