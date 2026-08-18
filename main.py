from scrapdiver import *

def setlist_scrap():
	_input = input("INPUT A URL FOR READIND[quit-for quit]:")
	if(_input != 'quit'):
		add_task(_input)
		setlist_scrap()
	else:
		start_diver()

def startApp():
	set_db("db.sqlite")
	setlist_scrap()

startApp()