'''
THIS LIBRARY
CONTAINS MAIN MENU
SYSTEM INTERFACE
INCLUDING COVER OF APP
'''

import pathfunc as pt
def cover() :
	print("    ++       ++   ++   ++   ++         ++   ++++++   +++++     ++    ++++++        +++       ++\n    ++++     ++   ++   ++   ++++     ++++   ++       ++   ++   ++   ++            ++ ++      ++\n    ++ ++    ++   ++   ++   ++ ++   ++ ++   ++++++   ++    +   ++   ++           ++   ++     ++\n    ++   ++  ++   ++   ++   ++  ++ ++  ++   ++       ++++++    ++   ++          +++++++++    ++\n    ++     ++++   ++   ++   ++   +++   ++   ++       ++   ++   ++   ++         ++       ++   ++\n    ++       ++   +++++++   ++         ++   ++++++   ++    ++  ++    ++++++   ++         ++  +++++++++\n\n ++++++       +++       ++        +++++++  ++    ++  ++            +++      ++++++++++    ++++++    +++++\n++           ++ ++      ++       ++        ++    ++  ++           ++ ++         ++      ++      ++  ++   ++\n++          ++   ++     ++       ++        ++    ++  ++          ++   ++        ++      ++      ++  ++    +\n++         +++++++++    ++       ++        ++    ++  ++         +++++++++       ++      ++      ++  ++++++\n++        ++       ++   ++       ++        ++    ++  ++        ++       ++      ++      ++      ++  ++   ++\n ++++++  ++         ++  +++++++   +++++++  ++++++++  +++++++  ++         ++     ++        ++++++    ++    ++\n"
)
	print("\t\t\t\t\t\t\t\t\t------------------------------\n\nProgrammer : \t1.Asrofil Fachrul Riidlo\t12317033 \n\t\t2.Abdullah Budhi Salman Hasri\t12317061\n\t\t3.Columbus Simarora\t\t12317047\n\nVersion\t: Beta Version\nfurther information please welcome to sent mail at anjafachrie@gmail.com\n\n")
		
	looping = True
	while looping :
		okay = input("Enter 'continue' to open app = ")
		if okay == "continue" :
			looping = False
			pass
		else :
			okay = input("You've not entered 'entered', cancel to open app ? (yes/no) ")
			if okay == "yes" :
				print("Program stopped")
				exit()
			elif okay == "no" :
				pass
			else :
				print("You've not entered what we expected")
				pass

def about() :
	print("________________________________________________________________________\n\n\tAbout Us :\n\n\t 2019, Group 3 of final assignment of Geopyhsical Computation\n\tclass, Bandung Institute Technology.\n\tThis program created due to enhance students' skills\n\tin coding and understanding base of geophysical computation\n\tFar from perfection, this version need more and more to be\n\tdeveloped and updated and last but not least, we really tear\n\tin hope that this program gives any benefit tp everyone uses it.\n\n\tyours sincerely,\n\tAsrofil, Budhi, and Colombus \n________________________________________________________________________\n")
	input("\npress [enter] to go back..")
def MainMenu():
	print(pt.path(),"\nPlease choose type of methods below :\n1. Gauss\n2. Trapezoidal\n3. Least Square Regression\n4. Newton Interpolation Polynomial\n\ntype 'about' to show about program section\ntype 'exit' to end program")
	maimenutype = input("Enter Menu :  ")
	return maimenutype	