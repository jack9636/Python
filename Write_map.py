
#custom class tp find all the possible arcs
#Given the Format Letter + X +Y
#This class will find if another graph is a neighbpr or not
class Node(object):
    def __init__(self,char='' ,x=0, y=0):
        self.char=char
        self.x = x
        self.y = y

    def __str__(self):
        return self.char + str(self.x) + str(self.y)

    def equal(self,cmp):
        if((self.char==cmp.char)&(self.x==cmp.x)&(self.y==cmp.y)):
            return True;
        return False
#Check to see if a node is a neighbor to another node
    #will return true if they are neighbors and false otherwise
    #0-up left-1 right-2 down -4
    def neighbor(self,cmp):
        dir=-1
        flagd_U=0
        self_ds=ord(self.char)
        cmp_d=ord(cmp.char)


        diffx=cmp.x - self.x
        diffy=cmp.y - self.y

        diff=cmp_d-self_ds
#Difficult to read and probably not the best way to enforce the comparison between the points

        if((diff == 0)|(diff == 1)|( diff == -1)):
            if(diff==0):
             flagd_U=1
                #Determine whether the points are up or down
            if ((diffx == 0) | (diffx == 1)|(diffx == -1)):
                if(diffx==1):           #left turn
                    dir=2
                if(diffx==-1):          #right turn
                    dir=1
                # use to determine the right and left direction
                if ((diffy == 0) | (diffy == 1) |(diffy == -1)):
                    if(diffy==1):
                        dir=0
                    if(diffy==-1):
                        dir=3
                    if((abs(diffx)==1)&(abs(diffy)==1)):
                        return False, -1
                    return True, dir

        return False, -1

def bad_connection(BlackList,Node):
    for element in BlackList:
        if(Node.equal(element)):
            return True
    return False


file = open("Nodes_3.3.txt","w+")
#Initilize the naming convention that i like starting at A11-----etc
x=['A','B','C','D','E','F','G','H']
y=[1,2,3,4,5,6,7,8]
counter=1
#Store the node into a file
for i in range(8):
    for k in range(8):
        file.write(str(x[i]))
        file.write(str(counter));
        file.write(str(y[k]))
        file.write("\n")
    counter  +=1
file.close()

in_stream=open("Nodes_3.3.txt","r")

out_stream=open("Connections.txt","w+")
#File where the  black block should be store. Blacklist node will not connect to the graph
invaild_moves=open("BlackList.txt","r")

#unit testing
Test1=Node('A',1,1)
Test2=Node('B',1,1)
Test3=Node('A',1,2)
Test4=Node('A',3)
print(Test1.neighbor(Test2))
print(Test1.neighbor(Test3))
print(Test1.neighbor(Test4))

List = []
BlackList= []
#Testing backward list of nodes
for i in in_stream:
    strip =i.strip("\n")
    strip = i.strip(" ")
    char = i[0]
    x =int(i[1])
    y =int(i[2])
    List.append(Node(char,x,y))
Listb=[]
bcounter=len(List)-1
for backward in range(len(List)):
    i=List[bcounter]
    print(bcounter)
    bcounter-=1
    Listb.append(i)
print(Listb)

#Import Nodes that are not allowed
for i in invaild_moves:
    strip = i.strip("\n")
    strip = i.strip(" ")
    char = i[0]
    x = int(i[1])
    y = int(i[2])
    BlackList.append(Node(char, x, y))

#Create all the connections for the graph. This checks to see if the nodes are neighbor
#As well as enforcing a UP RIGHT LEFT DOWN reading for the arcs
for element1 in List:
    if(bad_connection(BlackList,element1)):
        continue
    out_stream.write(str(element1))
    out_stream.write(" ")

    up = None
    right = None
    left = None
    down = None

    for element2 in List:
        if(bad_connection(BlackList,element2)):
            continue
        if(element1.equal(element2)==False):
            bool, dir = element1.neighbor(element2)
            if(bool):
                print("\nParent "+str(element1))
                print(element2)
                print(dir)
                if dir==0:
                    up=element2
                if dir ==1:
                    right=element2
                if dir ==2:
                    left=element2
                if dir ==3:
                    down=element2

                #out_stream.write(str(element2))
                #out_stream.write(" ")
    if(up!=None):
      out_stream.write(str(up))
      out_stream.write(" ")
    if (left != None):
      out_stream.write(str(left))
      out_stream.write(" ")
    if (right != None):
      out_stream.write(str(right))
      out_stream.write(" ")
    if (down != None):
      out_stream.write(str(down))
      out_stream.write(" ")

    out_stream.write("\n")
print(Test2)
