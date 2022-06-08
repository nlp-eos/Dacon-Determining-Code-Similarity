import random

def random_negative(path,wr,duplicate_check):
    code = []
    tuple_set = []
    random_num1 = random.randint(1,300)
    random_file1 = random.randint(1,150)
    num1 = 0
    while (random_num1,random_file1) in duplicate_check:
        random_file1 = random.randint(1,150)
        num1 += 1
        if num1>20:
            random_num1 = random.randint(1,300)
            num1=0
    tuple_set.append((random_num1,random_file1))
    
    while(True):
        random_num2 = random.randint(1,300)
        if random_num2 != random_num1:
            break
    random_file2 = random.randint(1,150)
    num2=0
    while (random_num2,random_file2) in duplicate_check:
            random_file2 = random.randint(1,150)
            num2 +=1
            if num2>20:
                while(True):
                    random_num2 = random.randint(1,300)
                    if random_num2 != random_num1:
                        break
    tuple_set.append((random_num2,random_file2))
    
    random_dir1 = "problem"+str(random_num1).zfill(3)
    random_dir2 = "problem"+str(random_num2).zfill(3)
    
    file_name1 = path+"/"+random_dir1+"/"+random_dir1+"_"+str(random_file1)+".py"
    file_name2 = path+"/"+random_dir2+"/"+random_dir2+"_"+str(random_file2)+".py"
    #print(file_name1, file_name2)
    with open(file_name1,'r') as file:
            code.append("".join(file.readlines()))
    with open(file_name2,'r') as file:
        code.append("".join(file.readlines()))
    
    wr.writerow([code[0],code[1],0])
    return tuple_set