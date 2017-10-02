import csv 
 
with  open('Crime.csv') as csvile:
    readCSV = csv.reader(csvfile,delimiter=',')
    print(readCSV)
    for row in readCSV:
        print (row)
 
f.close()

