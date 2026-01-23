def determinenumber(num):
 sum = int()
 for i in str(num):
    sum = sum + pow(int(i),len(str(num)))
 if sum == num:
       return True
 else:
       return False


def fileprocess():
 #read
 try:
     with open("numbers.txt","r") as file:
         numsfromfile = file.readlines()
 except FileNotFoundError:
        exit("There isn't any file")
 
#split
 for each in numsfromfile:
     if determinenumber(int(each.strip())):
        with open("armstrong.txt","a") as file2:
            file2.writelines(each)
    


def main():
 fileprocess()



if __name__ == '__main__':
    main()