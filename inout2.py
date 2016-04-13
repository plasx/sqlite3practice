my_input_file = open("hello.txt", "r")
line = my_input_file.readline()
while line != "":
	print(line),
	line = my_input_file.readline()

my_input_file.close()