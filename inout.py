my_output_file = open("hello.txt", "a")

lines_to_write = ["This is my file.", "\n There are many like it,", "\nbut this one is mine."]
my_output_file.writelines(lines_to_write)

my_output_file.close()