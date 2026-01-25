def getMap1():
 with open("map1.dat", "r") as map:
  map1 = map.readlines()  
  map1List = list()
 for eachLine in map1:
  map1List.append(list(eachLine.strip()))
 return map1List
  

def getMap2():
 with open("map2.dat", "r") as map:
  map2 = map.readlines()
  map2List = list()
 for eachLine in map2:
  map2List.append(list(eachLine.strip()))
 return map2List

def moves():
 with open("moves.txt", "r") as moves:
   moves = moves.readlines()
   moveList = list()
   player1MoveList = list()
   player2MoveList = list()
   for eachmove in moves:
    moveList.append(eachmove.strip())
   for splitPlayers in moveList:
    if moveList.index(splitPlayers) % 2 == 0:
     player1MoveList.append(splitPlayers)
    else:
     player2MoveList.append(splitPlayers)
   return [player1MoveList, player2MoveList, moveList]


def gameProcess():
 map1 = getMap1()
 map2 = getMap2()
 allMoves = moves()
 player1Moves = allMoves[0]
 player2Moves = allMoves[1]
 totalMoves = allMoves[2]
 alphatable = dict()
 alphatable = { 
  "A" : 0,
  "B" : 1,
  "C" : 2,
  "D" : 3,
  "E" : 4,
  "F" : 5,
  "G" : 6,
  "H" : 7,
  "I" : 8,
  "J" : 9
  }

 for everyRound in totalMoves:

    if totalMoves.index(everyRound) % 2 == 0:
        print("player 1's turn", end="\n")
        print("the coordinates of the shot: ", everyRound,end="\n")
        if map1[alphatable.get(everyRound[0])][int(everyRound[2])] == "-":
            map1[alphatable.get(everyRound[0])][int(everyRound[2])] = "o"
            print("result: Miss", end="\n\n")
        elif map1[alphatable.get(everyRound[0])][int(everyRound[2])] == "#":
            map1[alphatable.get(everyRound[0])][int(everyRound[2])] = "*"
            print("result: Hit", end="\n\n")
       # if map1.count("#") == 0:
          #  print("Player 1 Wins", end="\n")
    

    else:
        print("player 2's turn")
        print("the coordinates of the shot: ", everyRound,end="\n")
        if map2[alphatable.get(everyRound[0])][int(everyRound[2])] == "-":
            map2[alphatable.get(everyRound[0])][int(everyRound[2])] = "o"
            print("result: Miss", end="\n\n")
        elif map2[alphatable.get(everyRound[0])][int(everyRound[2])] == "#":
            map2[alphatable.get(everyRound[0])][int(everyRound[2])] = "*"
            print("result: Hit", end="\n\n")
      #  if map2.count("#") == 0:
       #     print("Player 2 Wins", end="\n")
    
    if totalMoves[-1] == everyRound:
      print("Player 1's table", end="\n")
      for allHorizonal in range(0,10):
        print("",end="\n")
        for allVertical in range(0,10):
          print(map1[allHorizonal][allVertical],end="")
    
      print("\n\n Player 2's table", end="\n")
      for allHorizonal2 in range(0,10):
        print("",end="\n")
        for allVertical2 in range(0,10):
          print(map2[allHorizonal2][allVertical2],end="")  

    totalShipPlayer1 = int()
    totalShipPlayer2 = int()
    for everyRow in map1:
      totalShipPlayer1 = totalShipPlayer1 + everyRow.count("#")
    if(totalShipPlayer1 == 0):
      print("\nPlayer 1 Wins")
     
    for everyRow2 in map2:
      totalShipPlayer2 = totalShipPlayer2 + everyRow2.count("#")
    if(totalShipPlayer2 == 0):
      print("\nPlayer 2 Wins")

def main():
 gameProcess()


if __name__ == '__main__':
 main()
