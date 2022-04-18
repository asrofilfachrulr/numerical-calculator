import numpy as np
import matplotlib.pyplot as plt
import pathfunc as pt 		# stored menu path
import errorlist as err 	# library to show error, condition-based
import time as tm
import os 
a,b,c,d,e = 0,0,0,0,0
os_user = "windows"

def trapezmenu() :
	'''
	Contains :
	1. Treapezoid Menu
	2. Input Equation Data
	3. Processing Data to Find Solution Based
		Trapezoid Method
	4. Showing Solutions
	5. Option to Operate Data or Solution with File
	'''
	homecommand = False
	trapez_equation = ''
	degree = 0
	lower = 0
	upper = 0
	grid = 1000 # default
	write_to_file = ""
	FromExtract = False
	

	print(pt.path(m = 1),"\nSelect the degree of polynomial : \n1. Second Degree Polynomial Equation\n2. Third Degree Polynomial Equation\n3. Fourth Degree Polynomial Equation\n\ntype 'back' to go back to previous menu\ntype 'home' to go back to main menu\n\n")
	SubMenu_input = input("Enter Menu : ")
	if SubMenu_input == "1" or SubMenu_input == "2" or SubMenu_input ==  "3" :
		if SubMenu_input == "1":
			degree = 2
		if SubMenu_input == "2":
			degree = 3
		if SubMenu_input == "3":
			degree = 4

		while True :
			if trapez_equation == '' :
				print(pt.path(m = 1,t0 = int(SubMenu_input)-1),"\nEquations :",trapez_equation,"\n1. Enter Manually\n2. Extract from File\n3. Find and Show Solutions\n4. Write Solutions into a File\n\ntype 'back' to go back to previous menu\ntype 'home' to go back to main menu\n\n")

			elif trapez_equation != '':
				print(pt.path(m = 1,t0 = int(SubMenu_input)-1),"\nEquations :",trapez_equation,"\n1. Replace Equations Manually\n2. Replace Equations and Extract from File\n3. Find and Show Solutions\n4. Write Solutions into a File\n\ntype 'back' to go back to previous menu\ntype 'home' to go back to main menu\nWARNING : back to previous menu or go to main menu will erase equation that you've entered\n")
			SubSubMenu_input = input("Enter Menu : ")
			#	Enter manual  #
			if SubSubMenu_input ==  "1" :
				print(pt.path(m = 1, t0 = int(SubMenu_input)-1, u = int(SubSubMenu_input)-1))
				while True :
					if degree == 2 :
						try :
							lower = int(input("lower bound = "))
							upper = int(input("upper bound = "))
						except :
							print("error data type!(must be an integer!)")
							continue
						print("General form = ax^2+bx+c")
						try :
							a = float(input("a ="))
							b = float(input("b ="))
							c = float(input("c ="))
						except :
							print("error data type! (must be an interger of a float)")
							continue
						if b >= 0 :
							temp_b = " + " + str(b)
						if c >= 0 :
							temp_c = " + " + str(c)
						trapez_equation = "{}x^2{}x{}".format(a,temp_b,temp_c)
						option = input("enter custom grid?(default is = 1000)\n[y/n] = ")
						if option == "y":
							grid = int(input("(Warning, the highest grid may cause the program crashes!)Grid = "))
						else:
							print("grid set to 1000")
						break
							
					elif degree == 3 :
						try :
							lower = int(input("lower bound = "))
							upper = int(input("upper bound = "))
						except :
							print("error data type!(must be an integer!)")
							continue
						print("General form = ax^3+bx^2+cx+d")
						try :
							a = float(input("a ="))
							b = float(input("b ="))
							c = float(input("c ="))
							d = float(input("d ="))

						except :
							print("error data type! (must be an interger of a float)")
							continue
						if b >= 0 :
							temp_b = "+" + str(b)
						if c >= 0 :
							temp_c = "+" + str(c)
						if d >= 0 :
							temp_d = "+" + str(d)

						trapez_equation = "{}x^3{}x^2{}x{}".format(a,temp_b,temp_c,temp_d)
						option = input("enter custom grid?(default is = 1000)\n[y/n] = ")
						if option == "y":
							grid = input("(Warning, the highest grid may cause the program crashes!)Grid = ")
						else:
							print("grid set to 1000")
						break


					elif degree == 4 :

						try :
							lower = int(input("lower bound = "))
							upper = int(input("upper bound = "))
						except :
							print("error data type!(must be an integer!)")
							continue
						print("General form = ax^4+bx^3+cx^2+dx+e")
						try :
							a = float(input("a ="))
							b = float(input("b ="))
							c = float(input("c ="))
							d = float(input("d ="))
							e = float(input("e ="))


						except :
							print("error data type! (must be an interger of a float)")
							continue
						if b >= 0 :
							temp_b = "+" + str(b)
						if c >= 0 :
							temp_c = "+" + str(c)
						if d >= 0 :
							temp_d = "+" + str(d)
						if e >= 0 :
							temp_e = "+" + str(e)

						trapez_equation = "{}x^4{}x^3{}x^2{}x{}".format(a,temp_b,temp_c,temp_d,temp_e)
						option = input("enter custom grid?(default is = 1000)\n[y/n] = ")
						if option == "y":
							grid = input("(Warning, the highest grid may cause the program crashes!)Grid = ")
						else:
							print("grid set to 1000")
						break
			#	Extract file   #
			elif SubSubMenu_input ==  "2" :
				Flow = True
				os_user = input("Do you use linux or windows?\n")
				print(pt.path(m = 1, t0 = int(SubMenu_input)-1, u = int(SubSubMenu_input)-1))
				if degree == 2 :
					print("File must be .txt and contains following format  = ax^2+bx+c, with a, b , c are constants")
				elif degree == 3 :
					print("File must be .txt and contains following format  = ax^3+bx^2+cx+d, with a , b , c , d are constants")
				elif degree == 4 :
					print("File must be .txt and contains following format  = ax^4+bx^3+cx^2+dx+e, with a , b , c , d , e  are constants ")
				print("Caution = Wrong file format may cause constants misread")
				temp = input("\nPlease choose method to open the file :\n1. Enter Full Path of Directory\n2. Enter File's Name(select this IF ONLY particular file's directory and file's application directory is same\n\nEnter Menu : ")
				
				while Flow :
					ScanRun = True
					if temp == "1" :
						while True :
							if os_user == "windows" :
								filepath = input("Enter path  (ex. = C:\\Users\\Username\\Path\\To\\File\nEnter 'cancel' to go back\nPath = ")
							elif os_user == "linux" :
								filepath = input("Enter path (ex. = /home/Username/Path/To/File\nEnter 'cancel' to go back\nPath = ")
							if filepath == 'cancel' :
								ScanRun = False
								break
							else:
								if os.path.isfile(filepath) :
									if filepath[-3:] != "txt":
										print("wrong extension!")
									else :
										break					
								else :
									print("File not found!")

					
					elif temp == "2" :
						while True :
							filepath = input("Enter file's name = (insert the extension .txt)\nEnter 'cancel' to go back\nFile's Name = ")						
							if filepath == 'cancel':
								ScanRun = False
								break
							if os.path.isfile(os.getcwd()+'/'+filepath) :
								if filepath[-3:] != "txt":
									print("wrong extension!")
								else :
									break
							else :
								print("File not found!")
						
					else :
						print("wrong input, please try again")
						temp = input("\nPlease choose method to open the file :\n1. Enter Full Path of Directory\n2. Enter File's Name(select this IF ONLY particular file's directory and file's application directory is same)")
						continue
					while ScanRun :
						a,b,c,d,e = 0,0,0,0,0
						f = open(filepath,"r")
						sign = False
						index = 0
						nums = ''
						skip = False
						for cursor in f.read() :
							if cursor == "-" :
								sign = True
								continue
							if skip :
								skip = False
								continue
							try :
								if cursor != "x" and cursor != "+" :
									nums = nums + cursor
									continue
								elif cursor == "x" or cursor == "+" or cursor == "|":
									if cursor == "x" :
										skip = True
									elif cursor == "+" or cursor == "=" :
										continue
									nums = int(nums)
									if degree == 2 :
										if index == 0 :
											if sign :
												nums*= -1
												sign = False
											a = nums
											nums = ''
											index += 1
										elif index == 1 :
											if sign :
												nums*= -1
												sign = False
											b = nums
											nums = ''
											index += 1
										elif index == 2 :
											if sign :
												nums*= -1
												sign = False
											c = nums
											nums = ''
											break
									elif degree == 3 :
										if index == 0 :
											if sign :
												nums*= -1
												sign = False
											a = nums
											nums = ''
											index += 1
										elif index == 1 :
											if sign :
												nums*= -1
												sign = False
											b = nums
											nums = ''
											index += 1
										elif index == 2 :
											if sign :
												nums*= -1
												sign = False
											c = nums
											nums = ''
											index+=1
										elif index == 3 :
											if sign :
												nums*= -1
												sign = False
											d = nums
											nums = ''
											break
									elif degree == 4 :
										if index == 0 :
											if sign :
												nums*= -1
												sign = False
											a = nums
											nums = ''
											index += 1
										elif index == 1 :
											if sign :
												nums*= -1
												sign = False
											b = nums
											nums = ''
											index += 1
										elif index == 2 :
											if sign :
												nums*= -1
												sign = False
											c = nums
											nums = ''
											index+=1
										elif index == 3 :
											if sign :
												nums*= -1
												sign = False
											d = nums
											nums = ''
											index+=1
										elif index == 4 :
											if sign :
												nums*= -1
												sign = False
											e = nums
											nums = ''
											break

								ExtractSuccess = True
							except :
								print("Wrong File Format!")
								ExtractSuccess = False

						f.close()
						if ExtractSuccess :
							if b >= 0 :
								temp_b = "+" + str(b)
							if c >= 0 :
								temp_c = "+" + str(c)
							if d >= 0 :
								temp_d = "+" + str(d)
							if e >= 0 :
								temp_e = "+" + str(e)
							if degree == 2:
								trapez_equation = "{}x^2{}x{}".format(a,temp_b,temp_c)
							elif degree == 3:
								trapez_equation = "{}x^3{}x^2{}x{}".format(a,temp_b,temp_c,temp_d)
							if degree == 4:
								trapez_equation = "{}x^4{}x^3{}x^2{}x{}".format(a,temp_b,temp_c,temp_d,temp_e)
							Flow = False
							FromExtract = True
							break

						else :
							print("Due an Error was Found While Reading the File, Program will Back to Previous Menu ...")
							tm.sleep(3)
							Flow =  False
							break

			#	find solution  #
			elif SubSubMenu_input ==  "3" :
				if FromExtract :
					while True:
						try :
							upper = int(input("Enter upper bound = "))
							lower = int(input("Enter lower bound = "))
							break
						except :
							print("wrong data type!")
				jum = 0
				print(pt.path(m = 1, t0 = int(SubMenu_input)-1, u = int(SubSubMenu_input)-1))
				h=(upper-lower)/grid #lebar grid
				if degree == 2:
					jum=0.5*a*lower*lower+b*lower+c
				elif degree == 3:
					jum=0.5*a*lower*lower*lower+b*lower*lower+c*lower+d
				elif degree == 4:
					jum=0.5*a*lower*lower*lower*lower+b*lower*lower*lower+c*lower*lower+d*lower+e
				for i in range (1,grid):
					xi=lower+h*i
					if degree == 2:
						jum=jum + a*xi*xi+b*xi+c
					elif degree == 3:
						jum=jum + a*xi*xi*xi+b*xi*xi+c*xi+d
					elif degree == 4:
						jum=jum + a*xi*xi*xi*xi+b*xi*xi*xi+c*xi*xi+d*xi+e

				if degree == 2:
					jum=jum+0.5*a*upper*upper+b*upper+c
				elif degree == 3:
					jum=jum+0.5*a*upper*upper*upper+b*upper*upper+c*upper+d
				elif degree == 4:
					jum=jum+0.5*a*upper*upper*upper*upper+b*upper*upper*upper+c*upper*upper+d*upper+e
				res=jum*h
				write_to_file = "Equation = {}\nLower bound = {}\nUpper bound = {}\nGrid = {}\nResult = {}".format(trapez_equation,lower,upper,grid,res)
				print(write_to_file)
				temp = input("\n\nPress enter to go back")

			#	Write to File  	#
			elif SubSubMenu_input ==  "4" :
				print(pt.path(m = 1, t0 = int(SubMenu_input)-1, u = int(SubSubMenu_input)-1))
				if write_to_file != "":
					filename = input("Please input file's name \n\nEnter name : ")
					filename = filename + '.txt'
					cwd = os.getcwd()
					if os_user == "linux" :
						check = "/Saved Solution/Trapezoid/"
					elif os_user == "windows" :
						check = "\\Saved Solution\\Trapezoid\\"
					if os.path.isdir(cwd+check) :
						pass
					else :
						os.makedirs(cwd+check)
					filename = cwd + check + filename
					f = open(filename,"w")
					f.write(write_to_file)
					f.close()
					print("File saved in ",filename)
					misc = input("Press enter go back")
				else :
					print("Solution Data isn't Exist yet!.\nPlease select 'Find Solution' first!")


			elif SubSubMenu_input == 'back' :
				return True
			elif SubSubMenu_input == 'home' :
				return False
			else:
				err.error(0,SubSubMenu_input)
	elif SubMenu_input == 'back' :
		return False	
	elif SubMenu_input == 'home' :
		return False
	else :
		err.error(0,SubMenu_input)
		return True