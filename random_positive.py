import sys, random
import csv

f = open('new_train_sample_positive.csv','w',newline='\n')
wr = csv.writer(f)
wr.writerow(['code1','code2','similar'])
row = 0 #17970

while(row<200): #pair 개수
    random_num = random.randint(1,300)
    random_dir = "problem"+str(random_num).zfill(3)
    code = []
    for _ in range(2):
        random_file = random.randint(1,150)
        file_name = random_dir+"/"+random_dir+"_"+str(random_file)+".py"
        #print(file_name)
        with open(file_name,'r') as file:
            code.append(file.readlines())
    wr.writerow([code[0],code[1],1])
    row +=1

f.close()