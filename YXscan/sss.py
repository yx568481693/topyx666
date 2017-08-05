class Test():
    def __init__(self):
        self.__num = 100

    def SetNum(self, newNum):
        self.__num = newNum

    def getNum(self):
        return self.__num

t = Test()
#print(t.__num)
#t.__num = 200
print t.getNum()
t.SetNum(200)
print t.getNum() 
