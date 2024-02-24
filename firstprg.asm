.data
n: .word 5 # change the value of n here to get desired factorial
#store value 0x10010000 at s0 register
result: .word 1 # intializing result with 1
.text
	lw $t0,0($s0) 	        # loading n into t0 from address stored in s0
	addi $t1,$zero,1	# intializing t1 =1
	addi $t2,$zero,1	# intializing result variable with 1
	code:
	beq $t0,$t1,exitloop   # while n!=1
	mul $t2,$t2,$t0	       # t2 = t2*n
	sub $t0,$t0,$t1        # n=n-1
	j code
	exitloop:
	sw $t2,4($s0) 	# storing the result into memeory
	
	
	
	#Print the result
	#lw $a0,4($s0)
	#li $v0,1
	#syscall
	 
