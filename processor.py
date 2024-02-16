class Instruction_Memory:
    def __init__(self,PC):
        self.PC=""
        


    def Processor(self):
        return 


class Register:
    def __init__(self,readReg1,readReg2,writeReg,writeData,readData1,readData2):
        self.readReg1=""
        self.readReg2=""
        self.writeReg=""
        self.writeData=""
        self.readData=""
        self.readData2=""

    def sign_extend(self,i):
        x="0000"
        self.i=4*x*self.i
        return self.i

class Data_Memory:
    def __init__(self,address,readData,writeData):
        self.address=""
        self.readData=""
        self.writeData=""