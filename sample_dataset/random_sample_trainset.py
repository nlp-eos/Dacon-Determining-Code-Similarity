import sys, random
import csv
from random_negative import random_negative
from random_positive import random_positive

path = str(sys.path[0])
f = open('new_train_sample.csv','w',newline='\n')
wr = csv.writer(f)
wr.writerow(['code1','code2','similar'])
row = 0 #17970
random_list = [random.randint(0,1) for r in range(30000)]
duplicate_check = []

while(row<30000): #pair 개수
    if row%100==0: print(row)
    if random_list[row] == 0:
        duplicate_check += random_positive(path,wr,duplicate_check)
    elif random_list[row] == 1:
        duplicate_check += random_negative(path,wr,duplicate_check)
    row +=1

f.close()