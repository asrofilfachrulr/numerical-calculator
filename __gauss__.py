# import all necessary libary
import numpy as np
import matplotlib.pyplot as plt
import pathfunc as pt 		# stored menu path
import errorlist as err 	# library to show error, condition-based
import time as tm
import os 
np.set_printoptions(suppress=True)
os_user = "windows"

def gaussmenu():
	'''
	Contains :
	1. Gauss Menu
	2. Input Equation Data
	3. Processing Data to Find Solution Based
		Gauss Naive Method
	4. Showing Solutions
	5. Option to Operate Data or Solution with File
	'''
	gauss_equation = "" # will be stored with coefficent of all variables and its result
	matrix_element = []
	x = []
	# Logical path and gauss menu
	print(pt.path(m = 0),"\nHere just take deal with system of linear equations\n1. 3 Variables\n2. 4 Variables\n3. 5 Variables\n\ntype 'back' to go back to previous menu\ntype 'home' to go back to main menu\n\n")
	SubMenu_input = input("Enter Menu : ")

	if SubMenu_input == "1" or SubMenu_input == "2" or SubMenu_input ==  "3" :
		Solutions = False
		if SubMenu_input == "1" :
			var = 3
		elif SubMenu_input == "2" :
			var = 4
		elif SubMenu_input == "3" :
			var = 5
		while True :
			if gauss_equation == "" :
				print(pt.path(m = 0,g0 = int(SubMenu_input)-1),"\nGauss Matrix :",gauss_equation,"\n1. Enter Manually\n2. Extract from File\n3. Find and Show Solutions\n4. Write Solutions into a File\n\ntype 'back' to go back to previous menu\ntype 'home' to go back to main menu\n\n")
			elif gauss_equation != "" :
				print(pt.path(m = 0,g0 = int(SubMenu_input)-1),"\nGauss Matrix :",gauss_equation,"\n1. Replace Equations Manually\n2. Replace Equations and Extract from File\n3. Find and Show Solutions\n4. Write Solutions into a File\n\ntype 'back' to go back to previous menu\ntype 'home' to go back to main menu\nWARNING : back to previous menu or go to main menu will erase equation that you've entered\n")

			SubSubMenu_input = input("Enter Menu : ")
			if SubSubMenu_input == "home" :
				return False
			elif SubSubMenu_input == "back" :
				return True

			#	ENTER MANUALLY FEATURE	#
			elif SubSubMenu_input == "1" :
				Solutions = False  # state to forbid another menu
				print(pt.path(m = 0, g0 = int(SubMenu_input)-1, u = 0)) # universal path, user input based


			#	for 3 variables 	#
				if var == 3 :
					print("General Form :\na11x1 + a12x2 + a13x3 = c1		[a11 a12 a13|c1]\na21x1 + a22x2 + a23x3 = c2 ==>	[a21 a22 a23|c2]\na31x1 + a32x2 + a33x3 = c3		[a31 a32 a33|c3]\nwith a is coefficient , x is variabel and c is the yield. Please mind the Gauss' pitfalls during entering matrix elements!")
					matrix_element = []	# start value
					print("Enter elements : (enter 'cancel' anytime to abort this action and go to previous menu) \n")
					
					# entering matrix element
					cancel = False
					row,column = 1,1
					while row <=3 :
						if cancel :
							break
						while column <=3 :
							if cancel :
								break
							try :
								temp = input("a{i}{j} = ".format(i = row, j = column))
								matrix_element.append(float(temp))
								column += 1
							except :
								if temp == "cancel" :
									cancel = 'True'
								else :
									err.error(2,temp)
						row+=1
						column=1
									

					row = 1
					while row <= 3 :
						if cancel :
							break
						try :
							temp = input("c{i} = ".format(i = row))

							matrix_element.append(float(temp))
							row += 1
						except :
								if temp == "cancel" :
									cancel = 'True'
									break
								else :
									error(2,temp)
							
	
					if cancel :
						pass
					elif cancel != True :
						gauss_equation = "\n[{0} {1} {2}|{3}]\n[{4} {5} {6}|{7}]\n[{8} {9} {10}|{11}]".format(matrix_element[0],matrix_element[1],matrix_element[2],matrix_element[9],matrix_element[3],matrix_element[4],matrix_element[5],matrix_element[10],matrix_element[6],matrix_element[7],matrix_element[8],matrix_element[11])
			
			#	for 4 variables 	# 	
				elif var == 4 :
					print("General Form :\na11x1 + a12x2 + a13x3 + a14x4 = c1		[a11 a12 a13 a14|c1]\na21x1 + a22x2 + a23x3 + a24x4 = c2 ==>	[a21 a22 a23 a24|c2]\na31x1 + a32x2 + a33x3 + a34x4 = c3		[a31 a32 a33 a34|c3]\na41x1 + a42x2 + a43x3 + a44x4 = c4		[a41 a42 a43 a44|c4]\nwith a is coefficient , x is variabel and c is the yield. Please mind the Gauss' pitfalls during entering matrix elements!")
					matrix_element = []	#start value
					print("Enter elements : (enter 'cancel' anytime to abort this action and go to previous menu) \n")
					# entering matrix element
					cancel = False
					row,column = 1,1
					while row <=4 :
						if cancel :
							break
						while column <=4 :
							if cancel :
								break
							try :
								temp = input("a{i}{j} = ".format(i = row, j = column))
								matrix_element.append(float(temp))
								column += 1
							except :
								if temp == "cancel" :
									cancel = 'True'
								else :
									err.error(2,temp)
						row+=1
						column=1
									

					row = 1
					while row <= 4 :
						if cancel :
							break
						try :
							temp = input("c{i} = ".format(i = row))

							matrix_element.append(float(temp))
							row += 1
						except :
								if temp == "cancel" :
									cancel = 'True'
									break
								else :
									err.error(2,temp)
							
	
					if cancel :
						pass
					elif cancel != True :
						gauss_equation = "\n[{0} {1} {2} {3}|{4}]\n[{5} {6} {7} {8}|{9}]\n[{10} {11} {12} {13}|{14}]\n[{15} {16} {17} {18}|{19}]".format(matrix_element[0],matrix_element[1],matrix_element[2],matrix_element[3],matrix_element[16],matrix_element[4],matrix_element[5],matrix_element[6],matrix_element[7],matrix_element[17],matrix_element[8],matrix_element[9],matrix_element[10],matrix_element[11],matrix_element[18],matrix_element[12],matrix_element[13],matrix_element[14],matrix_element[15],matrix_element[19])
				# 	for 5 variables 	#
				elif var == 5 :
					print("General Form :\na11x1 + a12x2 + a13x3 + a14x4 + a15x5 = c1		[a11 a12 a13 a14 a15|c1]\na21x1 + a22x2 + a23x3 + a24x4 + a25x5 = c2 		[a21 a22 a23 a24 a25|c2]\na31x1 + a32x2 + a33x3 + a34x4 + a35x5 = c3 ==>	[a31 a32 a33 a34 a35|c3]\na41x1 + a42x2 + a43x3 + a44x4 + a45x5 = c4		[a41 a42 a43 a44 a45|c4]\na51x1 + a52x2 + a53x3 + a54x4 + a55x5 = c5		[a51 a52 a53 a54 a55|c5]\nwith a is coefficient , x is variabel and c is the yield. Please mind the Gauss' pitfalls during entering matrix elements!")
					matrix_element = []	#start value
					print("Enter elements : (enter 'cancel' anytime to abort this action and go to previous menu) \n")
					# entering matrix element
					cancel = False
					row,column = 1,1
					while row <=5 :
						if cancel :
							break
						while column <=5 :
							if cancel :
								break
							try :
								temp = input("a{i}{j} = ".format(i = row, j = column))
								matrix_element.append(float(temp))
								column += 1
							except :
								if temp == "cancel" :
									cancel = 'True'
								else :
									err.error(2,temp)
						row+=1
						column=1
									

					row = 1
					while row <= 5 :
						if cancel :
							break
						try :
							temp = input("c{i} = ".format(i = row))

							matrix_element.append(float(temp))
							row += 1
						except :
								if temp == "cancel" :
									cancel = 'True'
									break
								else :
									err.error(2,temp)
							
	
					if cancel :
						pass
					elif cancel != True :
						gauss_equation = "\n[{0} {1} {2} {3} {4}|{5}]\n[{6} {7} {8} {9} {10}|{11}]\n[{12} {13} {14} {15} {16}|{17}]\n[{18} {19} {20} {21} {22}|{23}]\n[{24} {25} {26} {27} {28}|{29}]".format(matrix_element[0],matrix_element[1],matrix_element[2],matrix_element[3],matrix_element[4],matrix_element[25],matrix_element[5],matrix_element[6],matrix_element[7],matrix_element[8],matrix_element[9],matrix_element[26],matrix_element[10],matrix_element[11],matrix_element[12],matrix_element[13],matrix_element[14],matrix_element[27],matrix_element[15],matrix_element[16],matrix_element[17],matrix_element[18],matrix_element[19],matrix_element[28],matrix_element[20],matrix_element[21],matrix_element[22],matrix_element[23],matrix_element[24],matrix_element[29])

			#	EXTRACT FROM FILE FEATURE	#
			elif SubSubMenu_input == "2" :
				Solutions = False
				AddMatrixState = False
				os_user = input("Do you use linux or windows?\n")

				print(pt.path(m = 0, g0 = int(SubMenu_input)-1, u = int(SubSubMenu_input)-1))
				if var == 3 :
					print("File must be .txt and contains following format (please mind the gauss' pitfalls) = c11x1+c12x2+c13x3=a1|c21x1+c22x2+c23x3=a2|c31x1+c32x2+c33x3=a3|\nWith c is constant and a is yield. If the constant is 1 or 0, just write it(ex = 1x2 / 0x1). Please don't insert anything out from format.\nPutting wrong format impact extracting may fail or misread")
				elif var == 4 :
					print("File must be .txt and contains following format (please mind the gauss' pitfalls) = c11x1+c12x2+c13x3+c14x4=a1|c21x1+c22x2+c23x3+c24x4=a2|c31x1+c32x2+c33x3+c34x4=a3|c41x1+c42x2+c43x3+c44x4=a4|\nWith c is constant and a is yield. If the constant is 1 or 0, just write it(ex = 1x2 / 0x1). Please don't insert anything out from format.\nPutting wrong format impact extracting may fail or misread")
				elif var == 5 :
					print("File must be .txt and contains following format (please mind the gauss' pitfalls) = c11x1+c12x2+c13x3+c14x4+c15x5=a1|c21x1+c22x2+c23x3+c24x4+c25x5=a2|c31x1+c32x2+c33x3+c34x4+c35x5=a3|c41x1+c42x2+c43x3+c44x4+c45x5=a4|c51x1+c52x2+c53x3+c54x4+c55x5=a5|\nWith c is constant and a is yield. If the constant is 1 or 0, just write it(ex = 1x2 / 0x1). Please don't insert anything out from format.\nPutting wrong format impact extracting may fail or misread")
				temp = input("\nPlease choose method to open the file :\n1. Enter Full Path of Directory\n2. Enter File's Name(select this IF ONLY particular file's directory and file's application directory is same\n\nEnter Menu : ")
				
				while True :
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
						break
					
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
						break
					else :
						print("wrong input, please try again")
						temp = input("\nPlease choose method to open the file :\n1. Enter Full Path of Directory\n2. Enter File's Name(select this IF ONLY particular file's directory and file's application directory is same)")
						continue
				while ScanRun :	
					constants = [] 
					yields = [] 
					c = open(filepath,"r")
					sign = False
					index = 1
					nums = ''
					skip = False
					for cursor in c.read() :

						if cursor == "-" :
							sign = True
							continue
						if skip :
							skip = False
							continue
						try :
							if cursor != "x" and cursor != "+" and cursor != "=" and cursor != "|":
								nums = nums + cursor
								continue
							elif cursor == "x" or cursor == "+" or cursor == "|":
								if cursor == "x" :
									skip = True
								elif cursor == "+" or cursor == "=" :
									continue
								nums = int(nums)
								if var == 3 :
									if index % 4 != 0 :
										if sign :
											nums*= -1
											sign = False
										constants.append(nums)
										nums = ''
										index += 1
									elif index % 4 == 0 :
										if sign :
											nums*= -1
											sign = False
										yields.append(nums)
										nums = ''
										index += 1
								elif var == 4 :
									if index % 5 != 0 :
										if sign :
											nums*= -1
											sign = False
										constants.append(nums)
										nums = ''
										index += 1
									elif index % 5 == 0 :
										if sign :
											nums*= -1
											sign = False
										yields.append(nums)
										nums = ''
										index += 1
								elif var == 5 :
									if index % 6 != 0 :
										if sign :
											nums*= -1
											sign = False
										constants.append(nums)
										nums = ''
										index += 1
									elif index % 6 == 0 :
										if sign :
											nums*= -1
											sign = False
										yields.append(nums)
										nums = ''
										index += 1
							AddMatrixState = True
						except :
							print("Wrong File Format!")
							AddMatrixState = False

					c.close()
					if AddMatrixState :
						for i in constants :
							matrix_element.append(i)
						for i in yields :
							matrix_element.append(i)
						if var == 3 :
							gauss_equation = "\n[{0} {1} {2}|{3}]\n[{4} {5} {6}|{7}]\n[{8} {9} {10}|{11}]".format(matrix_element[0],matrix_element[1],matrix_element[2],matrix_element[9],matrix_element[3],matrix_element[4],matrix_element[5],matrix_element[10],matrix_element[6],matrix_element[7],matrix_element[8],matrix_element[11])
						elif var == 4 :
							gauss_equation = "\n[{0} {1} {2} {3}|{4}]\n[{5} {6} {7} {8}|{9}]\n[{10} {11} {12} {13}|{14}]\n[{15} {16} {17} {18}|{19}]".format(matrix_element[0],matrix_element[1],matrix_element[2],matrix_element[3],matrix_element[16],matrix_element[4],matrix_element[5],matrix_element[6],matrix_element[7],matrix_element[17],matrix_element[8],matrix_element[9],matrix_element[10],matrix_element[11],matrix_element[18],matrix_element[12],matrix_element[13],matrix_element[14],matrix_element[15],matrix_element[19])
						elif var == 5 :
							gauss_equation = "\n[{0} {1} {2} {3} {4}|{5}]\n[{6} {7} {8} {9} {10}|{11}]\n[{12} {13} {14} {15} {16}|{17}]\n[{18} {19} {20} {21} {22}|{23}]\n[{24} {25} {26} {27} {28}|{29}]".format(matrix_element[0],matrix_element[1],matrix_element[2],matrix_element[3],matrix_element[4],matrix_element[25],matrix_element[5],matrix_element[6],matrix_element[7],matrix_element[8],matrix_element[9],matrix_element[26],matrix_element[10],matrix_element[11],matrix_element[12],matrix_element[13],matrix_element[14],matrix_element[27],matrix_element[15],matrix_element[16],matrix_element[17],matrix_element[18],matrix_element[19],matrix_element[28],matrix_element[20],matrix_element[21],matrix_element[22],matrix_element[23],matrix_element[24],matrix_element[29])
						break
					else :
						print("Due an Error was Found While Reading the File, Program will Back to Previous Menu ...")
						tm.sleep(3)
						break

			#	SOLVING EQUATION 	#
			elif SubSubMenu_input == "3" :

				print(pt.path(m = 0, g0 = int(SubMenu_input)-1, u = int(SubSubMenu_input)-1))
				if gauss_equation != "":

					#	for 3 variables 	#
					if var == 3 : 
						a = np.array([[matrix_element[0],matrix_element[1],matrix_element[2]],[matrix_element[3],matrix_element[4],matrix_element[5]],[matrix_element[6],matrix_element[7],matrix_element[8]]])
						b=[matrix_element[9], matrix_element[10], matrix_element[11]]
						[m,n]=a.shape
						
						a1 = np.zeros((m,n))
						b1 = np.zeros(m)
						for i in range (0,m):
							for j in range (0,n):
								a1[i,j]=a[i,j]*a[0,0]*a[1,0]*a[2,0]/a[i,0]
							b1[i]=b[i]*a[0,0]*a[1,0]*a[2,0]/a[i,0]
						for i in range (1,m):
							for j in range(0,n):
								a1[i,j]=a1[i,j]-a1[0,j]
							b1[i]=b1[i]-b1[0]
						a2 = np.zeros((m,n))
						b2 = np.zeros(m)
						for i in range (0,m):
							for j in range(0,n):
								a2[i,j]=a1[i,j]
							b2[i]=b1[i]
						for i in range (1,m):
							for j in range(0,n):
								a2[i,j]=a1[i,j]*a1[1,1]*a1[2,1]/a1[i,1]
							b2[i]=b1[i]*a1[1,1]*a1[2,1]/a1[i,1]
						for i in range (2,m):
							for j in range(0,n):
								a2[i,j]=a2[i,j]-a2[1,j]
							b2[i]=b2[i]-b2[1]
						x = np.zeros(m)

						x[2]=b2[2]/a2[2,2]
						x[1]=[b2[1]-a2[1,2]*x[2]]/a2[1,1]
						x[0]=[b2[0]-a2[0,2]*x[2]- a2[0,1]*x[1]]/a2[0,0]

						print("please wait ... ")
						tm.sleep(3)
						print("x1 = ",x[0])
						print("x2 = ",x[1])
						print("x3 = ",x[2])
						
					#	for  4 variables 	#
					elif var == 4 :
						a = np.array([[matrix_element[0],matrix_element[1],matrix_element[2],matrix_element[3]],[matrix_element[4],matrix_element[5],matrix_element[6],matrix_element[7]],[matrix_element[8],matrix_element[9],matrix_element[10],matrix_element[11]],[matrix_element[12],matrix_element[13],matrix_element[14],matrix_element[15]]]) 
						b=[matrix_element[16], matrix_element[17], matrix_element[18],matrix_element[19]]
						[m,n]=a.shape #memuatdimensimatriks 
						a1=np.zeros((m,n)) 
						b1=np.zeros(m) 
						#loop 
						for i in range(0,m): #baris 
							for j in range(0,n): #kolom 
								a1[i,j]=a[i,j]*a[0,0]*a[1,0]*a[2,0]*a[3,0]/a[i,0] 
							b1[i]=b[i]*a[0,0]*a[1,0]*a[2,0]*a[3,0]/a[i,0] 
						for i in range(1,m): 
							for j in range(0,n): 
								a1[i,j]=a1[i,j]-a1[0,j] 
							b1[i]=b1[i]-b1[0] 
						a2=np.zeros((m,n)) 
						b2=np.zeros(m) 
						for i in range(0,m): #copymatriks 
							for j in range(0,n): 
								a2[i,j]=a1[i,j] 
							b2[i]=b1[i] 
						for i in range(1,m): #baris 
							for j in range(0,n): #kolom 
								a2[i,j]=a1[i,j]*a1[1,1]*a1[2,1]*a1[3,1]/a1[i,1] 
							b2[i]=b1[i]*a1[1,1]*a1[2,1]*a1[3,1]/a1[i,1] 
						for i in range(2,m): 
							for j in range(0,n): 
								a2[i,j]=a2[i,j]-a2[1,j] 
							b2[i]=b2[i]-b2[1] 
						a3=np.zeros((m,n)) 
						b3=np.zeros(m) 
						for i in range(0,m): #copymatriks 
							for j in range(0,n): 
								a3[i,j]=a2[i,j] 
							b3[i]=b2[i] 
						for i in range(2,m): #baris 
							for j in range(0,n): #kolom 
								a3[i,j]=a2[i,j]*a2[2,2]*a2[3,2]/a2[i,2] 
							b3[i]=b2[i]*a2[2,2]*a2[3,2]/a2[i,2] 
						for i in range(3,m): 
							for j in range(0,n): 
								a3[i,j]=a3[i,j]-a3[2,j] 
							b3[i]=b3[i]-b3[2] 
						x=np.zeros(m) 
						x[3]=b3[3]/a3[3,3] 
						x[2]=[b3[2]-a3[2,3]*x[3]]/a3[2,2] 
						x[1]=[b3[1]-a3[1,3]*x[3]-a3[1,2]*x[2]]/a3[1,1] 
						x[0]=[b3[0]-a3[0,3]*x[3]-a3[0,2]*x[2]-a3[0,1]*x[1]]/a3[0,0] 


						print("please wait ... ")
						tm.sleep(3)
						print("x1 = ",x[0])
						print("x2 = ",x[1])
						print("x3 = ",x[2])
						print("x4 = ", x[3])

					elif var == 5 :
						a = np.array([[matrix_element[0],matrix_element[1],matrix_element[2],matrix_element[3],matrix_element[4]],[matrix_element[5],matrix_element[6],matrix_element[7],matrix_element[8],matrix_element[9]],[matrix_element[10],matrix_element[11],matrix_element[12],matrix_element[13],matrix_element[14]],[matrix_element[15],matrix_element[16],matrix_element[17],matrix_element[18],matrix_element[19]],[matrix_element[20],matrix_element[21],matrix_element[22],matrix_element[23],matrix_element[24]]]) 
						b=[matrix_element[25], matrix_element[26], matrix_element[27],matrix_element[28],matrix_element[29]]
						[m,n]=a.shape #memuatdimensimatriks 
						
						a1=np.zeros((m,n)) 
						b1=np.zeros(m)  
						for i in range(0,m): #baris 
							for j in range(0,n): #kolom 
								a1[i,j]=a[i,j]*a[0,0]*a[1,0]*a[2,0]*a[3,0]*a[4,0]/a[i,0] 
							b1[i]=b[i]*a[0,0]*a[1,0]*a[2,0]*a[3,0]*a[4,0]/a[i,0] 
						for i in range(1,m): 
							for j in range(0,n): 
								a1[i,j]=a1[i,j]-a1[0,j] 
							b1[i]=b1[i]-b1[0] 


						a2=np.zeros((m,n)) 
						b2=np.zeros(m) 
						for i in range(0,m): #copymatriks 
							for j in range(0,n): 
								a2[i,j]=a1[i,j] 
							b2[i]=b1[i] 
						for i in range(1,m): #baris 
							for j in range(0,n): #kolom 
								a2[i,j]=a1[i,j]*a1[1,1]*a1[2,1]*a1[3,1]*a1[4,1]/a1[i,1] 
							b2[i]=b1[i]*a1[1,1]*a1[2,1]*a1[3,1]*a1[4,1]/a1[i,1] 
						for i in range(2,m): 
							for j in range(0,n): 
								a2[i,j]=a2[i,j]-a2[1,j] 
							b2[i]=b2[i]-b2[1] 


						a3=np.zeros((m,n)) 
						b3=np.zeros(m) 
						for i in range(0,m): #copymatriks 
							for j in range(0,n): 
								a3[i,j]=a2[i,j] 
							b3[i]=b2[i] 
						for i in range(2,m): #baris 
							for j in range(0,n): #kolom 
								a3[i,j]=a2[i,j]*a2[2,2]*a2[3,2]*a2[4,2]/a2[i,2] 
							b3[i]=b2[i]*a2[2,2]*a2[3,2]*a2[4,2]/a2[i,2] 
						for i in range(3,m): 
							for j in range(0,n): 
								a3[i,j]=a3[i,j]-a3[2,j] 
							b3[i]=b3[i]-b3[2]


						a4=np.zeros((m,n)) 
						b4=np.zeros(m) 
						for i in range(0,m): #copymatriks 
							for j in range(0,n): 
								a4[i,j]=a3[i,j] 
							b4[i]=b3[i] 
						for i in range(3,m): #baris 
							for j in range(0,n): #kolom 
								a4[i,j]=a3[i,j]*a3[3,3]*a3[4,3]/a3[i,3] 
							b4[i]=b3[i]*a3[3,3]*a3[4,3]/a3[i,3] 
						for i in range(4,m): 
							for j in range(0,n): 
								a4[i,j]=a4[i,j]-a4[3,j] 
							b4[i]=b4[i]-b4[3]
						

						x=np.zeros(m)
						x[4]=b4[4]/a4[4,4] 
						x[3]=[b4[3]-a4[3,4]*x[4]]/a4[3,3] 
						x[2]=[b4[2]-a4[2,4]*x[4]-a4[2,3]*x[3]]/a4[2,2] 
						x[1]=[b4[1]-a4[1,4]*x[4]-a4[1,3]*x[3]-a4[1,2]*x[2]]/a4[1,1] 
						x[0]=[b4[0]-a4[0,4]*x[4]-a4[0,3]*x[3]-a4[0,2]*x[2]-a4[0,1]*x[1]]/a4[0,0]

						for i in range(0,5):
							print("x{} = {}".format(i,x[i])) 



					while True :
						m = input("press enter to go to previous menu")
						Solutions = True
						if m == "":
							break					
				else :
					print("Please enter equations first!")

			# 	SAVE TO FILE FEATURE 	#
			elif SubSubMenu_input == "4" :
				if Solutions:
					index = 0
					elements = []
					if var == 3 :
						for i in matrix_element:
							if i >= 0 and index !=0 and index !=9 and index != 3 and index != 10 and index != 11 and index != 6 :
								i = " + " + str(i)
							elif i < 0 and index !=0 and index !=9 and index != 3 and index != 10 and index != 11 and index != 6 :
								i = " - " + str(i)
							elements.append(i)
							index+=1
					elif var == 4 :
						for i in matrix_element :
							if i >= 0 and index != 16 and index != 17 and index != 18 and index != 19 and index != 0 and index != 4 and index != 8 and index != 12  :
								i = " + " + str(i)
							elif i < 0 and index != 16 and index != 17 and index != 18 and index != 19 and index != 0 and index != 4 and index != 8 and index != 12  :
								i = " - " + str(i)
							elements.append(i)
							index+=1
					elif var == 5 :
						for i in matrix_element :
							if i >= 0 and index != 25 and index != 26 and index != 27 and index != 28 and index != 29 and index != 0 and index != 5 and index != 10 and index != 15 and index != 20 :
								i = " + " + str(i)
							elif i < 0 and index != 25 and index != 26 and index != 27 and index != 28 and index != 29 and index != 0 and index != 5 and index != 10 and index != 15 and index != 20 :
								i = " - " + str(i)
							elements.append(i)
							index+=1
					filename = input("Please input file's name \n\nEnter name : ")
					filename = filename + '.txt'
					cwd = os.getcwd()
					if os_user == "linux" :
						check = "/Saved Solution/Gauss/"
					elif os_user == "windows":
						check = "\\Saved Solution\\Gauss\\"
					if os.path.isdir(cwd+check) :
						pass
					else :
						os.makedirs(cwd+check)
					filename = cwd + check + filename
					f = open(filename,'w')
					if var == 3 :
						write = "Equations = \n{0}x1{1}x2{2}x3 = {3}\n{4}x1{5}x2{6}x3 = {7}\n{8}x1{9}x2{10}x3 = {11}\n\nSolutions =\nx1 = {12}\nx2 = {13}\nx3 = {14}\n".format(elements[0],elements[1],elements[2],elements[9],elements[3],elements[4],elements[5],elements[10],elements[6],elements[7],elements[8],elements[11],x[0],x[1],x[2])
					elif var == 4 :
						write ="Equations = \n{0}x1{1}x2{2}x3{3}x4 = {4}\n{5}x1{6}x2{7}x3{8}x4 = {9}\n{10}x1{11}x2{12}x3{13}x4 = {14}\n{15}x1{16}x2{17}x3{18}x4 = {19}\n\nSolutions =\nx1 = {20}\nx2 = {21}\nx3 = {22}\nx4 = {23}".format(elements[0],elements[1],elements[2],elements[3],elements[16],elements[4],elements[5],elements[6],elements[7],elements[17],elements[8],elements[9],elements[10],elements[11],elements[18],elements[12],elements[13],elements[14],elements[15],elements[19],x[0],x[1],x[2],x[3])
					elif var == 5 :
						write = "Equations = \n{0}x1{1}x2{2}x3{3}x4{4}x5 = {5}\n{6}x1{7}x2{8}x3{9}x4{10}x5 = {11}\n{12}x1{13}x2{14}x3{15}x4{16}x5 = {17}\n{18}x1{19}x2{20}x3{21}x4{22}x5 = {23}\n{24}x1{25}x2{26}x3{27}x4{28}x5 = {29}\n\nSolutions =\nx1 = {30}\nx2 = {31}\nx3 = {32}\nx4 = {33}\nx5 = {34}".format(elements[0],elements[1],elements[2],elements[3],elements[4],elements[25],elements[5],elements[6],elements[7],elements[8],elements[9],elements[26],elements[10],elements[11],elements[12],elements[13],elements[14],elements[27],elements[15],elements[16],elements[17],elements[18],elements[19],elements[28],elements[20],elements[21],elements[22],elements[23],elements[24],elements[29],x[0],x[1],x[2],x[3],[4])
					f.write(write)
					f.close()
					print("File have been made! \nFile Path = ",filename)
					misc = input("\n\nPress enter to go back")
				elif Solutions == False:
					print("Please select 'Find Solutions' first!")
			else :
				err.error(0,SubSubMenu_input)
	elif SubMenu_input == "back" :
		return False
	elif SubMenu_input == "home" :
		return False
	else :
		err.error(0,SubMenu_input)
		return True
