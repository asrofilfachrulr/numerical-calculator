'''
MAIN CONTROL OF WHOLE APP
INCLUDE BUT NOT RESTRICTED TO :
1. MAIN MENU
2. CALLING ALL SUBMENU
3. TERMINTATION APP
4. RUN APP IN CYCLE(LOOPING)

DO NOT EDIT ANYTHING WITHOUT ANY CONSIDERATION
'''

#---------------------------all necessary libaries--------------------#
import mainmenu as mm # skeleton of main menu interface
import __interpolate__ as pol # Interpolation's module
import __gauss__ as gs # Gauss' module
import __trapezoid__ as trp # Trapezoidal's module
import __regress__ as rg # Regression's module
import pathfunc as pt # stored all path menu
import errorlist as err # list of all error
import os
# -------------------------Main Program Flow-----------------------------#

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def run() : 
	''' 
	Trigger to run application
	begin with showing cover of app
	as introductory
	'''
	print("For better experience before running this app, please use console with fullscreen or maximum window size\njust tell us anytime to continue..")
	run_input = input("Continue ? (y/n) = ")
	if run_input == 'y' :
		mm.cover()
		AppFlow()
	elif run_input == 'n' :
		looping = True
		while looping :
			print("we strongly reccomended to use fullscreen/maximum console window size")
			run_input = input("Continue ? (y/n) = ")
			if run_input == 'y' :
				looping = False
				mm.cover()
				AppFlow()
			elif run_input == 'n' :
				pass
			else :
				print("Hmm you've entered input not what we expected")
	else :
		print("Hmm you've entered input not what we expected")


def AppFlow():
	'''
	Main flow of whole app
	begin with showing main menu
	and get user input to select
	desired menu(modules)
	'''
	# Make app run in cycle
	while True :
		clearConsole()
		flow_state = True # state that keep the cycle
		MainMenu_input = mm.MainMenu() # calling main menu to be shown
		# ^ variable that get user input to decide what menu to be procced

		if MainMenu_input == '1' :
			while flow_state :
				flow_state = gs.gaussmenu() #calling gauss menu
		elif MainMenu_input == '2' :
			while flow_state :
				flow_state = trp.trapezmenu() # calling trapezoid menu
		elif MainMenu_input == '3' :
			while flow_state :
				flow_state = rg.regressmenu() # calling regression menu
		elif MainMenu_input == '4' :
			while flow_state :
				flow_state = pol.interpolmenu() # calling interpolation menu
		elif MainMenu_input == 'about' :
			mm.about() # showing 'about' section
		elif MainMenu_input == 'exit' : 
			break # terminate program completely in a proper way based upon user consideration
		else :
			err.error(0,MainMenu_input) # calling error code when user give unexpected input
		

	print("\nProgram Ended Successfully ...")