from IntToBinConvertor import IntToBin
class PC:

    def __init__(self):
        self.counter = IntToBin(0)
    def increment(self,Branch,Zero,SignImm,Jump,Instruction_0_25):
        self.counter = IntToBin(int(self.counter,2)+4) # doing PC + 4
        Instruction_0_25 = Instruction_0_25[2:] + "00" #left shift by 2
        Instruction_0_25 = self.counter[28:32] + Instruction_0_25 # adding 4 MSB from PC + 4
        SignImm = SignImm[2:] + "00" #left shift by 2
        if(int(Branch,2) and int(Zero,2)): # implementaion of Mux with PcSrc as select line
            self.counter = IntToBin( int(self.counter) + int(SignImm,2) ) # doing PC+4 +imm*4
        else:
            self.counter = self.counter
        if(int(Jump,2)): # implemenation of Mux with Jump as select line
            self.counter = Instruction_0_25 # assinging Pc to Jump address after concatenation
        else:
            self.counter = self.counter
        

