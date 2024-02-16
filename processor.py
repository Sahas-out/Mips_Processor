class Instruction_Memory:
    def __init__(self,PC):
        self.PC=""
        


    def Processor(self,opcode,rs,rt,rd,jump,shamt,ff,imm):
        self.opcode=self.PC[0:6]
        if(self.opcode=="000000"): #Rformat
            self.rs=self.PC[6:11]
            self.rt=self.PC[11:16]
            self.rd=self.PC[16:21]
            self.shamt=self.PC[21:26]
            self.ff=self.PC[26:]
        elif(self.opcode==""): #Iformat
            self.rs=self.PC[6:11]
            self.rt=self.PC[11:16]
            self.imm=self.PC[16:]

        else:             #jump
            self.jump=self.PC[6:] 


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

    def do_task(self):
        
