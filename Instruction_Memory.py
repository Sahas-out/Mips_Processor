import fileinput
from IntToBinConvertor import IntToBin
class Instruction_Memory:
    def __init__(self):
        self.instruction = IntToBin(0) 
        self.ins_mem = []

    # store instructions import file
    def store_instructions(self):
        for line in fileinput.input(files="machinecode.txt"):
            if(line=='\n'):
                 break
            else:
                self.ins_mem.append(line)

    def fetch_instruction(self,Pc):
        self.instruction = self.ins_mem[int(Pc,2)-4194304]

    