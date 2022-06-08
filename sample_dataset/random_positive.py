import sys,random

def random_positive(path,wr,duplicate_check):
    random_num = random.randint(1,300)
    random_dir = "problem"+str(random_num).zfill(3)
    code = []
    tuple_set = []
    for _ in range(2):
        random_file = random.randint(1,150)
        num = 0
        while (random_num,random_file) in duplicate_check:
            random_file = random.randint(1,150)
            num += 1
            if num > 20:
                random_num = random.randint(1,300)
                num=0
        tuple_set.append((random_num,random_file))
        file_name = path+"/"+random_dir+"/"+random_dir+"_"+str(random_file)+".py"
        #print(file_name)
        with open(file_name,'r') as file:
            code.append("".join(file.readlines()))
    wr.writerow([code[0],code[1],1])
    return tuple_set