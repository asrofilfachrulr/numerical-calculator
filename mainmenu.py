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
	print("\t\t\t\t\t\t\t\t\t------------------------------\n\nProgrammer : \t1.Asrofil Fachrul Riidlo\t\t12317033 \n\t\t\t\t2.Abdullah Budhi Salman Hasri\t12317061\n\t\t\t\t3.Columbus Simarora\t\t\t\t12317047\nVersion\t\t: Beta Version\nfurther information please welcome to sent mail at anjafachrie@gmail.com\n\n")
		
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
	print("\t________________________________________________________________________\n\n\t\t\t\t\t\t\t\t\tAbout Us :\n\n\t\t\t© 2019, Group 3 of final assignment of Geopyhsical Computation\n\t\t\t\t\tclass, Bandung Institute Technology.\n\t\t\t\tThis program created due to enhance students' skills\n\t\t\tin coding and understanding base of geophysical computation\n\t\t\tFar from perfection, this version need more and more to be\n\t\t\tdeveloped and updated and last but not least, we really tear\n\t\t  in hope that this program gives any benefit tp everyone uses it.\n\n\t\t\t\t\t\t\t\tyours sincerely,\n\t\t\t\t\t\tAsrofil, Budhi, and Colombus \n\t________________________________________________________________________\n")
def MainMenu():
	print(pt.path(),"\nPlease choose type of methods below :\n1. Gauss\n2. Trapezoidal\n3. Least Square Regression\n4. Newton Interpolation Polynomial\n\ntype 'about' to show about program section\ntype 'exit' to end program")
	maimenutype = input("Enter Menu :  ")
	return maimenutype	