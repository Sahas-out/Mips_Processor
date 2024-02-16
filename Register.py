from IntToBinConvertor import IntToBin
class Register:
    def __init__(self):
        self.Readdata1 = IntToBin(0)
        self.ReadData2 = IntToBin(0)
        self.reg_file = [IntToBin(0) for i in range (32)]
        self.write_reg = "00000"
    


    def read_data(self,Instruction_25_21,Instruction_20_16,Instruction_15_11,RegDst):
        self.Readdata1 = self.reg_file[int(Instruction_25_21,2)]
        self.Readdata2 = self.reg_file[int(Instruction_20_16,2)]
        if(RegDst):
            self.write_reg = Instruction_15_11
        else:
            self.write_reg = Instruction_20_16
    
    def write_data(self,RegWrite,Writedata):
        if(RegWrite):
            self.reg_file [int(self.write_reg,2)] = Writedata
        else:
            pass
    
