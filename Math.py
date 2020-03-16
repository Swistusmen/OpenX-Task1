from Node import Node
import random
import logging
logging.basicConfig(filename='dane.txt',filemode=logging.DEBUG)

class Math:
    def __init__(self):
        pass

    def sum(self, elements):
        if(len(elements)==0):
            raise Exception("There is no elements to operate on")
        sum=0
        for i in elements:
            if(type(i)!=int):
                raise Exception("Wrong type of data")
            sum+=i
        #print("sum: "+(str)(sum))
        return sum

    def average(self, elements):
        size=len(elements)
        if(size==0):
            raise Exception("There is no elements to operate on")
        sum=0
        for i in elements:
            if(type(i)!=int):
                raise Exception("Wrong type of data")
            sum+=i
        average=float(sum)/float(size)
        #print("average: "+(str)(average))
        return average
            
        

    def median(self,elements):
        size=len(elements)
        med=float(0)
        if(size==0):
            raise Exception("There is no elements to operate on")
        if(size%2==1):
            med=elements[(int)((size-1)/2)]
        else:
            med=(float)((elements[(int)(size/2)]+elements[(int)((size-1)/2)])/2)
        #print("median: "+(str)(med))
        return med

    def unitTest(self):
        
        logging.debug("Math")
        mistakes=0
        lista=[1,2,3,4,5,6,7,8,9]
        try:
            if(self.average(lista)!=5.0):
                logging.debug("self.average(lista)!=5.0")
                mistakes+=1
        except Exception as err:
            print(err)
        try:
            if(self.median(lista)!=5):
                logging.debug("self.median(lista)!=5")
                mistakes+=1
        except Exception as err:
            print(err)
        try:
            if(45!=self.sum(lista)):
                logging.debug("45!=self.sum(lista)")
                mistakes+=1
        except Exception as err:
            print(err)
        lista.append(10)
        try:
            if(self.average(lista)!=5.5):
                logging.debug("self.average(lista)!=5.5")
                mistakes+=1
        except Exception as err:
            print(err)
        try:
            if(self.median(lista)!=5.5):
                logging.debug("self.median(lista)!=5.5")
                mistakes+=1
        except Exception as err:
            print(err)
        try:
            if(self.sum(lista)!=55):
                logging.debug("self.sum(lista)!=55")
                mistakes+=1
        except Exception as err:
            print(err)
        lista.clear()
        lista=[-1,-2,-3,-4,-5,6,7,8,10]
        try:
            if(self.average(lista)!=1.7777777777777777):
                logging.debug("self.average(lista)!=1.7777777777777777")
                mistakes+=1
        except Exception as err:
            print(err)
        try:
            if(self.median(lista)!=-5):
                logging.debug("self.median(lista)!=-5")
                mistakes+=1
        except Exception as err:
            print(err)
        try:
            if(self.sum(lista)!=16):
                logging.debug("self.sum(lista)!=16")
                mistakes+=1
        except Exception as err:
            print(err)
        lista.clear()
        lista=[1.22]
        try:
            try:
                self.sum(lista)
            finally:
                mistakes+=1
        except Exception as err:
            mistakes-=1
        lista.clear()
        lista.append('a')
        try:
            try:
                self.sum(lista)
            finally:
                mistakes+=1
        except Exception as err:
            mistakes-=1
        if(mistakes!=0):
            print("Unit test for math: failed")
            print("mistakes: "+str(mistakes)+"/11")
            logging.debug("mistakes: "+(str)(mistakes))
            logging.debug("If there is no comunicates, it means bugs are in try... finally")
            return 0
        else:
            print("test for: math has been passed!")
            logging.debug("passed")
            return 1


#o=Math()
#o.unitTest()
            

