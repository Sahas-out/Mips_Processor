
import fileinput
for line in fileinput.input(files="machinecode.txt"):
    if(line=='\n'):
        break
    else:
        print(f"opcode {line[0:6]} function {line[26:32]}")
