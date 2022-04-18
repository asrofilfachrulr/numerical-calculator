def error(code,input):
	errorlist = ["$ \"{}\" is wrong input, please mind to re-type your menu $\n".format(input),"$ Invalid path, please check again $\n","$ \"{}\" isn't an integer or a float, input must be integers or float $\n".format(input)]
	print("\nERROR CODE 0{x}".format(x = code)," :",errorlist[code])