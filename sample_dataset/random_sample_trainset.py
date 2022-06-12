import sys, random
import csv

def random_positive(path,wr,duplicate_check):
    numbers = list(range(1,301))
    random_num = random.choice(numbers)
    random_dir = "problem"+str(random_num).zfill(3)
    code = []
    tuple_set = []
    for _ in range(2):
        random_file = random.randint(1,150)
        num = 0
        while (random_num,random_file) in duplicate_check and len(numbers)>0:
            random_file = random.randint(1,150)
            num += 1
            if num > 100:
                numbers.remove(random_num)
                random_num = random.choice(numbers)
                num=0
        tuple_set.append((random_num,random_file))
        file_name = path+"/"+random_dir+"/"+random_dir+"_"+str(random_file)+".py"
        #print(file_name)
        with open(file_name,'r') as file:
            code.append("".join(file.readlines()))
    wr.writerow([code[0],code[1],1])
    return tuple_set


def random_negative(path,wr,duplicate_check):
    code = []
    tuple_set = []
    random_num1 = random.randint(1,300)
    random_file1 = random.randint(1,150)
    num1 = 0
    while (random_num1,random_file1) in duplicate_check:
        random_file1 = random.randint(1,150)
        num1 += 1
        if num1>100:
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
            if num2>100:
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


if __name__ == "__main__":
    path = str(sys.path[0])
    f = open('new_train_sample_5.csv','w',newline='\n')
    wr = csv.writer(f)
    wr.writerow(['code1','code2','similar'])
    row = 0 #17970
    random_list = [random.randint(0,1) for r in range(50000)]
    duplicate_check_positive = []
    duplicate_check_negative = []

    while(row<50000): #pair 개수
        if row%100==0: print(row)
        if random_list[row] == 0:
            duplicate_check_positive += random_positive(path,wr,duplicate_check_positive)
        elif random_list[row] == 1:
            duplicate_check_negative += random_negative(path,wr,duplicate_check_negative)
        row +=1

    f.close()