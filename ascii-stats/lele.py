def readfile():
    filename = input("give file name you want to process: ")
    try:
     with open(filename, "r") as file:
      filecontent = file.readlines()
      return filecontent
    except FileNotFoundError:
        exit("File does not exist. Exiting..")

def processascii():
 filecontent = readfile()
 lines = list()
 for eachline in filecontent:
   lines.append(eachline.strip()) 
 return lines

def createsquare():
 getlines = processascii()
 xcordinate = int(input("X cordinate: "))
 ycordinate = int(input("Y cordinate: "))
 squaresize = int(input("square size: ")) 
 dataset = ""
 for verticalsort in range(ycordinate+1,ycordinate+squaresize+1):
  for horizonalsort in range(xcordinate+1,xcordinate+squaresize+1):
    dataset = dataset + getlines[verticalsort][horizonalsort]
 return dataset


def processdata():
 totalletters = 0
 thedata = createsquare()
 clearduplicate = set()
 for letters in thedata:
   clearduplicate.add(letters)
 for everyletter in clearduplicate:
   totalletters = totalletters + thedata.count(everyletter)
 for everyletter2 in clearduplicate:
   percentage = 100 * thedata.count(everyletter2) / totalletters
   print(everyletter2," -> ", percentage)


def main():
 processdata()

if __name__ == '__main__':
     main()