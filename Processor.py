import fileinput
def IntToBin(integer):                                                #function to convert int to bin
    return bin(integer)[2:].rjust(32,'0')

class Instruction_Memory:                                                   #INSTRUCTION MEMORY
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

class Register:                                                            #REGISTERS
    def __init__(self):
        self.Readdata1 = IntToBin(0)
        self.Readdata2 = IntToBin(0)
        self.reg_file = [IntToBin(0) for i in range (32)]
        self.write_reg = "00000"
    


    def read_data(self,Instruction_25_21,Instruction_20_16,Instruction_15_11,RegDst):
        self.Readdata1 = self.reg_file[int(Instruction_25_21,2)]
        self.Readdata2 = self.reg_file[int(Instruction_20_16,2)]
        if(RegDst):
            self.write_reg = Instruction_15_11
        else:
            self.write_reg = Instruction_20_16
    
    def write_data(self,RegWrite,Readdata,MemtoReg,ALUresult):
        if(MemtoReg): # Mux with MemtoReg as select line
            Writedata = Readdata
        else:
            Writedata = ALUresult
        if(RegWrite):
            self.reg_file [int(self.write_reg,2)] = Writedata
        else:
            pass

class Sign_Extend:                                                      #SIGN_EXTEND                      
    def __init__ (self):
        self.SignImm = IntToBin(0) # SignImm variable stores the SignImm value
    def extend(self,Instruction_15_0):
        self.SignImm = ("0"*16) + Instruction_15_0 #extending to 32 bits

class ControlUnit:                                                      #CONTROL UNIT
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

class ALU:                                                               #ALU 
    def __init__(self):
        self.zero = '0'
        self.AluResult = IntToBin(0)
    def AluCalculate(self,ALUcontrol,ReadData_1,ReadData_2,ALUSrc,SignImm):
        input_1 = ReadData_1
        if(ALUSrc): # Mux with ALUSrc as select line
            input_2 = SignImm
        else:
            input_2 = ReadData_2
        
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

class ALUcontrol:                                                      #ALUcontrol
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

class PC:                                                             #PC

    def __init__(self):
        self.counter = IntToBin(4194304)
    def change(self,Branch,Zero,SignImm,Jump,Instruction_0_25):
        self.counter = IntToBin(int(self.counter,2)+4) # doing PC + 4
        Instruction_0_25 = Instruction_0_25 + "00" #left shift by 2
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

class Data_Memory:                                                 #DATA MEMORY 
    def __init__(self):
        
        self.readData = IntToBin(0)
        self.Data_memory =   [IntToBin(0) for i in range(32)]

    def read_Or_write(self,MemWrite,MemRead,Address,Writedata):
        if(MemRead):
            self.readData = self.Data_memory[Address]
        elif(MemWrite):
            self.Data_memory[Address] =  Writedata 
        else:
            pass
    
    def change_data(self):
        #example self.DataMemory[16] = IntToBin(9) to store the value 9 at address 26
        pass

instruction_memory = Instruction_Memory()     # creating objects for different components in MIPS
registers = Register()  
control_unit = ControlUnit()
alu = ALU()
alu_control = ALUcontrol()
pc = PC()
data_memory = Data_Memory()
sign_extend = Sign_Extend()

instruction_memory.store_instructions()        # storing instructions from "machinecode.txt"
last_step_no = len(instruction_memory.ins_mem) # finding out how many instructions are to be executed

for step in range(last_step_no):

    instruction_memory.fetch_instruction(pc.counter)                                                                          # this opeartion fetches the instruction at current pc value
    instruction = instruction_memory.instruction 
    control_unit.GenerateControlSignals(instruction[:6])                                                                      # first 6 bits goes to control unit and control signals are genrated
    alu_control.Generate_ALU_control(control_unit.ALUOp,instruction[26:32])                                                   # alu input signals are generated 
    registers.read_data(instruction[6:11],instruction[11:16],instruction[16:21],control_unit.RegDst)                          # decode stage execution
    sign_extend.extend(instruction[16:32])                                                                                    # it extends the last 16 bits of instruction to 32 bits by adding 0's
    alu.AluCalculate(alu_control.ALUcontrol,registers.Readdata1,registers.Readdata2,control_unit.ALUSrc,sign_extend.SignImm)  # alu computes the value  desired
    data_memory.read_Or_write(control_unit.MemWrite,control_unit.MemRead,alu.AluResult,registers.Readdata2)                   # writting or reading from memory
    registers.write_data(control_unit.RegWrite,data_memory.readData,control_unit.MemToReg,alu.AluResult)                      # writing back to reg if had to
    pc.change(control_unit.Branch,alu.zero,sign_extend.SignImm,control_unit.jump,instruction[6:32])                           # changing PC as per instruction
    
    






     
