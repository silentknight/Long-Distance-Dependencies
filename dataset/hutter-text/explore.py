import time

f = open("text8","r")
data = f.read()
f.close()

valid = len(data[7011142:8528825])
test = len(data[8528826:10019983])
train = len(data[:7011141]+data[10019984:])

print valid/1000000.0, test/1000000.0, train/1000000.0
