import sys, random
import csv

def random_positive(wr):
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