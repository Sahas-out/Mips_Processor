from IntToBinConvertor import IntToBin
class ALUcontrol:
    def __init__(self):
        self.ALUcontrol = "0000" # storing Alu control input 
    def Generate_ALU_control(self,ALUOp,Instruction_5_0):
        function_map={
            "100000" : "0010", #add operation
            "100010" : "0110", #substract opertion
            "100100" : "0000", #and operation
            "000010" : "1111", # mul operation
            "101010" : "0111", #set on less than
            "100101" : "0001", # or opertion
            "100110" : "1110", # xor operation
            "011011" : "1010", # divide operation 
        }
        ALUcontrol_map = {
            "10" : function_map[Instruction_5_0], # R format 
            "01" : "0110", #substract on beq and j
            "00" : "0010", # add operation on load, store and addi
            "11" : "0000", # and operation on andi
        }        
        self.ALUcontrol = ALUcontrol_map[ALUOp]
