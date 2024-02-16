from IntToBinConvertor import IntToBin

class Data_Memory:
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
