def path(**kwargs) :
	show_path = ""
	main = [" > Gauss Naive", " > Trapezoidal", " > Least Square Regression", " > Newton Interpolation Polynomial"]
	gauss_submenu0 = ["3 Variables", "4 Variables" ,"5 Variables"] 
	trapez_submenu0 = ["Second Degree Polynomial Equation","Third Degree Polynomial Equation","Fourth Degree Polynomial Equation"]
	universal_submenu = ["Enter Manually","Extract from File","Find and Show Solutions","Write Solutions into a File","Replace Equations Manually","Replace Equations and Extract from File"]
	universal_submenu0 = ["Enter Data (x,y) Manually","Extract Data from File","Process to Find the Estimated x or y","Replace Data (x,y) Manually","Replace Data from File"]
	
	item = 1

	if kwargs != None :
		for key,value in kwargs.items() :
			if key == "m" :
				key = main
			elif key == "g0" :
				key = gauss_submenu0
			elif key == "u" :
				key = universal_submenu
			elif key == "u0" :
				key = universal_submenu0
			elif key == "t0" :
				key = trapez_submenu0
			path_open = key[value]
			if item < len(kwargs.items()) :
				show_path = show_path + path_open + " > "
			elif item == len(kwargs.items()) :
				show_path = show_path + path_open
			item+=1

	return "____________________________________________________________________________________________________________\nMain Menu"+show_path+"\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"