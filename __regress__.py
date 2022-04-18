import numpy as np
import matplotlib.pyplot as plt
import pathfunc as pt 		# stored menu path
import errorlist as err 	# library to show error, condition-based
import time as tm
import os 
os_user = "windows"


def regressmenu():
	'''
	Contains :
	1. Regression Menu
	2. Input x.y Data
	3. Processing Data to Find Solution Based
		Least Sqquare Regression Method
	4. Showing and Plotting Solutions
	5. Option to Operate Data or Solution with File
	'''
	dataX = []
	dataY = []
	data = ''
	data_len = 0
	write_to_file = ""

	while True:
		if data == '' :
			print(pt.path(m = 2),"\nData :\n",data,"\n1. Enter Data (x,y) Manually\n2.Extract Data from File\n3.Process to Find the Estimated x or y\n\ntype 'back' to go back to previous menu\ntype 'home' to go back to main menu\n\n")
		elif data != '' :
			print(pt.path(m = 2),"\nData :\n",data,"\n1.Replace Data (x,y) Manually\n2.Replace Data from File\n3.Process to Find the Estimated x or y\n\ntype 'back' to go back to previous menu\ntype 'home' to go back to main menu\n\n")	
		SubMenu_input = input("Enter Menu : ")
		if SubMenu_input == "1" or SubMenu_input == "2" or SubMenu_input == "3" :
			while True :
				##  Enter Data Manually  ##
				if SubMenu_input == "1" :
					print(pt.path(m=2,u0 = 0))
					print("Enter data x,y. Enter 'stop' to finish entering, enter 'cancel' to abort")
					counter = 1
					skip = False
					while True :
						try :
							data_len = counter
							temp = input("x{} = ".format(counter))
							dataX.append(float(temp))
							temp = input("y{} = ".format(counter))
							dataY.append(float(temp))
							counter+=1
						except :
							if temp == "cancel":
								dataX = []
								dataY = []
								data_len = 0
								skip = True
								break
							elif temp == "stop":
								data = "data x = {}, data y = {}".format(dataX,dataY)
								print("data saved")
								tm.sleep(3)
								skip = True
								break
							else:
								print("Wrong data type!, data must be an integer or a float")
								continue
					if skip :
						break
				#	Extract data   #
				elif SubMenu_input == "2":
					Flow = True
					ScanRun = False
					SuccessState = False
					print(pt.path(m=2,u0 = 1))

					os_user = input("Do you use linux or windows?\n")
					print("File must contains following format = \nx1,x2,x3,x4|y1,y2,y3|\nuse dot(.) for decimal and comma (,) for data separator!")
					print("Caution = Wrong file format may cause data misread")
					temp = input("\nPlease choose method to open the file :\n1. Enter Full Path of Directory\n2. Enter File's Name(select this IF ONLY particular file's directory and file's application directory is same\n\nEnter Menu : ")
					a = True
					while Flow :

						if temp == "1" :
							while a :
								if os_user == "windows" :
									filepath = input("Enter path  (ex. = C:\\Users\\Username\\Path\\To\\File\nEnter 'cancel' to go back\nPath = ")
								elif os_user == "linux" :
									filepath = input("Enter path (ex. = /home/Username/Path/To/File\nEnter 'cancel' to go back\nPath = ")
								if filepath == 'cancel' :
									ScanRun = False
									a = False
								else:
									if os.path.isfile(filepath) :
										if filepath[-3:] != "txt":
											print("wrong extension!")
										else :
											ScanRun = True
											a = False					
									else :
										print("File not found!")

						
						elif temp == "2" :
							while a :
								filepath = input("Enter file's name = (insert the extension .txt)\nEnter 'cancel' to go back\nFile's Name = ")						
								if filepath == 'cancel':
									ScanRun = False
									a = False
								if os.path.isfile(os.getcwd()+'/'+filepath) :
									if filepath[-3:] != "txt":
										print("wrong extension!")
									else :
										ScanRun = True
										a = False
								else :
									print("File not found!")
							
						else :
							print("wrong input, please try again")
							temp = input("\nPlease choose method to open the file :\n1. Enter Full Path of Directory\n2. Enter File's Name(select this IF ONLY particular file's directory and file's application directory is same)")
							continue

						while ScanRun :
							switch = False
							sign = False
							f = open(filepath,"r")
							nums = ""
							for cursor in f.read():
								if cursor == "-" :
									sign = True
									continue
								try :
									if cursor != "," and cursor != "|":
										nums = nums + cursor
										
										continue
									elif cursor == "," or cursor == "|" :
										nums = float(nums)
										if cursor == "," :
											if switch :
												if sign :
													nums*= -1
													sign = False
												dataY.append(nums)
												nums = ""
											else :
												if sign :
													nums*= -1
													sign = False
												dataX.append(nums)
												nums = ""
										elif cursor == "|" :
											if switch :
												if sign :
													nums*= -1
													sign = False
												dataY.append(nums)
												nums = ""
											else :
												if sign :
													nums*= -1
													sign = False
												dataX.append(nums)
												nums = ""

											switch = True
								except :
									print("Wrong File Format!")
									SuccessState = False

							SuccessState = True
							f.close()
							ScanRun = False
								
						if SuccessState :
							data = "x = {}, y = {}".format(dataX,dataY)
							print("data added!")
							break

						else :
							print("Due an Error was Found While Reading the File, Program will Back to Previous Menu ...")
							dataX = []
							dataY = []
							tm.sleep(3)
							Flow = False
							break
					break
				# Proccessing Data  #
				elif SubMenu_input == "3":
					print(pt.path(m=2,u0 = 2))
					x_soal = float(input("Enter x to estimate: "))
					data_len = len(dataX)
					x = np.zeros(data_len)
					y = np.zeros(data_len)
					i =0
					for temp in dataX :
						x[i] = temp
						i+=1
					i = 0
					for temp in dataY :
						y[i] = temp
						i += 1

					n = x.size
					x_total = 0
					y_total = 0
					x_sq_total = 0
					xy_total = 0
					for i in range (n):
						x_total = x_total + x[i]
						y_total = y_total + y[i]
						x_sq_total = x_sq_total + x[i] * x[i]
						xy_total = xy_total + x[i] * y[i]
					b = (n * xy_total - x_total * y_total) / (n * x_sq_total - (x_total) * x_total)
					a = y_total/n - b * x_total/n
					y_jawab = a+b*x_soal

					
					xmax = int(np.amax(x))
					Nx = 100*xmax
					x_plot = [0 for i in range(Nx)]
					y_plot = [0 for i in range(Nx)]
					for i in range (Nx):
						x_plot[i] = (1.5 / 100.0) * i
						y_plot[i] = a+b*x_plot[i]
					fig, ax = plt.subplots()
					ax.plot(x, y, 'ro', label='data')
					ax.plot(x_soal, y_jawab, 'bs', label='estimated point')
					if b >= 0:
						b = "+" + str(b)
					ax.plot(x_plot, y_plot, 'g', label="regression line")
					
					print("Estimated y for x = ", x_soal, " is : ", y_jawab)
					legend = ax.legend()
					plt.xlabel("x")
					plt.ylabel("f(x) = y")
					temp = input("Do you want show the plot or save the plot?\n[show/save/both] = ")
					if temp == "show" :
						plt.show()
					elif temp == "save" :
						name = input("Enter figure's name = ")
						plt.savefig(name+".jpg")
						print("picture saved in working directory..")
					elif temp == "both" :
						name = input("Enter figure's name = ")
						plt.savefig(name+".jpg")
						print("picture saved in working directory..")
						plt.show()
						

					write_to_file = "data x = {}\ndata y = {}\nestimated y from x = {}, is = {}\nwith regression line = {}{}x".format(dataX,dataY,x_soal,y_jawab,a,b)


					option = input("Do you want to save this solution ? [y/n]")
					if option == "y" :
						os_user = input("Do you use linux or windows ?")
						filename = input("Please input file's name \n\nEnter name : ")
						cwd = os.getcwd()
						if os_user == "linux" :
							check = "/Saved Solution/Regression/"
						elif os_user == "windows" :
							check = "\\Saved Solution\\Regression\\"
						if os.path.isdir(cwd+check) :
							pass
						else :
							os.makedirs(cwd+check)

						filename = filename + '.txt'
						if os_user == "linux":
							filename = cwd + check + filename 
						else :
							filename = cwd + check + filename 

						f = open(filename,"w")
						f.write(write_to_file)
						f.close()
						print("File saved in ",filename)
						misc = input("Press enter go back")

					else :
						print("file not saved")
						write_to_file = ""
						pass
					misc = input("Press enter to go back")

		elif SubMenu_input == "back"  :
			return False
		elif SubMenu_input == "home" :
			return False
		else :
			err.error(0,SubMenu_input)
			return True