open_file = open('train.txt', 'r')
data = open_file.read()
new_data = data.replace("\n ","")

f = open('new_train.txt','w')
f.write(new_data)
f.close()