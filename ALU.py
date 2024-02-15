
from IntToBinConvertor import IntToBin
class ALU:
    def __init__(self):
        self.zero = '0'
        self.AluResult = IntToBin(0)
    def AluCalculate(self,ALUcontrol,input_1,input_2):
        
        if(ALUcontrol == "0010"): #add
            self.AluResult = IntToBin( int(input_1) + int(input_2) ) 
        elif(ALUcontrol == "0110"): #subtract
            self.AluResult = IntToBin( int(input_1) - int(input_2) ) 
        elif(ALUcontrol == "1111"): #mul
            self.AluResult = IntToBin( int(input_1) * int(input_2) )
        elif(ALUcontrol == "0000"): #bitwise and
            self.AluResult = IntToBin( int(input_1) & int(input_2) )
        elif(ALUcontrol == "0001"): #bitwise or
            self.AluResult = IntToBin( int(input_1) | int(input_2) )  
        elif(ALUcontrol == "1110"): #bitwise xor
            self.AluResult = IntToBin( int(input_1) ^ int(input_2) )    
        elif(ALUcontrol == "1010"):# floor division
            self.AluResult = IntToBin( int(input_1) / int(input_2) ) 
        elif(ALUcontrol == "0111"):# set on less than
            if(input_1 < input_2):
                self.AluResult = IntToBin(1)
            else:
                self.AluResult = IntToBin(0)
        else:
            print("Exception ALUcontrol doesnt match wuth any ")
        if(self.AluResult == 0): # checking if the result is zero
            self.zero = '1'
        else:
            self.zero = '0'
    