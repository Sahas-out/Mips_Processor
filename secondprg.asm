.data
n: .word 15            # Change this value to find nth Fibonacci term
result: .word 0


.text

main:
    
    lw $t0, 0($s0)              # Load value of n into $t0
    addi $t1, $zero,2           # Initialize counter i = 2
    addi $t2, $zero,0           # Initialize first Fibonacci number F0 = 0
    addi $t3, $zero,1           # Initialize second Fibonacci number F1 = 1
    
loop:
    beq $t1, $t0, exit  # If i == n, exit loop
    add $t4, $t2, $t3    # F(i) = F(i-1) + F(i-2)
    addi $t2, $t3 ,0      # Update F(i-2) = F(i-1)
    addi $t3, $t4 ,0      # Update F(i-1) = F(i)
    addi $t1, $t1, 1     # Increment counter i
    j loop               # Jump back to loop
    
exit:
    sw  $t3,4($s0)	
     
    #print the result 
    	#lw $a0,4($s0)
	#li $v0,1
	#syscall
