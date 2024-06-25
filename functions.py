# Library autor: Nicolás Santísima Trinidad Santín
# Created: 16/06/2024
# Python 3
# Using: Visual Studio Code by Microsoft
# All rights reserved
class array:
    identification = 0
    true_false = False
    actualArray = None
    def __getInfoLocalArray__(Array):
        return len(Array)
    def delete(number, Array):
        del Array[number]
    def show(Array):
        for i in range(0,len(Array)):
            print(Array[i])
    def search(Array,searching):
        for i in range(0,len(Array)):
            if (Array[i] == searching):
                array.true_false = True
                break
            else:
                array.true_false = False
        return array.true_false
    def getIdentification(Array, Object):
        for i in range(0,len(Array)):
            if (Array[i] == Object):
                array.true_false = True
                array.identification = i
                break
            else:
                array.true_false = False
        if (array.true_false == True):
            return array.identification
        else:
            return None
