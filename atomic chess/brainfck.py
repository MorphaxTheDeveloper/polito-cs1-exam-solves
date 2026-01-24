def gettxt():
 with open("game2.txt", "r") as gamefile:
      alltxt = gamefile.readlines()
 return alltxt
 
 
def edittxt():
 alltxt = gettxt()
 alltxtlist = list()
 for eachline in alltxt:   
    alltxtlist.append(eachline.strip())
 moves = alltxtlist[8:]
 gametable = alltxtlist[0:8]
 return [moves,gametable]


def makemove():
 getinstructions = edittxt()
 moves = getinstructions[0]
 gametable = getinstructions[1]
 print("initial table")
 for i in gametable:
  if i[0] == "|":
      print(" ",i,end="\n")
  else:
      print(i,end="\n")
  
 alphainfotable = {"a":0,
                   "b": 3,
                   "c": 6,
                   "d": 9,
                   "e": 12,
                   "f": 15,
                   "g": 18,
                   "h": 21}
 for eachmove in moves:
   firstlocation = eachmove[0:2]
   finishlocation = eachmove[3:5]

   firstlocation_horizonal = 8 - int(firstlocation[1])
   finishlocation_horizonal = 8 - int(finishlocation[1])

   firstlocation_vertical = alphainfotable.get(firstlocation[0])
   finishlocation_vertical = alphainfotable.get(finishlocation[0])

   stone_first_location = gametable[firstlocation_horizonal][firstlocation_vertical:firstlocation_vertical+2]
   stone_destination = gametable[finishlocation_horizonal][finishlocation_vertical:finishlocation_vertical+2]

   linethatneedstobechanged = gametable[finishlocation_horizonal]
   changedline = (
      linethatneedstobechanged[:finishlocation_vertical-2] +
      stone_first_location +
      linethatneedstobechanged[finishlocation_vertical:]
   )

   linethatneedstobedeleted = gametable[firstlocation_horizonal]
   deletedline = (
      linethatneedstobedeleted[:firstlocation_vertical] +
      "  " +
      linethatneedstobedeleted[firstlocation_vertical+2:]
   )

   gametable[firstlocation_horizonal] = deletedline
   gametable[finishlocation_horizonal] = changedline


   #gametable[firstlocation_horizonal][firstlocation_vertical:firstlocation_vertical+2] = gametable[finishlocation_horizonal][finishlocation_vertical+1:finishlocation_vertical+3]
   #gametable[finishlocation_horizonal][finishlocation_vertical+1:finishlocation_vertical+3] = "  "
   
   print("\n")
   print("move ",firstlocation," - ", finishlocation)
   for i in gametable:
    if i[0] == "|":
      print(" ",i,end="\n")
    else:
      print(i,end="\n")

   print("\n")
   if stone_destination == "K-":
     print("Black wins")
   elif stone_destination == "K+":
     print("White wins")

   

def main():
 makemove()


if __name__ == '__main__':
    main()