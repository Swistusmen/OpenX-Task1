import logging
logging.basicConfig(filename="dane.txt",level=logging.DEBUG)


class Node:
    
    def __init__(self, a=None):
        if((type(a)!=int)and(not(a is None))):
            raise Exception("Wrong data type")
        self.val=a
        self.Rson=None
        self.Lson=None

    def retVal(self):
        return self.val

    def retRson(self):
        return self.Rson

    def retLson(self):
        return self.Lson

    def setVal(self, a):
        if( type(a) == int):
            self.val=a
        else:
            raise Exception ("Zły typ wartosci")

    def setLson(self, a):
        if( type(a) == int):
            self.Lson=Node(a)
        else:
            raise Exception ("Zły typ wartosci")
        

    def setRson(self, a):
        if( type(a) == int):
            self.Rson=Node(a)
        else:
            raise Exception ("Zły typ wartosci")

def UnitTest():
    logging.debug("Node")
    mistakes=0
    a=Node()
    if(not(a.retRson()is None)):
        logging.debug("not(a.retRson()is None)")
        mistakes+=1
    if(not(a.retLson()is None)):
        logging.debug("not(a.retLson()is None)")
        mistakes+=1
    if(a.retVal()!=None):
        logging.debug("a.retVal()!=None")
        mistakes+=1
    val=4
    a.setVal(4)
    if(a.retVal()!=val):
        mistakes+=1
    val=None

    try:
        try:
            a.setVal(val)
        finally:
            mistakes+=1
    except Exception as err:
        mistakes-=1
    
    try:
        mistakes+=1
        val=Node('b')
    except Exception as err:
        mistakes-=1

    try:
        try:
            a.setVal(val)
        finally:
            mistakes+=1
    except Exception as err:
        mistakes-=1

    val=5
    try:
        a.setLson(val)
    except Exception as err:
        mistakes+=1

    if(val!=a.retLson().retVal()):
        logging.debug("val!=a.retLson().retVal()")
        mistakes+=1

    try:
        a.setRson(val)
    except Exception as err:
        mistakes+=1

    if(val!=a.retRson().retVal()):
        logging.debug("val!=a.retRson().retVal()")
        mistakes+=1

    if(mistakes!=0):
            print("Unit test for node: failed")
            print("mistakes: "+str(mistakes)+"/11")
            logging.debug("if there is no communicate about mistakes it means they are in try.. catch")
            logging.debug("mistakes: "+(str)(mistakes))
            return 0
    else:
            print("test for: node has been passed!")
            logging.debug("passed")
            return 1
    
#UnitTest()
    
    
        



