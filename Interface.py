from Node import Node
from Math import Math
from Node import UnitTest
import logging
logging.basicConfig(filename="dane.txt",level=logging.DEBUG)
    

class TaskOne:

    def __init__(self):
        self.Root=Node()
        self.Calculations=Math()
        self.Current=self.Root
        self.Elements=[]
        self.buf=""
        self.Operations=["1.Example input",
                        "2.User input",
                        "3.Inorder",
                        "4.Find node",
                        "5.Current node",
                        "6.Set Current Node as Root",
                        "7.Math operations",
                        "8.Menu",
                        "9.Quit"]
        self.Math_Operations=["1.Sum",
                             "2.Average",
                             "3.Medium",
                             "4.Back"]

    def start(self, test=None, param=None):
        buffer=''
        if(test is None):
            self.menu()
        while(1):
            if(test is None):
                which=''
                while(1):
                    which=input('Wrtie the operation number: ')
                    try:
                        val=(int)(which)
                        if((type(val)==int)and(val<=10)and(val>0)):
                            break
                    except Exception as err:
                        print(err)
                    print("Wrong answer, try again")
            else:
                val=test
            if (val==1):
                self.exampleInput()
                if(not(test is Node)):
                    return
            elif (val==2):
                self.addNode(self.Current)
            elif (val==3):
                self.buf=""
                self.inorder(self.Current)
                if(not(test is Node)):
                    buffer=self.buf
                    return buffer
                print(self.buf)
            elif (val==4):
                self.searchForNode(self.Current, param)
                if(not(test is Node)):
                    return
            elif (val==5):
                if(not(test is Node)):
                    return self.currentInfo()
                print(self.currentInfo())
            elif (val==6):
                self.Current=self.Root
            elif (val==7):
                buffer =self.mathOperations(test)
                if(not(test is Node)):
                    return buffer
            elif (val==8):
                self.menu()
            else:
                break
        
    def makeSubtreeTable(self, parent=None):
        if(parent is None):
            parent=self.Current
        
        self.insertToTable(parent.retVal())
        if(type(parent.retLson()) == Node):
            self.makeSubtreeTable(parent.retLson())
        if(type(parent.retRson())== Node):
            self.makeSubtreeTable(parent.retRson())

    def insertToTable(self, val):
        if(type(val)!=int):
            raise Exception("Wrong type of data")
        size=len(self.Elements)
        if(size==0):
            self.Elements.append(val)
        else:
            for i in range(size):
                if(self.Elements[i]>=val):
                    self.Elements.insert(i,val)
                    return
            self.Elements.append(val)

    def searchForNode(self, parent=None, test=None):
        if(not(test is None))and(type(test)==int):
            i=test
        else:
            while(1):
                try:
                    i=(int)(input("value of node which you looking for: "))
                    if(type(i)!=int):
                        raise Exception("Wrong input, try again")
                    break
                except Exception as err:
                    print(err)
        if(parent==None):
            parent=self.Current
            
        return self.findNode(parent,i)

    def menu(self):
        for i in self.Operations:
                print(i)
            
    def exampleInput(self):
        if((self.Root).retVal()!=None):
            print("Operation is available only when tree is empty")
            return
        self.addNode(self.Root,5)
        self.addNode(self.Root,3,0)
        self.addNode(self.Root,7,1)
        self.Current=self.Root.retLson()
        self.addNode(self.Current,2,0)
        self.addNode(self.Current,5,1)
        self.Current=self.Root.retRson()
        self.addNode(self.Current,1,0)
        self.addNode(self.Current,0,1)
        self.Current=self.Current.retRson()
        self.addNode(self.Current,2,0)
        self.addNode(self.Current,8,1)
        self.Current=self.Current.retRson()
        self.addNode(self.Current,5,1)
        self.Current=self.Root

    def inorder(self, parent): #shows the tree-order
        if((parent is None)or(parent.retVal() is None)):
            return
        self.inorder(parent.retLson())
        self.buf+=(str)(parent.retVal())+" "
        #print(parent.retVal())
        self.inorder(parent.retRson())

    def addNode(self, parent, value='a', automatic=-1): #add node as one of the Current's sons or throw an exception, 
        if((type(parent) != Node)and(not(self.Root.retVal()is None))):
            raise Exception("This node doesn't exist")
        
        if(value=='a'):
            a=(int)(input("new node value: "))
        else:
            a=(int)(value)

        if(self.Root.retVal() is None):
            self.Root.setVal(a)
        else:
            l=0
            r=0
            
            if((parent.retRson() is None)):
                r=1
            if((parent.retLson() is None)):
                l=1

            if((l==1)and(r==1)):
                if(automatic==-1):
                    zmienna=input("Choose which sone (left: 0, right: else): ")
                    if(zmienna=="0"):
                        parent.setLson(a)
                    else:
                        parent.setRson(a)
                elif(automatic==0):
                        parent.setLson(a)
                else:
                        parent.setRson(a)
            elif ((l==1)and(r==0)):
                    parent.setLson(a)
            elif ((l==0)and(r==1)):
                    parent.setRson(a)
            else:
                raise Exception("This node already has sons")

    def findNode(self, parent, value): #finds Node or throws an Exception, return the first one that fits
        if(type(value)!=int ):
            raise Exception("Wrong type of data")
        if((type(parent)!=Node) or(parent.retVal() is None)):
            return

        if(parent.retVal()==value):
            self.Current=parent
            return 
       
        self.findNode(parent.retLson(),value)
        self.findNode(parent.retRson(),value)

    def currentInfo(self): #shows the info about the current node
        napis="Current node: "+(str)(self.Current.retVal())+" "
        if(not(self.Current.retLson()is None)):
            napis+="L:"+(str)(self.Current.retLson().retVal())+" "
        if(not(self.Current.retRson()is None)):
            napis+="R:"+(str)(self.Current.retRson().retVal())
        
        return napis
        
    def mathOperations(self, param=None):
        if(self.Current.retVal()==None):
            print("Tree doesn't exists")
            return 0
        self.makeSubtreeTable()
        if(len(self.Elements)==0):
            raise Exception("No elements")
        buf=''
        if(not (param is None)):
            buf+="sum: "+(str)(self.Calculations.sum(self.Elements))
            buf+="median: "+(str)(self.Calculations.median(self.Elements))
            buf+="average: "+(str)(self.Calculations.average(self.Elements))
        print("sum: "+(str)(self.Calculations.sum(self.Elements)))
        print("median: "+(str)(self.Calculations.median(self.Elements)))
        print("average: "+(str)(self.Calculations.average(self.Elements)))
        self.Elements.clear()
        return buf

    def unitTest(self):
        plik=open('dane.txt',"w")
        plik.close()

        if(self.Calculations.unitTest()==0):
            return
        if(UnitTest()==0):
            return

        logging.debug("Interface")
        
        mistakes=0

        self.Current=self.Root
        self.searchForNode(test=-1)
        if(self.currentInfo()!="Current node: None "):
            logging.debug("""self.currentInfo()!="Current node: None " """)
            mistakes+=1


        if(not(self.Root.retVal() is None)):
            logging.debug("not(self.Root.retVal() is None)")
            mistakes+=1
        if(not(self.Current==self.Current)):
            logging.debug("not(self.Current==self.Current)")
            mistakes+=1
        if (len(self.Elements)!=0):
            logging.debug("len(self.Elements)!=0")
            mistakes+=1
        if(self.buf!=""):
            logging.debug("self.buf!=""")
            mistakes+=1
        
        self.addNode(self.Root,5)
        self.Current==self.Root
        self.inorder(self.Current)
        if(self.buf!='5 '):
            logging.debug("self.buf!='5 '")
            mistakes+=1

        self.addNode(self.Current,3,0)
        if(self.Current.retLson().retVal()!=3):
            logging.debug("self.Current.retLson().retVal()!=3")
            mistakes+=1
        self.buf=''
        self.inorder(self.Current)
        if(self.buf!='3 5 '):
            logging.debug("self.buf!='3 5 '")
            mistakes+=1


        self.addNode(self.Current,7,1)
        if(self.Current.retRson().retVal()!=7):
            logging.debug("self.Current.retRson().retVal()!=7")
            mistakes+=1
        self.buf=''
        self.inorder(self.Current)
        if(self.buf!='3 5 7 '):
            logging.debug("self.buf!='3 5 7 '")
            mistakes+=1

        self.makeSubtreeTable()
        if(self.Elements==self.buf.split(' ')):
            logging.debug("self.Elements==self.buf.split(' ')")
            mistakes+=1
        
        if(self.Elements!=[3,5,7]):
            logging.debug("self.Elements!=[3,5,7]")
            mistakes+=1

        self.Current=self.Root.retLson()
        self.addNode(self.Current,2,0)
        self.addNode(self.Current,5,1)
        self.Current=self.Root.retRson()
        self.addNode(self.Current,1,0)
        self.addNode(self.Current,0,1)
        self.Current=self.Current.retRson()
        
        if(self.currentInfo()!="Current node: 0 "):
            logging.debug("""self.currentInfo()!="Current node: 0""")
            mistakes+=1

        self.addNode(self.Current,2,0)
        self.addNode(self.Current,8,1)
        self.Current=self.Current.retRson()
        self.addNode(self.Current,5,1)
        self.Current=self.Root

        self.buf=''
        self.inorder(self.Current)
        
        if('2 3 5 5 1 7 2 0 8 5 '!=self.buf):
            logging.debug("'2 3 5 5 1 7 2 0 8 5 '!=self.buf")
            mistakes+=1
        
        self.Elements.clear()
        self.makeSubtreeTable()
        if(self.Elements!=[0,1,2,2,3,5,5,5,7,8]):
            logging.debug("self.Elements!=[0,1,2,2,3,5,5,5,7,8]")
            mistakes+=1
        
        self.searchForNode(test=8)

        if(self.Current.retVal()!=8):
            logging.debug("self.Current.retVal()!=8")
            mistakes+=1
        if(self.Current.retRson().retVal()!=5):
            logging.debug("self.Current.retRson().retVal()!=5")
            mistakes+=1

        if(not(self.Current.retLson() is None)):
            logging.debug("not(self.Current.retLson() is None)")
            mistakes+=1

        self.Current=self.Root
        self.Elements.clear()
        self.makeSubtreeTable()
        if(38!=(self.Calculations.sum(self.Elements))):
            logging.debug("38!=(self.Calculations.sum(self.Elements))")
            mistakes+=1
        if(4.0!=(self.Calculations.median(self.Elements))):
            logging.debug("4.0!=(self.Calculations.median(self.Elements))")
            mistakes+=1
        if(3.8!=(self.Calculations.average(self.Elements))):
            logging.debug("3.8!=(self.Calculations.average(self.Elements))")
            mistakes+=1
        
        if(self.currentInfo()!="Current node: 5 L:3 R:7"):
            logging.debug("""self.currentInfo()!="Current node: 5 L:3 R:7""")
            mistakes+=1

        self.Current=self.Root
        self.searchForNode(test=-1)
        if(self.currentInfo()!='Current node: 5 L:3 R:7'):
            logging.debug("self.currentInfo()!='Current node: 5 L:3 R:7'")
            mistakes+=1

        self.Root=Node()
        self.Current=self.Root
        self.buf=''
        self.Elements.clear()
        self.inorder(self.Current)

        self.start(test=4, param=1)
        if(self.currentInfo()!="Current node: None "):
            logging.debug("""self.currentInfo()!="Current node: None """)
            mistakes+=1

        self.start(test=3)
        if(self.buf!=""):
            logging.debug("self.buf!=""")
            mistakes+=1

        if(0!=self.start(test=7)):
            logging.debug("0!=self.start(test=7)")
            mistakes+=1

        self.buf='a'
        self.start(test=3)
        if(self.buf!=''):
            logging.debug("self.buf!=""")
            mistakes+=1
        
        self.start(test=1)
        self.start(test=3)
        if(self.buf!="2 3 5 5 1 7 2 0 8 5 "):
            logging.debug("""self.buf!="2 3 5 5 1 7 2 0 8 5 """)
            mistakes+=1

        self.start(test=4,param=7)
        if(self.currentInfo()!="Current node: 7 L:1 R:0"):
            logging.debug("""self.currentInfo()!="Current node: 7 L:1 R:0""")
            mistakes+=1

        self.start(test=4, param=11)
        
        if(self.currentInfo()!="Current node: 7 L:1 R:0"):
            logging.debug("""self.currentInfo()!="Current node: 7 L:1 R:0""")
            mistakes+=1

        if(self.start(test=5)!=self.currentInfo()):
            logging.debug("self.start(test=5)!=self.currentInfo()")
            mistakes+=1

       
        if(self.start(test=7)!='sum: 23median: 3.5average: 3.8333333333333335'):
            mistakes+=1

        if(self.Elements!=[]):
            logging.debug("self.Elements!=[]")
            mistakes+=1
        
        if(mistakes==0):
            print("test for: interface has been passed")
            logging.debug("passed")
            return 1
        else:
            print("Unit test for interface: failed")
            print("mistakes: "+str(mistakes))
            logging.debug("mistakes: "+(str)(mistakes))
            return 0
        

        
        
        
    

        

obiekt=TaskOne()

#obiekt.unitTest()
obiekt.start()