import sys, random
import csv
from random_negative import random_negative
from random_positive import random_positive

f = open('new_train_sample.csv','w',newline='\n')
wr = csv.writer(f)
wr.writerow(['code1','code2','similar'])
row = 0 #17970
random_list = [random.randint(0,1) for r in range(20000)]

while(row<20000): #pair 개수
    if random_list[row] == 0:
        random_positive(wr)
    elif random_list[row] == 1:
        random_negative(wr)
    row +=1

f.close()
