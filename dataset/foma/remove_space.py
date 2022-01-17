import random

def myfunction():
  return 0.1

filename = "Data_SP2_20_New_F1.dat"

f = open("trash/"+filename,"r")
lines = f.readlines()
f.close()

# no_lines = int(len(lines)/20)
# random.shuffle(lines, myfunction)

new = ""
# index = 0

for line in lines:
	new += line.rstrip('\n').strip()
	# if(index == no_lines):
	# 	break
	# index += 1

f = open(filename,"w")
f.write(new)
f.close()
