.data
size:  .word 9
result: .word 0
sampleinput: .word 20
array: .word 1,6,5,3,2,199,21,23,1
# we need to store 0x10010000 into s0 first
.text
main:
lw $t0, 0($s0) # loading n into t0
addi $s1, $s0, 12 # loading the address of start of array into s1
addi $t1, $zero, 0 # intializing index variable
lw $t2, 8($s0)  # loading sample into t2
loop:
beq $t0, $t1, exit
lw $t4, 0($s1)
beq $t4, $t2, exit
addi $t1, $t1, 1
addi $s1, $s1, 4
j loop
exit:
sw $t1, 4($s0)
#print the result
#lw $a0,4($s0)
#li $v0,1
#syscall

