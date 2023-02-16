class DotPair:
     def __init__(self, start):
          self.start = start
          self.end = -1

def findIndex(index):
     for p in range(len(loopPoints)):
          if loopPoints[p].start == index or loopPoints[p].end == index:
               return p
     return -1

try:
     filename = input("File name : ")
     file = open(filename, "r")
     code = file.read()
     file.close()
except:
     print("File could not open")
     a = input("\nClick to Close")

memory = [0]
loopPoints = []
memoryI = 0

for j in range(len(code)):
     if code[j] == "[":
          loopPoints.append(DotPair(j))

     elif code[j] == "]":
          for i in reversed(range(len(loopPoints))):
               if loopPoints[i].end == -1:
                    loopPoints[i].end = j
                    break
#---------------------------------------------------------------------------------

for l in loopPoints:
     if l.end == -1:
          print("There is a square brackets mistake")
          exit()
#---------------------------------------------------------------------------------

codeI = 0

while codeI < len(code):

     if code[codeI] == "+":
          if memory[memoryI] == 255:
               memory[memoryI] = 0
          else:
               memory[memoryI] += 1     
#---------------------------------------------------------------------------------

     elif code[codeI] == "-":
          if memory[memoryI] == 0:
               memory[memoryI] = 255
          else:
               memory[memoryI] -= 1    
#--------------------------------------------------------------------------------- 

     elif code[codeI] == ">":
          memoryI += 1
          if len(memory) - 1 < memoryI:
               memory.append(0)
#---------------------------------------------------------------------------------   
   
     elif code[codeI] == "<":
          if memoryI == 0:
               print("\n---You tried to access to -1 memoryI of memory---\n")
               break
          memoryI -= 1
#---------------------------------------------------------------------------------

     elif code[codeI] == ".":
          #print(memory[memoryI])
          print(chr(memory[memoryI]), end="")     

#---------------------------------------------------------------------------------

     elif code[codeI] == ",":
          memory[memoryI] = ord(input())
#---------------------------------------------------------------------------------

     elif code[codeI] == "[":
          if memory[memoryI] == 0:
               codeI = loopPoints[findIndex(codeI)].end
#---------------------------------------------------------------------------------

     elif code[codeI] == "]":
          if memory[memoryI] != 0:
               codeI = loopPoints[findIndex(codeI)].start
     
     codeI += 1

#a = input("\nPress A Key To Close")