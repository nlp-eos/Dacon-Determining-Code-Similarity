import sys, random
import csv

def random_negative(wr):
    code = []
    random_num1 = random.randint(1,300)
    while(True):
        random_num2 = random.randint(1,300)
        if random_num2 != random_num1:
            break
    random_dir1 = "problem"+str(random_num1).zfill(3)
    random_dir2 = "problem"+str(random_num2).zfill(3)
   
    random_file1 = random.randint(1,150)
    random_file2 = random.randint(1,150)
    file_name1 = random_dir1+"/"+random_dir1+"_"+str(random_file1)+".py"
    file_name2 = random_dir2+"/"+random_dir2+"_"+str(random_file2)+".py"
    print(file_name1, file_name2)
    with open(file_name1,'r') as file:
            code.append(file.readlines())
    with open(file_name2,'r') as file:
        code.append(file.readlines())
    
    wr.writerow([code[0],code[1],0])