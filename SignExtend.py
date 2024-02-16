from IntToBinConvertor import IntToBin
class Sign_Extend:
    def __init__ (self):
        self.SignImm = IntToBin(0) # SignImm variable stores the SignImm value
    def extend(self,Instruction_15_0):
        self.SignImm = ("0"*16) + Instruction_15_0
     