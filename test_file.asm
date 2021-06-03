.LFB11:
	.cfi_startproc
	leal	-2(%rsi), %eax
	testl	%esi, %esi
	jle	.L5
	cltq
	addq	%rdi, %rax
	movzbl	(%rax), %edx
	cmpb	%dl, (%rdi)
	jne	.L7
	subl	$1, %esi
	addq	%rdi, %rsi
	jnp	.L3
	.p2align 4,,10
	.p2align 3
.L4:
	movzbl	1(%rdi), %ecx
	movzbl	-1(%rax), %edx
	addq	$1, %rdi
	subq	$1, %rax
	cmpb	%dl, %cl
	jne	.L7
.L3:
    movzbl	1(%rdi), %ecx
	movzbl	-1(%rax), %edx