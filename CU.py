from IntToBinConvertor import IntToBin
class ControlUnit:
    def __init__(self):
        # below are all the conrol signals that are generated during instrcuction execution
        self.RegDst   = '0' 
        self.Branch   = '0'
        self.MemRead  = '0'
        self.MemToReg = '0'
        self.MemWrite = '0'
        self.ALUSrc   = '0'
        self.RegWrite = '0'
        self.jump     = '0'
        self.ALUOp    = '00'
    def GenerateControlSignals(self,Instructions_26_31):
        # format is like s[0]=RegWrite s[1:3]=ALUOp s[3]=AluSrc and so on
        Signals_map = {
            "000000" : "1-10-0-0-0-0-0-1-0", #R-Format instructions
            "011100" : "1-10-0-0-0-0-0-1-0", #mul-instruction
            "001000" : "1-00-1-0-0-0-0-0-0", #addi-instruction
            "100011" : "1-00-1-0-1-1-0-0-0", #load instruction
            "101011" : "0-00-1-1-0-0-0-1-0", #store instruction
            "000100" : "0-01-0-0-0-0-1-0-0", #branch on equal instruction
            "000010" : "0-01-0-0-0-0-0-0-1", #jump instruction
            "001100" : "1-11-1-0-0-0-0-0-0"  #addi instruction
        }
        s=Signals_map[Instructions_26_31].split('-')
        #Each character of binary string correspond some control signal
        self.RegWrite = s[0]
        self.ALUOp    = s[1]
        self.AluSrc   = s[2]
        self.MemWrite = s[3]
        self.MemToReg = s[4]
        self.MemRead  = s[5]
        self.Branch   = s[6]
        self.RegDst   = s[7]
        self.jump     = s[8]

        