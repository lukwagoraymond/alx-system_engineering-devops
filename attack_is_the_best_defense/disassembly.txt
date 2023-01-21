
user_authenticating_into_server:     file format elf64-x86-64


Disassembly of section .init:

00000000004009c0 <.init>:
  4009c0:	48 83 ec 08          	sub    rsp,0x8
  4009c4:	48 8b 05 2d 16 20 00 	mov    rax,QWORD PTR [rip+0x20162d]        # 601ff8 <strerror@plt+0x201498>
  4009cb:	48 85 c0             	test   rax,rax
  4009ce:	74 05                	je     4009d5 <getenv@plt-0x1b>
  4009d0:	e8 db 00 00 00       	call   400ab0 <__gmon_start__@plt>
  4009d5:	48 83 c4 08          	add    rsp,0x8
  4009d9:	c3                   	ret    

Disassembly of section .plt:

00000000004009e0 <getenv@plt-0x10>:
  4009e0:	ff 35 22 16 20 00    	push   QWORD PTR [rip+0x201622]        # 602008 <strerror@plt+0x2014a8>
  4009e6:	ff 25 24 16 20 00    	jmp    QWORD PTR [rip+0x201624]        # 602010 <strerror@plt+0x2014b0>
  4009ec:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]

00000000004009f0 <getenv@plt>:
  4009f0:	ff 25 22 16 20 00    	jmp    QWORD PTR [rip+0x201622]        # 602018 <strerror@plt+0x2014b8>
  4009f6:	68 00 00 00 00       	push   0x0
  4009fb:	e9 e0 ff ff ff       	jmp    4009e0 <getenv@plt-0x10>

0000000000400a00 <__errno_location@plt>:
  400a00:	ff 25 1a 16 20 00    	jmp    QWORD PTR [rip+0x20161a]        # 602020 <strerror@plt+0x2014c0>
  400a06:	68 01 00 00 00       	push   0x1
  400a0b:	e9 d0 ff ff ff       	jmp    4009e0 <getenv@plt-0x10>

0000000000400a10 <getpid@plt>:
  400a10:	ff 25 12 16 20 00    	jmp    QWORD PTR [rip+0x201612]        # 602028 <strerror@plt+0x2014c8>
  400a16:	68 02 00 00 00       	push   0x2
  400a1b:	e9 c0 ff ff ff       	jmp    4009e0 <getenv@plt-0x10>

0000000000400a20 <strlen@plt>:
  400a20:	ff 25 0a 16 20 00    	jmp    QWORD PTR [rip+0x20160a]        # 602030 <strerror@plt+0x2014d0>
  400a26:	68 03 00 00 00       	push   0x3
  400a2b:	e9 b0 ff ff ff       	jmp    4009e0 <getenv@plt-0x10>

0000000000400a30 <__stack_chk_fail@plt>:
  400a30:	ff 25 02 16 20 00    	jmp    QWORD PTR [rip+0x201602]        # 602038 <strerror@plt+0x2014d8>
  400a36:	68 04 00 00 00       	push   0x4
  400a3b:	e9 a0 ff ff ff       	jmp    4009e0 <getenv@plt-0x10>

0000000000400a40 <memset@plt>:
  400a40:	ff 25 fa 15 20 00    	jmp    QWORD PTR [rip+0x2015fa]        # 602040 <strerror@plt+0x2014e0>
  400a46:	68 05 00 00 00       	push   0x5
  400a4b:	e9 90 ff ff ff       	jmp    4009e0 <getenv@plt-0x10>

0000000000400a50 <__libc_start_main@plt>:
  400a50:	ff 25 f2 15 20 00    	jmp    QWORD PTR [rip+0x2015f2]        # 602048 <strerror@plt+0x2014e8>
  400a56:	68 06 00 00 00       	push   0x6
  400a5b:	e9 80 ff ff ff       	jmp    4009e0 <getenv@plt-0x10>

0000000000400a60 <memcmp@plt>:
  400a60:	ff 25 ea 15 20 00    	jmp    QWORD PTR [rip+0x2015ea]        # 602050 <strerror@plt+0x2014f0>
  400a66:	68 07 00 00 00       	push   0x7
  400a6b:	e9 70 ff ff ff       	jmp    4009e0 <getenv@plt-0x10>

0000000000400a70 <calloc@plt>:
  400a70:	ff 25 e2 15 20 00    	jmp    QWORD PTR [rip+0x2015e2]        # 602058 <strerror@plt+0x2014f8>
  400a76:	68 08 00 00 00       	push   0x8
  400a7b:	e9 60 ff ff ff       	jmp    4009e0 <getenv@plt-0x10>

0000000000400a80 <putenv@plt>:
  400a80:	ff 25 da 15 20 00    	jmp    QWORD PTR [rip+0x2015da]        # 602060 <strerror@plt+0x201500>
  400a86:	68 09 00 00 00       	push   0x9
  400a8b:	e9 50 ff ff ff       	jmp    4009e0 <getenv@plt-0x10>

0000000000400a90 <atoll@plt>:
  400a90:	ff 25 d2 15 20 00    	jmp    QWORD PTR [rip+0x2015d2]        # 602068 <strerror@plt+0x201508>
  400a96:	68 0a 00 00 00       	push   0xa
  400a9b:	e9 40 ff ff ff       	jmp    4009e0 <getenv@plt-0x10>

0000000000400aa0 <fprintf@plt>:
  400aa0:	ff 25 ca 15 20 00    	jmp    QWORD PTR [rip+0x2015ca]        # 602070 <strerror@plt+0x201510>
  400aa6:	68 0b 00 00 00       	push   0xb
  400aab:	e9 30 ff ff ff       	jmp    4009e0 <getenv@plt-0x10>

0000000000400ab0 <__gmon_start__@plt>:
  400ab0:	ff 25 c2 15 20 00    	jmp    QWORD PTR [rip+0x2015c2]        # 602078 <strerror@plt+0x201518>
  400ab6:	68 0c 00 00 00       	push   0xc
  400abb:	e9 20 ff ff ff       	jmp    4009e0 <getenv@plt-0x10>

0000000000400ac0 <memcpy@plt>:
  400ac0:	ff 25 ba 15 20 00    	jmp    QWORD PTR [rip+0x2015ba]        # 602080 <strerror@plt+0x201520>
  400ac6:	68 0d 00 00 00       	push   0xd
  400acb:	e9 10 ff ff ff       	jmp    4009e0 <getenv@plt-0x10>

0000000000400ad0 <time@plt>:
  400ad0:	ff 25 b2 15 20 00    	jmp    QWORD PTR [rip+0x2015b2]        # 602088 <strerror@plt+0x201528>
  400ad6:	68 0e 00 00 00       	push   0xe
  400adb:	e9 00 ff ff ff       	jmp    4009e0 <getenv@plt-0x10>

0000000000400ae0 <__xstat@plt>:
  400ae0:	ff 25 aa 15 20 00    	jmp    QWORD PTR [rip+0x2015aa]        # 602090 <strerror@plt+0x201530>
  400ae6:	68 0f 00 00 00       	push   0xf
  400aeb:	e9 f0 fe ff ff       	jmp    4009e0 <getenv@plt-0x10>

0000000000400af0 <malloc@plt>:
  400af0:	ff 25 a2 15 20 00    	jmp    QWORD PTR [rip+0x2015a2]        # 602098 <strerror@plt+0x201538>
  400af6:	68 10 00 00 00       	push   0x10
  400afb:	e9 e0 fe ff ff       	jmp    4009e0 <getenv@plt-0x10>

0000000000400b00 <__isoc99_sscanf@plt>:
  400b00:	ff 25 9a 15 20 00    	jmp    QWORD PTR [rip+0x20159a]        # 6020a0 <strerror@plt+0x201540>
  400b06:	68 11 00 00 00       	push   0x11
  400b0b:	e9 d0 fe ff ff       	jmp    4009e0 <getenv@plt-0x10>

0000000000400b10 <execvp@plt>:
  400b10:	ff 25 92 15 20 00    	jmp    QWORD PTR [rip+0x201592]        # 6020a8 <strerror@plt+0x201548>
  400b16:	68 12 00 00 00       	push   0x12
  400b1b:	e9 c0 fe ff ff       	jmp    4009e0 <getenv@plt-0x10>

0000000000400b20 <sprintf@plt>:
  400b20:	ff 25 8a 15 20 00    	jmp    QWORD PTR [rip+0x20158a]        # 6020b0 <strerror@plt+0x201550>
  400b26:	68 13 00 00 00       	push   0x13
  400b2b:	e9 b0 fe ff ff       	jmp    4009e0 <getenv@plt-0x10>

0000000000400b30 <exit@plt>:
  400b30:	ff 25 82 15 20 00    	jmp    QWORD PTR [rip+0x201582]        # 6020b8 <strerror@plt+0x201558>
  400b36:	68 14 00 00 00       	push   0x14
  400b3b:	e9 a0 fe ff ff       	jmp    4009e0 <getenv@plt-0x10>

0000000000400b40 <fwrite@plt>:
  400b40:	ff 25 7a 15 20 00    	jmp    QWORD PTR [rip+0x20157a]        # 6020c0 <strerror@plt+0x201560>
  400b46:	68 15 00 00 00       	push   0x15
  400b4b:	e9 90 fe ff ff       	jmp    4009e0 <getenv@plt-0x10>

0000000000400b50 <strdup@plt>:
  400b50:	ff 25 72 15 20 00    	jmp    QWORD PTR [rip+0x201572]        # 6020c8 <strerror@plt+0x201568>
  400b56:	68 16 00 00 00       	push   0x16
  400b5b:	e9 80 fe ff ff       	jmp    4009e0 <getenv@plt-0x10>

0000000000400b60 <strerror@plt>:
  400b60:	ff 25 6a 15 20 00    	jmp    QWORD PTR [rip+0x20156a]        # 6020d0 <strerror@plt+0x201570>
  400b66:	68 17 00 00 00       	push   0x17
  400b6b:	e9 70 fe ff ff       	jmp    4009e0 <getenv@plt-0x10>

Disassembly of section .text:

0000000000400b70 <.text>:
  400b70:	31 ed                	xor    ebp,ebp
  400b72:	49 89 d1             	mov    r9,rdx
  400b75:	5e                   	pop    rsi
  400b76:	48 89 e2             	mov    rdx,rsp
  400b79:	48 83 e4 f0          	and    rsp,0xfffffffffffffff0
  400b7d:	50                   	push   rax
  400b7e:	54                   	push   rsp
  400b7f:	49 c7 c0 00 17 40 00 	mov    r8,0x401700
  400b86:	48 c7 c1 90 16 40 00 	mov    rcx,0x401690
  400b8d:	48 c7 c7 d4 15 40 00 	mov    rdi,0x4015d4
  400b94:	e8 b7 fe ff ff       	call   400a50 <__libc_start_main@plt>
  400b99:	f4                   	hlt    
  400b9a:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]
  400ba0:	b8 27 24 60 00       	mov    eax,0x602427
  400ba5:	55                   	push   rbp
  400ba6:	48 2d 20 24 60 00    	sub    rax,0x602420
  400bac:	48 83 f8 0e          	cmp    rax,0xe
  400bb0:	48 89 e5             	mov    rbp,rsp
  400bb3:	77 02                	ja     400bb7 <strerror@plt+0x57>
  400bb5:	5d                   	pop    rbp
  400bb6:	c3                   	ret    
  400bb7:	b8 00 00 00 00       	mov    eax,0x0
  400bbc:	48 85 c0             	test   rax,rax
  400bbf:	74 f4                	je     400bb5 <strerror@plt+0x55>
  400bc1:	5d                   	pop    rbp
  400bc2:	bf 20 24 60 00       	mov    edi,0x602420
  400bc7:	ff e0                	jmp    rax
  400bc9:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
  400bd0:	b8 20 24 60 00       	mov    eax,0x602420
  400bd5:	55                   	push   rbp
  400bd6:	48 2d 20 24 60 00    	sub    rax,0x602420
  400bdc:	48 c1 f8 03          	sar    rax,0x3
  400be0:	48 89 e5             	mov    rbp,rsp
  400be3:	48 89 c2             	mov    rdx,rax
  400be6:	48 c1 ea 3f          	shr    rdx,0x3f
  400bea:	48 01 d0             	add    rax,rdx
  400bed:	48 d1 f8             	sar    rax,1
  400bf0:	75 02                	jne    400bf4 <strerror@plt+0x94>
  400bf2:	5d                   	pop    rbp
  400bf3:	c3                   	ret    
  400bf4:	ba 00 00 00 00       	mov    edx,0x0
  400bf9:	48 85 d2             	test   rdx,rdx
  400bfc:	74 f4                	je     400bf2 <strerror@plt+0x92>
  400bfe:	5d                   	pop    rbp
  400bff:	48 89 c6             	mov    rsi,rax
  400c02:	bf 20 24 60 00       	mov    edi,0x602420
  400c07:	ff e2                	jmp    rdx
  400c09:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
  400c10:	80 3d 19 18 20 00 00 	cmp    BYTE PTR [rip+0x201819],0x0        # 602430 <stderr@GLIBC_2.2.5+0x8>
  400c17:	75 11                	jne    400c2a <strerror@plt+0xca>
  400c19:	55                   	push   rbp
  400c1a:	48 89 e5             	mov    rbp,rsp
  400c1d:	e8 7e ff ff ff       	call   400ba0 <strerror@plt+0x40>
  400c22:	5d                   	pop    rbp
  400c23:	c6 05 06 18 20 00 01 	mov    BYTE PTR [rip+0x201806],0x1        # 602430 <stderr@GLIBC_2.2.5+0x8>
  400c2a:	f3 c3                	repz ret 
  400c2c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
  400c30:	48 83 3d e8 11 20 00 	cmp    QWORD PTR [rip+0x2011e8],0x0        # 601e20 <strerror@plt+0x2012c0>
  400c37:	00 
  400c38:	74 1e                	je     400c58 <strerror@plt+0xf8>
  400c3a:	b8 00 00 00 00       	mov    eax,0x0
  400c3f:	48 85 c0             	test   rax,rax
  400c42:	74 14                	je     400c58 <strerror@plt+0xf8>
  400c44:	55                   	push   rbp
  400c45:	bf 20 1e 60 00       	mov    edi,0x601e20
  400c4a:	48 89 e5             	mov    rbp,rsp
  400c4d:	ff d0                	call   rax
  400c4f:	5d                   	pop    rbp
  400c50:	e9 7b ff ff ff       	jmp    400bd0 <strerror@plt+0x70>
  400c55:	0f 1f 00             	nop    DWORD PTR [rax]
  400c58:	e9 73 ff ff ff       	jmp    400bd0 <strerror@plt+0x70>
  400c5d:	55                   	push   rbp
  400c5e:	48 89 e5             	mov    rbp,rsp
  400c61:	c6 05 da 18 20 00 00 	mov    BYTE PTR [rip+0x2018da],0x0        # 602542 <stderr@GLIBC_2.2.5+0x11a>
  400c68:	0f b6 05 d3 18 20 00 	movzx  eax,BYTE PTR [rip+0x2018d3]        # 602542 <stderr@GLIBC_2.2.5+0x11a>
  400c6f:	88 05 cc 18 20 00    	mov    BYTE PTR [rip+0x2018cc],al        # 602541 <stderr@GLIBC_2.2.5+0x119>
  400c75:	0f b6 05 c5 18 20 00 	movzx  eax,BYTE PTR [rip+0x2018c5]        # 602541 <stderr@GLIBC_2.2.5+0x119>
  400c7c:	88 05 be 18 20 00    	mov    BYTE PTR [rip+0x2018be],al        # 602540 <stderr@GLIBC_2.2.5+0x118>
  400c82:	0f b6 05 b7 18 20 00 	movzx  eax,BYTE PTR [rip+0x2018b7]        # 602540 <stderr@GLIBC_2.2.5+0x118>
  400c89:	0f b6 c0             	movzx  eax,al
  400c8c:	0f b6 15 ad 18 20 00 	movzx  edx,BYTE PTR [rip+0x2018ad]        # 602540 <stderr@GLIBC_2.2.5+0x118>
  400c93:	48 98                	cdqe   
  400c95:	88 90 40 24 60 00    	mov    BYTE PTR [rax+0x602440],dl
  400c9b:	0f b6 05 9e 18 20 00 	movzx  eax,BYTE PTR [rip+0x20189e]        # 602540 <stderr@GLIBC_2.2.5+0x118>
  400ca2:	83 c0 01             	add    eax,0x1
  400ca5:	88 05 95 18 20 00    	mov    BYTE PTR [rip+0x201895],al        # 602540 <stderr@GLIBC_2.2.5+0x118>
  400cab:	0f b6 05 8e 18 20 00 	movzx  eax,BYTE PTR [rip+0x20188e]        # 602540 <stderr@GLIBC_2.2.5+0x118>
  400cb2:	84 c0                	test   al,al
  400cb4:	75 cc                	jne    400c82 <strerror@plt+0x122>
  400cb6:	5d                   	pop    rbp
  400cb7:	c3                   	ret    
  400cb8:	55                   	push   rbp
  400cb9:	48 89 e5             	mov    rbp,rsp
  400cbc:	48 89 7d e8          	mov    QWORD PTR [rbp-0x18],rdi
  400cc0:	89 75 e4             	mov    DWORD PTR [rbp-0x1c],esi
  400cc3:	48 8b 45 e8          	mov    rax,QWORD PTR [rbp-0x18]
  400cc7:	48 89 45 f8          	mov    QWORD PTR [rbp-0x8],rax
  400ccb:	e9 bf 00 00 00       	jmp    400d8f <strerror@plt+0x22f>
  400cd0:	0f b6 05 69 18 20 00 	movzx  eax,BYTE PTR [rip+0x201869]        # 602540 <stderr@GLIBC_2.2.5+0x118>
  400cd7:	0f b6 c0             	movzx  eax,al
  400cda:	48 98                	cdqe   
  400cdc:	0f b6 80 40 24 60 00 	movzx  eax,BYTE PTR [rax+0x602440]
  400ce3:	88 45 f7             	mov    BYTE PTR [rbp-0x9],al
  400ce6:	0f b6 15 55 18 20 00 	movzx  edx,BYTE PTR [rip+0x201855]        # 602542 <stderr@GLIBC_2.2.5+0x11a>
  400ced:	0f b6 45 f7          	movzx  eax,BYTE PTR [rbp-0x9]
  400cf1:	01 d0                	add    eax,edx
  400cf3:	88 05 49 18 20 00    	mov    BYTE PTR [rip+0x201849],al        # 602542 <stderr@GLIBC_2.2.5+0x11a>
  400cf9:	0f b6 05 40 18 20 00 	movzx  eax,BYTE PTR [rip+0x201840]        # 602540 <stderr@GLIBC_2.2.5+0x118>
  400d00:	0f b6 c0             	movzx  eax,al
  400d03:	99                   	cdq    
  400d04:	f7 7d e4             	idiv   DWORD PTR [rbp-0x1c]
  400d07:	89 d0                	mov    eax,edx
  400d09:	48 63 d0             	movsxd rdx,eax
  400d0c:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
  400d10:	48 01 d0             	add    rax,rdx
  400d13:	0f b6 10             	movzx  edx,BYTE PTR [rax]
  400d16:	0f b6 05 25 18 20 00 	movzx  eax,BYTE PTR [rip+0x201825]        # 602542 <stderr@GLIBC_2.2.5+0x11a>
  400d1d:	01 d0                	add    eax,edx
  400d1f:	88 05 1d 18 20 00    	mov    BYTE PTR [rip+0x20181d],al        # 602542 <stderr@GLIBC_2.2.5+0x11a>
  400d25:	0f b6 05 14 18 20 00 	movzx  eax,BYTE PTR [rip+0x201814]        # 602540 <stderr@GLIBC_2.2.5+0x118>
  400d2c:	0f b6 c8             	movzx  ecx,al
  400d2f:	0f b6 05 0c 18 20 00 	movzx  eax,BYTE PTR [rip+0x20180c]        # 602542 <stderr@GLIBC_2.2.5+0x11a>
  400d36:	0f b6 c0             	movzx  eax,al
  400d39:	48 98                	cdqe   
  400d3b:	0f b6 90 40 24 60 00 	movzx  edx,BYTE PTR [rax+0x602440]
  400d42:	48 63 c1             	movsxd rax,ecx
  400d45:	88 90 40 24 60 00    	mov    BYTE PTR [rax+0x602440],dl
  400d4b:	0f b6 05 f0 17 20 00 	movzx  eax,BYTE PTR [rip+0x2017f0]        # 602542 <stderr@GLIBC_2.2.5+0x11a>
  400d52:	0f b6 c0             	movzx  eax,al
  400d55:	48 98                	cdqe   
  400d57:	0f b6 55 f7          	movzx  edx,BYTE PTR [rbp-0x9]
  400d5b:	88 90 40 24 60 00    	mov    BYTE PTR [rax+0x602440],dl
  400d61:	0f b6 05 d8 17 20 00 	movzx  eax,BYTE PTR [rip+0x2017d8]        # 602540 <stderr@GLIBC_2.2.5+0x118>
  400d68:	83 c0 01             	add    eax,0x1
  400d6b:	88 05 cf 17 20 00    	mov    BYTE PTR [rip+0x2017cf],al        # 602540 <stderr@GLIBC_2.2.5+0x118>
  400d71:	0f b6 05 c8 17 20 00 	movzx  eax,BYTE PTR [rip+0x2017c8]        # 602540 <stderr@GLIBC_2.2.5+0x118>
  400d78:	84 c0                	test   al,al
  400d7a:	0f 85 50 ff ff ff    	jne    400cd0 <strerror@plt+0x170>
  400d80:	48 81 45 f8 00 01 00 	add    QWORD PTR [rbp-0x8],0x100
  400d87:	00 
  400d88:	81 6d e4 00 01 00 00 	sub    DWORD PTR [rbp-0x1c],0x100
  400d8f:	83 7d e4 00          	cmp    DWORD PTR [rbp-0x1c],0x0
  400d93:	0f 8f 37 ff ff ff    	jg     400cd0 <strerror@plt+0x170>
  400d99:	5d                   	pop    rbp
  400d9a:	c3                   	ret    
  400d9b:	55                   	push   rbp
  400d9c:	48 89 e5             	mov    rbp,rsp
  400d9f:	48 89 7d e8          	mov    QWORD PTR [rbp-0x18],rdi
  400da3:	89 75 e4             	mov    DWORD PTR [rbp-0x1c],esi
  400da6:	48 8b 45 e8          	mov    rax,QWORD PTR [rbp-0x18]
  400daa:	48 89 45 f8          	mov    QWORD PTR [rbp-0x8],rax
  400dae:	e9 b0 00 00 00       	jmp    400e63 <strerror@plt+0x303>
  400db3:	0f b6 05 86 17 20 00 	movzx  eax,BYTE PTR [rip+0x201786]        # 602540 <stderr@GLIBC_2.2.5+0x118>
  400dba:	83 c0 01             	add    eax,0x1
  400dbd:	88 05 7d 17 20 00    	mov    BYTE PTR [rip+0x20177d],al        # 602540 <stderr@GLIBC_2.2.5+0x118>
  400dc3:	0f b6 05 76 17 20 00 	movzx  eax,BYTE PTR [rip+0x201776]        # 602540 <stderr@GLIBC_2.2.5+0x118>
  400dca:	0f b6 c0             	movzx  eax,al
  400dcd:	48 98                	cdqe   
  400dcf:	0f b6 80 40 24 60 00 	movzx  eax,BYTE PTR [rax+0x602440]
  400dd6:	88 45 f7             	mov    BYTE PTR [rbp-0x9],al
  400dd9:	0f b6 15 61 17 20 00 	movzx  edx,BYTE PTR [rip+0x201761]        # 602541 <stderr@GLIBC_2.2.5+0x119>
  400de0:	0f b6 45 f7          	movzx  eax,BYTE PTR [rbp-0x9]
  400de4:	01 d0                	add    eax,edx
  400de6:	88 05 55 17 20 00    	mov    BYTE PTR [rip+0x201755],al        # 602541 <stderr@GLIBC_2.2.5+0x119>
  400dec:	0f b6 05 4d 17 20 00 	movzx  eax,BYTE PTR [rip+0x20174d]        # 602540 <stderr@GLIBC_2.2.5+0x118>
  400df3:	0f b6 c8             	movzx  ecx,al
  400df6:	0f b6 05 44 17 20 00 	movzx  eax,BYTE PTR [rip+0x201744]        # 602541 <stderr@GLIBC_2.2.5+0x119>
  400dfd:	0f b6 c0             	movzx  eax,al
  400e00:	48 98                	cdqe   
  400e02:	0f b6 90 40 24 60 00 	movzx  edx,BYTE PTR [rax+0x602440]
  400e09:	48 63 c1             	movsxd rax,ecx
  400e0c:	88 90 40 24 60 00    	mov    BYTE PTR [rax+0x602440],dl
  400e12:	0f b6 05 28 17 20 00 	movzx  eax,BYTE PTR [rip+0x201728]        # 602541 <stderr@GLIBC_2.2.5+0x119>
  400e19:	0f b6 c0             	movzx  eax,al
  400e1c:	48 98                	cdqe   
  400e1e:	0f b6 55 f7          	movzx  edx,BYTE PTR [rbp-0x9]
  400e22:	88 90 40 24 60 00    	mov    BYTE PTR [rax+0x602440],dl
  400e28:	0f b6 05 11 17 20 00 	movzx  eax,BYTE PTR [rip+0x201711]        # 602540 <stderr@GLIBC_2.2.5+0x118>
  400e2f:	0f b6 c0             	movzx  eax,al
  400e32:	48 98                	cdqe   
  400e34:	0f b6 80 40 24 60 00 	movzx  eax,BYTE PTR [rax+0x602440]
  400e3b:	00 45 f7             	add    BYTE PTR [rbp-0x9],al
  400e3e:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
  400e42:	0f b6 10             	movzx  edx,BYTE PTR [rax]
  400e45:	0f b6 45 f7          	movzx  eax,BYTE PTR [rbp-0x9]
  400e49:	48 98                	cdqe   
  400e4b:	0f b6 80 40 24 60 00 	movzx  eax,BYTE PTR [rax+0x602440]
  400e52:	31 c2                	xor    edx,eax
  400e54:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
  400e58:	88 10                	mov    BYTE PTR [rax],dl
  400e5a:	48 83 45 f8 01       	add    QWORD PTR [rbp-0x8],0x1
  400e5f:	83 6d e4 01          	sub    DWORD PTR [rbp-0x1c],0x1
  400e63:	83 7d e4 00          	cmp    DWORD PTR [rbp-0x1c],0x0
  400e67:	0f 8f 46 ff ff ff    	jg     400db3 <strerror@plt+0x253>
  400e6d:	5d                   	pop    rbp
  400e6e:	c3                   	ret    
  400e6f:	55                   	push   rbp
  400e70:	48 89 e5             	mov    rbp,rsp
  400e73:	48 81 ec 30 01 00 00 	sub    rsp,0x130
  400e7a:	48 89 bd d8 fe ff ff 	mov    QWORD PTR [rbp-0x128],rdi
  400e81:	48 8d 95 e0 fe ff ff 	lea    rdx,[rbp-0x120]
  400e88:	48 8b 85 d8 fe ff ff 	mov    rax,QWORD PTR [rbp-0x128]
  400e8f:	48 89 d6             	mov    rsi,rdx
  400e92:	48 89 c7             	mov    rdi,rax
  400e95:	e8 76 08 00 00       	call   401710 <strerror@plt+0xbb0>
  400e9a:	85 c0                	test   eax,eax
  400e9c:	79 0a                	jns    400ea8 <strerror@plt+0x348>
  400e9e:	b8 ff ff ff ff       	mov    eax,0xffffffff
  400ea3:	e9 8c 00 00 00       	jmp    400f34 <strerror@plt+0x3d4>
  400ea8:	48 8d 85 70 ff ff ff 	lea    rax,[rbp-0x90]
  400eaf:	ba 90 00 00 00       	mov    edx,0x90
  400eb4:	be 00 00 00 00       	mov    esi,0x0
  400eb9:	48 89 c7             	mov    rdi,rax
  400ebc:	e8 7f fb ff ff       	call   400a40 <memset@plt>
  400ec1:	48 8b 85 e8 fe ff ff 	mov    rax,QWORD PTR [rbp-0x118]
  400ec8:	48 89 85 78 ff ff ff 	mov    QWORD PTR [rbp-0x88],rax
  400ecf:	48 8b 85 e0 fe ff ff 	mov    rax,QWORD PTR [rbp-0x120]
  400ed6:	48 89 85 70 ff ff ff 	mov    QWORD PTR [rbp-0x90],rax
  400edd:	48 8b 85 08 ff ff ff 	mov    rax,QWORD PTR [rbp-0xf8]
  400ee4:	48 89 45 98          	mov    QWORD PTR [rbp-0x68],rax
  400ee8:	8b 85 fc fe ff ff    	mov    eax,DWORD PTR [rbp-0x104]
  400eee:	89 45 8c             	mov    DWORD PTR [rbp-0x74],eax
  400ef1:	8b 85 00 ff ff ff    	mov    eax,DWORD PTR [rbp-0x100]
  400ef7:	89 45 90             	mov    DWORD PTR [rbp-0x70],eax
  400efa:	48 8b 85 10 ff ff ff 	mov    rax,QWORD PTR [rbp-0xf0]
  400f01:	48 89 45 a0          	mov    QWORD PTR [rbp-0x60],rax
  400f05:	48 8b 85 38 ff ff ff 	mov    rax,QWORD PTR [rbp-0xc8]
  400f0c:	48 89 45 c8          	mov    QWORD PTR [rbp-0x38],rax
  400f10:	48 8b 85 48 ff ff ff 	mov    rax,QWORD PTR [rbp-0xb8]
  400f17:	48 89 45 d8          	mov    QWORD PTR [rbp-0x28],rax
  400f1b:	48 8d 85 70 ff ff ff 	lea    rax,[rbp-0x90]
  400f22:	be 90 00 00 00       	mov    esi,0x90
  400f27:	48 89 c7             	mov    rdi,rax
  400f2a:	e8 89 fd ff ff       	call   400cb8 <strerror@plt+0x158>
  400f2f:	b8 00 00 00 00       	mov    eax,0x0
  400f34:	c9                   	leave  
  400f35:	c3                   	ret    
  400f36:	55                   	push   rbp
  400f37:	48 89 e5             	mov    rbp,rsp
  400f3a:	48 89 7d f8          	mov    QWORD PTR [rbp-0x8],rdi
  400f3e:	48 89 75 f0          	mov    QWORD PTR [rbp-0x10],rsi
  400f42:	eb 05                	jmp    400f49 <strerror@plt+0x3e9>
  400f44:	48 83 45 f8 08       	add    QWORD PTR [rbp-0x8],0x8
  400f49:	48 83 7d f8 00       	cmp    QWORD PTR [rbp-0x8],0x0
  400f4e:	74 19                	je     400f69 <strerror@plt+0x409>
  400f50:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
  400f54:	48 8b 00             	mov    rax,QWORD PTR [rax]
  400f57:	48 85 c0             	test   rax,rax
  400f5a:	74 0d                	je     400f69 <strerror@plt+0x409>
  400f5c:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
  400f60:	48 8b 00             	mov    rax,QWORD PTR [rax]
  400f63:	48 3b 45 f0          	cmp    rax,QWORD PTR [rbp-0x10]
  400f67:	75 db                	jne    400f44 <strerror@plt+0x3e4>
  400f69:	eb 14                	jmp    400f7f <strerror@plt+0x41f>
  400f6b:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
  400f6f:	48 8b 50 08          	mov    rdx,QWORD PTR [rax+0x8]
  400f73:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
  400f77:	48 89 10             	mov    QWORD PTR [rax],rdx
  400f7a:	48 83 45 f8 08       	add    QWORD PTR [rbp-0x8],0x8
  400f7f:	48 83 7d f8 00       	cmp    QWORD PTR [rbp-0x8],0x0
  400f84:	74 0c                	je     400f92 <strerror@plt+0x432>
  400f86:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
  400f8a:	48 8b 00             	mov    rax,QWORD PTR [rax]
  400f8d:	48 85 c0             	test   rax,rax
  400f90:	75 d9                	jne    400f6b <strerror@plt+0x40b>
  400f92:	5d                   	pop    rbp
  400f93:	c3                   	ret    
  400f94:	55                   	push   rbp
  400f95:	48 89 e5             	mov    rbp,rsp
  400f98:	53                   	push   rbx
  400f99:	48 81 ec 58 02 00 00 	sub    rsp,0x258
  400fa0:	89 bd ac fd ff ff    	mov    DWORD PTR [rbp-0x254],edi
  400fa6:	64 48 8b 04 25 28 00 	mov    rax,QWORD PTR fs:0x28
  400fad:	00 00 
  400faf:	48 89 45 e8          	mov    QWORD PTR [rbp-0x18],rax
  400fb3:	31 c0                	xor    eax,eax
  400fb5:	e8 56 fa ff ff       	call   400a10 <getpid@plt>
  400fba:	48 98                	cdqe   
  400fbc:	48 89 85 c8 fd ff ff 	mov    QWORD PTR [rbp-0x238],rax
  400fc3:	e8 95 fc ff ff       	call   400c5d <strerror@plt+0xfd>
  400fc8:	ba 7b 11 40 00       	mov    edx,0x40117b
  400fcd:	b8 94 0f 40 00       	mov    eax,0x400f94
  400fd2:	48 29 c2             	sub    rdx,rax
  400fd5:	48 89 d0             	mov    rax,rdx
  400fd8:	89 c6                	mov    esi,eax
  400fda:	bf 94 0f 40 00       	mov    edi,0x400f94
  400fdf:	e8 d4 fc ff ff       	call   400cb8 <strerror@plt+0x158>
  400fe4:	be 1c 03 00 00       	mov    esi,0x31c
  400fe9:	bf 00 21 60 00       	mov    edi,0x602100
  400fee:	e8 c5 fc ff ff       	call   400cb8 <strerror@plt+0x158>
  400ff3:	48 8d 85 c8 fd ff ff 	lea    rax,[rbp-0x238]
  400ffa:	be 08 00 00 00       	mov    esi,0x8
  400fff:	48 89 c7             	mov    rdi,rax
  401002:	e8 b1 fc ff ff       	call   400cb8 <strerror@plt+0x158>
  401007:	48 8d 85 c8 fd ff ff 	lea    rax,[rbp-0x238]
  40100e:	be 08 00 00 00       	mov    esi,0x8
  401013:	48 89 c7             	mov    rdi,rax
  401016:	e8 80 fd ff ff       	call   400d9b <strerror@plt+0x23b>
  40101b:	48 8b 95 c8 fd ff ff 	mov    rdx,QWORD PTR [rbp-0x238]
  401022:	48 8d 85 e0 fd ff ff 	lea    rax,[rbp-0x220]
  401029:	be 38 17 40 00       	mov    esi,0x401738
  40102e:	48 89 c7             	mov    rdi,rax
  401031:	b8 00 00 00 00       	mov    eax,0x0
  401036:	e8 e5 fa ff ff       	call   400b20 <sprintf@plt>
  40103b:	48 8d 85 e0 fd ff ff 	lea    rax,[rbp-0x220]
  401042:	48 89 c7             	mov    rdi,rax
  401045:	e8 a6 f9 ff ff       	call   4009f0 <getenv@plt>
  40104a:	48 89 85 d8 fd ff ff 	mov    QWORD PTR [rbp-0x228],rax
  401051:	48 8d 85 e0 fd ff ff 	lea    rax,[rbp-0x220]
  401058:	48 89 c7             	mov    rdi,rax
  40105b:	e8 c0 f9 ff ff       	call   400a20 <strlen@plt>
  401060:	89 85 c0 fd ff ff    	mov    DWORD PTR [rbp-0x240],eax
  401066:	48 83 bd d8 fd ff ff 	cmp    QWORD PTR [rbp-0x228],0x0
  40106d:	00 
  40106e:	75 56                	jne    4010c6 <strerror@plt+0x566>
  401070:	48 8b 85 c8 fd ff ff 	mov    rax,QWORD PTR [rbp-0x238]
  401077:	48 8d 8d e0 fd ff ff 	lea    rcx,[rbp-0x220]
  40107e:	8b 95 c0 fd ff ff    	mov    edx,DWORD PTR [rbp-0x240]
  401084:	48 63 d2             	movsxd rdx,edx
  401087:	48 8d 3c 11          	lea    rdi,[rcx+rdx*1]
  40108b:	8b 95 ac fd ff ff    	mov    edx,DWORD PTR [rbp-0x254]
  401091:	89 d1                	mov    ecx,edx
  401093:	48 89 c2             	mov    rdx,rax
  401096:	be 3d 17 40 00       	mov    esi,0x40173d
  40109b:	b8 00 00 00 00       	mov    eax,0x0
  4010a0:	e8 7b fa ff ff       	call   400b20 <sprintf@plt>
  4010a5:	48 8d 85 e0 fd ff ff 	lea    rax,[rbp-0x220]
  4010ac:	48 89 c7             	mov    rdi,rax
  4010af:	e8 9c fa ff ff       	call   400b50 <strdup@plt>
  4010b4:	48 89 c7             	mov    rdi,rax
  4010b7:	e8 c4 f9 ff ff       	call   400a80 <putenv@plt>
  4010bc:	b8 00 00 00 00       	mov    eax,0x0
  4010c1:	e9 97 00 00 00       	jmp    40115d <strerror@plt+0x5fd>
  4010c6:	48 8d b5 e0 fd ff ff 	lea    rsi,[rbp-0x220]
  4010cd:	48 8d 8d bc fd ff ff 	lea    rcx,[rbp-0x244]
  4010d4:	48 8d 95 d0 fd ff ff 	lea    rdx,[rbp-0x230]
  4010db:	48 8b 85 d8 fd ff ff 	mov    rax,QWORD PTR [rbp-0x228]
  4010e2:	49 89 f0             	mov    r8,rsi
  4010e5:	be 45 17 40 00       	mov    esi,0x401745
  4010ea:	48 89 c7             	mov    rdi,rax
  4010ed:	b8 00 00 00 00       	mov    eax,0x0
  4010f2:	e8 09 fa ff ff       	call   400b00 <__isoc99_sscanf@plt>
  4010f7:	89 85 c4 fd ff ff    	mov    DWORD PTR [rbp-0x23c],eax
  4010fd:	83 bd c4 fd ff ff 02 	cmp    DWORD PTR [rbp-0x23c],0x2
  401104:	75 52                	jne    401158 <strerror@plt+0x5f8>
  401106:	48 8b 95 d0 fd ff ff 	mov    rdx,QWORD PTR [rbp-0x230]
  40110d:	48 8b 85 c8 fd ff ff 	mov    rax,QWORD PTR [rbp-0x238]
  401114:	48 39 c2             	cmp    rdx,rax
  401117:	75 3f                	jne    401158 <strerror@plt+0x5f8>
  401119:	8b 85 c0 fd ff ff    	mov    eax,DWORD PTR [rbp-0x240]
  40111f:	f7 d8                	neg    eax
  401121:	48 98                	cdqe   
  401123:	48 8d 50 ff          	lea    rdx,[rax-0x1]
  401127:	48 8b 85 d8 fd ff ff 	mov    rax,QWORD PTR [rbp-0x228]
  40112e:	48 01 c2             	add    rdx,rax
  401131:	48 8b 05 e8 12 20 00 	mov    rax,QWORD PTR [rip+0x2012e8]        # 602420 <__environ@GLIBC_2.2.5>
  401138:	48 89 d6             	mov    rsi,rdx
  40113b:	48 89 c7             	mov    rdi,rax
  40113e:	e8 f3 fd ff ff       	call   400f36 <strerror@plt+0x3d6>
  401143:	8b 85 bc fd ff ff    	mov    eax,DWORD PTR [rbp-0x244]
  401149:	8b 95 ac fd ff ff    	mov    edx,DWORD PTR [rbp-0x254]
  40114f:	29 c2                	sub    edx,eax
  401151:	89 d0                	mov    eax,edx
  401153:	83 c0 01             	add    eax,0x1
  401156:	eb 05                	jmp    40115d <strerror@plt+0x5fd>
  401158:	b8 ff ff ff ff       	mov    eax,0xffffffff
  40115d:	48 8b 5d e8          	mov    rbx,QWORD PTR [rbp-0x18]
  401161:	64 48 33 1c 25 28 00 	xor    rbx,QWORD PTR fs:0x28
  401168:	00 00 
  40116a:	74 05                	je     401171 <strerror@plt+0x611>
  40116c:	e8 bf f8 ff ff       	call   400a30 <__stack_chk_fail@plt>
  401171:	48 81 c4 58 02 00 00 	add    rsp,0x258
  401178:	5b                   	pop    rbx
  401179:	5d                   	pop    rbp
  40117a:	c3                   	ret    
  40117b:	55                   	push   rbp
  40117c:	48 89 e5             	mov    rbp,rsp
  40117f:	5d                   	pop    rbp
  401180:	c3                   	ret    
  401181:	55                   	push   rbp
  401182:	48 89 e5             	mov    rbp,rsp
  401185:	53                   	push   rbx
  401186:	48 83 ec 48          	sub    rsp,0x48
  40118a:	89 7d bc             	mov    DWORD PTR [rbp-0x44],edi
  40118d:	48 89 75 b0          	mov    QWORD PTR [rbp-0x50],rsi
  401191:	48 8b 45 b0          	mov    rax,QWORD PTR [rbp-0x50]
  401195:	48 8b 00             	mov    rax,QWORD PTR [rax]
  401198:	48 89 45 e0          	mov    QWORD PTR [rbp-0x20],rax
  40119c:	48 83 7d e0 00       	cmp    QWORD PTR [rbp-0x20],0x0
  4011a1:	75 0e                	jne    4011b1 <strerror@plt+0x651>
  4011a3:	bf 4e 17 40 00       	mov    edi,0x40174e
  4011a8:	e8 43 f8 ff ff       	call   4009f0 <getenv@plt>
  4011ad:	48 89 45 e0          	mov    QWORD PTR [rbp-0x20],rax
  4011b1:	48 83 7d e0 00       	cmp    QWORD PTR [rbp-0x20],0x0
  4011b6:	75 28                	jne    4011e0 <strerror@plt+0x680>
  4011b8:	48 8b 05 69 12 20 00 	mov    rax,QWORD PTR [rip+0x201269]        # 602428 <stderr@GLIBC_2.2.5>
  4011bf:	48 89 c1             	mov    rcx,rax
  4011c2:	ba 20 00 00 00       	mov    edx,0x20
  4011c7:	be 01 00 00 00       	mov    esi,0x1
  4011cc:	bf 50 17 40 00       	mov    edi,0x401750
  4011d1:	e8 6a f9 ff ff       	call   400b40 <fwrite@plt>
  4011d6:	bf 01 00 00 00       	mov    edi,0x1
  4011db:	e8 50 f9 ff ff       	call   400b30 <exit@plt>
  4011e0:	8b 45 bc             	mov    eax,DWORD PTR [rbp-0x44]
  4011e3:	89 c7                	mov    edi,eax
  4011e5:	e8 aa fd ff ff       	call   400f94 <strerror@plt+0x434>
  4011ea:	89 45 d4             	mov    DWORD PTR [rbp-0x2c],eax
  4011ed:	e8 6b fa ff ff       	call   400c5d <strerror@plt+0xfd>
  4011f2:	be 00 01 00 00       	mov    esi,0x100
  4011f7:	bf df 22 60 00       	mov    edi,0x6022df
  4011fc:	e8 b7 fa ff ff       	call   400cb8 <strerror@plt+0x158>
  401201:	be 41 00 00 00       	mov    esi,0x41
  401206:	bf 7a 22 60 00       	mov    edi,0x60227a
  40120b:	e8 8b fb ff ff       	call   400d9b <strerror@plt+0x23b>
  401210:	be 01 00 00 00       	mov    esi,0x1
  401215:	bf f6 23 60 00       	mov    edi,0x6023f6
  40121a:	e8 7c fb ff ff       	call   400d9b <strerror@plt+0x23b>
  40121f:	0f b6 05 d0 11 20 00 	movzx  eax,BYTE PTR [rip+0x2011d0]        # 6023f6 <strerror@plt+0x201896>
  401226:	84 c0                	test   al,al
  401228:	74 26                	je     401250 <strerror@plt+0x6f0>
  40122a:	bf f6 23 60 00       	mov    edi,0x6023f6
  40122f:	e8 5c f8 ff ff       	call   400a90 <atoll@plt>
  401234:	48 89 c3             	mov    rbx,rax
  401237:	bf 00 00 00 00       	mov    edi,0x0
  40123c:	e8 8f f8 ff ff       	call   400ad0 <time@plt>
  401241:	48 39 c3             	cmp    rbx,rax
  401244:	7d 0a                	jge    401250 <strerror@plt+0x6f0>
  401246:	b8 7a 22 60 00       	mov    eax,0x60227a
  40124b:	e9 7d 03 00 00       	jmp    4015cd <strerror@plt+0xa6d>
  401250:	be 08 00 00 00       	mov    esi,0x8
  401255:	bf 11 24 60 00       	mov    edi,0x602411
  40125a:	e8 3c fb ff ff       	call   400d9b <strerror@plt+0x23b>
  40125f:	be 03 00 00 00       	mov    esi,0x3
  401264:	bf 55 21 60 00       	mov    edi,0x602155
  401269:	e8 2d fb ff ff       	call   400d9b <strerror@plt+0x23b>
  40126e:	be 0f 00 00 00       	mov    esi,0xf
  401273:	bf 45 21 60 00       	mov    edi,0x602145
  401278:	e8 1e fb ff ff       	call   400d9b <strerror@plt+0x23b>
  40127d:	be 01 00 00 00       	mov    esi,0x1
  401282:	bf 1a 24 60 00       	mov    edi,0x60241a
  401287:	e8 0f fb ff ff       	call   400d9b <strerror@plt+0x23b>
  40128c:	be 16 00 00 00       	mov    esi,0x16
  401291:	bf f8 23 60 00       	mov    edi,0x6023f8
  401296:	e8 00 fb ff ff       	call   400d9b <strerror@plt+0x23b>
  40129b:	be 16 00 00 00       	mov    esi,0x16
  4012a0:	bf f8 23 60 00       	mov    edi,0x6023f8
  4012a5:	e8 0e fa ff ff       	call   400cb8 <strerror@plt+0x158>
  4012aa:	be 16 00 00 00       	mov    esi,0x16
  4012af:	bf 00 21 60 00       	mov    edi,0x602100
  4012b4:	e8 e2 fa ff ff       	call   400d9b <strerror@plt+0x23b>
  4012b9:	ba 16 00 00 00       	mov    edx,0x16
  4012be:	be 00 21 60 00       	mov    esi,0x602100
  4012c3:	bf f8 23 60 00       	mov    edi,0x6023f8
  4012c8:	e8 93 f7 ff ff       	call   400a60 <memcmp@plt>
  4012cd:	85 c0                	test   eax,eax
  4012cf:	74 0a                	je     4012db <strerror@plt+0x77b>
  4012d1:	b8 f8 23 60 00       	mov    eax,0x6023f8
  4012d6:	e9 f2 02 00 00       	jmp    4015cd <strerror@plt+0xa6d>
  4012db:	be 13 00 00 00       	mov    esi,0x13
  4012e0:	bf 31 21 60 00       	mov    edi,0x602131
  4012e5:	e8 b1 fa ff ff       	call   400d9b <strerror@plt+0x23b>
  4012ea:	83 7d d4 00          	cmp    DWORD PTR [rbp-0x2c],0x0
  4012ee:	79 0a                	jns    4012fa <strerror@plt+0x79a>
  4012f0:	b8 31 21 60 00       	mov    eax,0x602131
  4012f5:	e9 d3 02 00 00       	jmp    4015cd <strerror@plt+0xa6d>
  4012fa:	8b 45 bc             	mov    eax,DWORD PTR [rbp-0x44]
  4012fd:	83 c0 0a             	add    eax,0xa
  401300:	48 98                	cdqe   
  401302:	be 08 00 00 00       	mov    esi,0x8
  401307:	48 89 c7             	mov    rdi,rax
  40130a:	e8 61 f7 ff ff       	call   400a70 <calloc@plt>
  40130f:	48 89 45 e8          	mov    QWORD PTR [rbp-0x18],rax
  401313:	48 83 7d e8 00       	cmp    QWORD PTR [rbp-0x18],0x0
  401318:	75 0a                	jne    401324 <strerror@plt+0x7c4>
  40131a:	b8 00 00 00 00       	mov    eax,0x0
  40131f:	e9 a9 02 00 00       	jmp    4015cd <strerror@plt+0xa6d>
  401324:	83 7d d4 00          	cmp    DWORD PTR [rbp-0x2c],0x0
  401328:	0f 84 f2 00 00 00    	je     401420 <strerror@plt+0x8c0>
  40132e:	be 01 00 00 00       	mov    esi,0x1
  401333:	bf 19 21 60 00       	mov    edi,0x602119
  401338:	e8 5e fa ff ff       	call   400d9b <strerror@plt+0x23b>
  40133d:	0f b6 05 d5 0d 20 00 	movzx  eax,BYTE PTR [rip+0x200dd5]        # 602119 <strerror@plt+0x2015b9>
  401344:	84 c0                	test   al,al
  401346:	75 18                	jne    401360 <strerror@plt+0x800>
  401348:	bf 11 24 60 00       	mov    edi,0x602411
  40134d:	e8 1d fb ff ff       	call   400e6f <strerror@plt+0x30f>
  401352:	85 c0                	test   eax,eax
  401354:	74 0a                	je     401360 <strerror@plt+0x800>
  401356:	b8 11 24 60 00       	mov    eax,0x602411
  40135b:	e9 6d 02 00 00       	jmp    4015cd <strerror@plt+0xa6d>
  401360:	be 01 00 00 00       	mov    esi,0x1
  401365:	bf 54 21 60 00       	mov    edi,0x602154
  40136a:	e8 2c fa ff ff       	call   400d9b <strerror@plt+0x23b>
  40136f:	be ce 00 00 00       	mov    esi,0xce
  401374:	bf 80 21 60 00       	mov    edi,0x602180
  401379:	e8 1d fa ff ff       	call   400d9b <strerror@plt+0x23b>
  40137e:	be 13 00 00 00       	mov    esi,0x13
  401383:	bf 5a 22 60 00       	mov    edi,0x60225a
  401388:	e8 0e fa ff ff       	call   400d9b <strerror@plt+0x23b>
  40138d:	be 13 00 00 00       	mov    esi,0x13
  401392:	bf 5a 22 60 00       	mov    edi,0x60225a
  401397:	e8 1c f9 ff ff       	call   400cb8 <strerror@plt+0x158>
  40139c:	be 13 00 00 00       	mov    esi,0x13
  4013a1:	bf 1a 21 60 00       	mov    edi,0x60211a
  4013a6:	e8 f0 f9 ff ff       	call   400d9b <strerror@plt+0x23b>
  4013ab:	ba 13 00 00 00       	mov    edx,0x13
  4013b0:	be 1a 21 60 00       	mov    esi,0x60211a
  4013b5:	bf 5a 22 60 00       	mov    edi,0x60225a
  4013ba:	e8 a1 f6 ff ff       	call   400a60 <memcmp@plt>
  4013bf:	85 c0                	test   eax,eax
  4013c1:	74 0a                	je     4013cd <strerror@plt+0x86d>
  4013c3:	b8 5a 22 60 00       	mov    eax,0x60225a
  4013c8:	e9 00 02 00 00       	jmp    4015cd <strerror@plt+0xa6d>
  4013cd:	bf ce 10 00 00       	mov    edi,0x10ce
  4013d2:	e8 19 f7 ff ff       	call   400af0 <malloc@plt>
  4013d7:	48 89 45 d8          	mov    QWORD PTR [rbp-0x28],rax
  4013db:	48 83 7d d8 00       	cmp    QWORD PTR [rbp-0x28],0x0
  4013e0:	75 0a                	jne    4013ec <strerror@plt+0x88c>
  4013e2:	b8 00 00 00 00       	mov    eax,0x0
  4013e7:	e9 e1 01 00 00       	jmp    4015cd <strerror@plt+0xa6d>
  4013ec:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
  4013f0:	ba 00 10 00 00       	mov    edx,0x1000
  4013f5:	be 20 00 00 00       	mov    esi,0x20
  4013fa:	48 89 c7             	mov    rdi,rax
  4013fd:	e8 3e f6 ff ff       	call   400a40 <memset@plt>
  401402:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
  401406:	48 05 00 10 00 00    	add    rax,0x1000
  40140c:	ba ce 00 00 00       	mov    edx,0xce
  401411:	be 80 21 60 00       	mov    esi,0x602180
  401416:	48 89 c7             	mov    rdi,rax
  401419:	e8 a2 f6 ff ff       	call   400ac0 <memcpy@plt>
  40141e:	eb 4e                	jmp    40146e <strerror@plt+0x90e>
  401420:	0f b6 05 1e 0d 20 00 	movzx  eax,BYTE PTR [rip+0x200d1e]        # 602145 <strerror@plt+0x2015e5>
  401427:	84 c0                	test   al,al
  401429:	74 3b                	je     401466 <strerror@plt+0x906>
  40142b:	bf 00 02 00 00       	mov    edi,0x200
  401430:	e8 bb f6 ff ff       	call   400af0 <malloc@plt>
  401435:	48 89 45 d8          	mov    QWORD PTR [rbp-0x28],rax
  401439:	48 83 7d d8 00       	cmp    QWORD PTR [rbp-0x28],0x0
  40143e:	75 0a                	jne    40144a <strerror@plt+0x8ea>
  401440:	b8 00 00 00 00       	mov    eax,0x0
  401445:	e9 83 01 00 00       	jmp    4015cd <strerror@plt+0xa6d>
  40144a:	48 8b 55 e0          	mov    rdx,QWORD PTR [rbp-0x20]
  40144e:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
  401452:	be 45 21 60 00       	mov    esi,0x602145
  401457:	48 89 c7             	mov    rdi,rax
  40145a:	b8 00 00 00 00       	mov    eax,0x0
  40145f:	e8 bc f6 ff ff       	call   400b20 <sprintf@plt>
  401464:	eb 08                	jmp    40146e <strerror@plt+0x90e>
  401466:	48 8b 45 e0          	mov    rax,QWORD PTR [rbp-0x20]
  40146a:	48 89 45 d8          	mov    QWORD PTR [rbp-0x28],rax
  40146e:	c7 45 d0 00 00 00 00 	mov    DWORD PTR [rbp-0x30],0x0
  401475:	8b 45 d0             	mov    eax,DWORD PTR [rbp-0x30]
  401478:	8d 50 01             	lea    edx,[rax+0x1]
  40147b:	89 55 d0             	mov    DWORD PTR [rbp-0x30],edx
  40147e:	48 98                	cdqe   
  401480:	48 8d 14 c5 00 00 00 	lea    rdx,[rax*8+0x0]
  401487:	00 
  401488:	48 8b 45 e8          	mov    rax,QWORD PTR [rbp-0x18]
  40148c:	48 01 c2             	add    rdx,rax
  40148f:	48 8b 45 b0          	mov    rax,QWORD PTR [rbp-0x50]
  401493:	48 8b 00             	mov    rax,QWORD PTR [rax]
  401496:	48 89 02             	mov    QWORD PTR [rdx],rax
  401499:	83 7d d4 00          	cmp    DWORD PTR [rbp-0x2c],0x0
  40149d:	74 2c                	je     4014cb <strerror@plt+0x96b>
  40149f:	0f b6 05 ae 0c 20 00 	movzx  eax,BYTE PTR [rip+0x200cae]        # 602154 <strerror@plt+0x2015f4>
  4014a6:	84 c0                	test   al,al
  4014a8:	74 21                	je     4014cb <strerror@plt+0x96b>
  4014aa:	8b 45 d0             	mov    eax,DWORD PTR [rbp-0x30]
  4014ad:	8d 50 01             	lea    edx,[rax+0x1]
  4014b0:	89 55 d0             	mov    DWORD PTR [rbp-0x30],edx
  4014b3:	48 98                	cdqe   
  4014b5:	48 8d 14 c5 00 00 00 	lea    rdx,[rax*8+0x0]
  4014bc:	00 
  4014bd:	48 8b 45 e8          	mov    rax,QWORD PTR [rbp-0x18]
  4014c1:	48 01 d0             	add    rax,rdx
  4014c4:	48 c7 00 54 21 60 00 	mov    QWORD PTR [rax],0x602154
  4014cb:	0f b6 05 83 0c 20 00 	movzx  eax,BYTE PTR [rip+0x200c83]        # 602155 <strerror@plt+0x2015f5>
  4014d2:	84 c0                	test   al,al
  4014d4:	74 21                	je     4014f7 <strerror@plt+0x997>
  4014d6:	8b 45 d0             	mov    eax,DWORD PTR [rbp-0x30]
  4014d9:	8d 50 01             	lea    edx,[rax+0x1]
  4014dc:	89 55 d0             	mov    DWORD PTR [rbp-0x30],edx
  4014df:	48 98                	cdqe   
  4014e1:	48 8d 14 c5 00 00 00 	lea    rdx,[rax*8+0x0]
  4014e8:	00 
  4014e9:	48 8b 45 e8          	mov    rax,QWORD PTR [rbp-0x18]
  4014ed:	48 01 d0             	add    rax,rdx
  4014f0:	48 c7 00 55 21 60 00 	mov    QWORD PTR [rax],0x602155
  4014f7:	8b 45 d0             	mov    eax,DWORD PTR [rbp-0x30]
  4014fa:	8d 50 01             	lea    edx,[rax+0x1]
  4014fd:	89 55 d0             	mov    DWORD PTR [rbp-0x30],edx
  401500:	48 98                	cdqe   
  401502:	48 8d 14 c5 00 00 00 	lea    rdx,[rax*8+0x0]
  401509:	00 
  40150a:	48 8b 45 e8          	mov    rax,QWORD PTR [rbp-0x18]
  40150e:	48 01 c2             	add    rdx,rax
  401511:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
  401515:	48 89 02             	mov    QWORD PTR [rdx],rax
  401518:	0f b6 05 fb 0e 20 00 	movzx  eax,BYTE PTR [rip+0x200efb]        # 60241a <strerror@plt+0x2018ba>
  40151f:	84 c0                	test   al,al
  401521:	74 21                	je     401544 <strerror@plt+0x9e4>
  401523:	8b 45 d0             	mov    eax,DWORD PTR [rbp-0x30]
  401526:	8d 50 01             	lea    edx,[rax+0x1]
  401529:	89 55 d0             	mov    DWORD PTR [rbp-0x30],edx
  40152c:	48 98                	cdqe   
  40152e:	48 8d 14 c5 00 00 00 	lea    rdx,[rax*8+0x0]
  401535:	00 
  401536:	48 8b 45 e8          	mov    rax,QWORD PTR [rbp-0x18]
  40153a:	48 01 d0             	add    rax,rdx
  40153d:	48 c7 00 1a 24 60 00 	mov    QWORD PTR [rax],0x60241a
  401544:	83 7d d4 01          	cmp    DWORD PTR [rbp-0x2c],0x1
  401548:	7e 05                	jle    40154f <strerror@plt+0x9ef>
  40154a:	8b 45 d4             	mov    eax,DWORD PTR [rbp-0x2c]
  40154d:	eb 05                	jmp    401554 <strerror@plt+0x9f4>
  40154f:	b8 00 00 00 00       	mov    eax,0x0
  401554:	89 45 cc             	mov    DWORD PTR [rbp-0x34],eax
  401557:	eb 3b                	jmp    401594 <strerror@plt+0xa34>
  401559:	8b 45 d0             	mov    eax,DWORD PTR [rbp-0x30]
  40155c:	8d 50 01             	lea    edx,[rax+0x1]
  40155f:	89 55 d0             	mov    DWORD PTR [rbp-0x30],edx
  401562:	48 98                	cdqe   
  401564:	48 8d 14 c5 00 00 00 	lea    rdx,[rax*8+0x0]
  40156b:	00 
  40156c:	48 8b 45 e8          	mov    rax,QWORD PTR [rbp-0x18]
  401570:	48 8d 0c 02          	lea    rcx,[rdx+rax*1]
  401574:	8b 45 cc             	mov    eax,DWORD PTR [rbp-0x34]
  401577:	8d 50 01             	lea    edx,[rax+0x1]
  40157a:	89 55 cc             	mov    DWORD PTR [rbp-0x34],edx
  40157d:	48 98                	cdqe   
  40157f:	48 8d 14 c5 00 00 00 	lea    rdx,[rax*8+0x0]
  401586:	00 
  401587:	48 8b 45 b0          	mov    rax,QWORD PTR [rbp-0x50]
  40158b:	48 01 d0             	add    rax,rdx
  40158e:	48 8b 00             	mov    rax,QWORD PTR [rax]
  401591:	48 89 01             	mov    QWORD PTR [rcx],rax
  401594:	8b 45 cc             	mov    eax,DWORD PTR [rbp-0x34]
  401597:	3b 45 bc             	cmp    eax,DWORD PTR [rbp-0x44]
  40159a:	7c bd                	jl     401559 <strerror@plt+0x9f9>
  40159c:	8b 45 d0             	mov    eax,DWORD PTR [rbp-0x30]
  40159f:	48 98                	cdqe   
  4015a1:	48 8d 14 c5 00 00 00 	lea    rdx,[rax*8+0x0]
  4015a8:	00 
  4015a9:	48 8b 45 e8          	mov    rax,QWORD PTR [rbp-0x18]
  4015ad:	48 01 d0             	add    rax,rdx
  4015b0:	48 c7 00 00 00 00 00 	mov    QWORD PTR [rax],0x0
  4015b7:	48 8b 45 e8          	mov    rax,QWORD PTR [rbp-0x18]
  4015bb:	48 89 c6             	mov    rsi,rax
  4015be:	bf 11 24 60 00       	mov    edi,0x602411
  4015c3:	e8 48 f5 ff ff       	call   400b10 <execvp@plt>
  4015c8:	b8 11 24 60 00       	mov    eax,0x602411
  4015cd:	48 83 c4 48          	add    rsp,0x48
  4015d1:	5b                   	pop    rbx
  4015d2:	5d                   	pop    rbp
  4015d3:	c3                   	ret    
  4015d4:	55                   	push   rbp
  4015d5:	48 89 e5             	mov    rbp,rsp
  4015d8:	41 54                	push   r12
  4015da:	53                   	push   rbx
  4015db:	48 83 ec 10          	sub    rsp,0x10
  4015df:	89 7d ec             	mov    DWORD PTR [rbp-0x14],edi
  4015e2:	48 89 75 e0          	mov    QWORD PTR [rbp-0x20],rsi
  4015e6:	48 8b 45 e0          	mov    rax,QWORD PTR [rbp-0x20]
  4015ea:	48 8d 58 08          	lea    rbx,[rax+0x8]
  4015ee:	48 8b 55 e0          	mov    rdx,QWORD PTR [rbp-0x20]
  4015f2:	8b 45 ec             	mov    eax,DWORD PTR [rbp-0x14]
  4015f5:	48 89 d6             	mov    rsi,rdx
  4015f8:	89 c7                	mov    edi,eax
  4015fa:	e8 82 fb ff ff       	call   401181 <strerror@plt+0x621>
  4015ff:	48 89 03             	mov    QWORD PTR [rbx],rax
  401602:	48 8b 45 e0          	mov    rax,QWORD PTR [rbp-0x20]
  401606:	48 83 c0 08          	add    rax,0x8
  40160a:	48 8b 00             	mov    rax,QWORD PTR [rax]
  40160d:	48 85 c0             	test   rax,rax
  401610:	74 0a                	je     40161c <strerror@plt+0xabc>
  401612:	48 8b 45 e0          	mov    rax,QWORD PTR [rbp-0x20]
  401616:	4c 8b 60 08          	mov    r12,QWORD PTR [rax+0x8]
  40161a:	eb 06                	jmp    401622 <strerror@plt+0xac2>
  40161c:	41 bc 71 17 40 00    	mov    r12d,0x401771
  401622:	e8 d9 f3 ff ff       	call   400a00 <__errno_location@plt>
  401627:	8b 00                	mov    eax,DWORD PTR [rax]
  401629:	85 c0                	test   eax,eax
  40162b:	74 13                	je     401640 <strerror@plt+0xae0>
  40162d:	e8 ce f3 ff ff       	call   400a00 <__errno_location@plt>
  401632:	8b 00                	mov    eax,DWORD PTR [rax]
  401634:	89 c7                	mov    edi,eax
  401636:	e8 25 f5 ff ff       	call   400b60 <strerror@plt>
  40163b:	48 89 c3             	mov    rbx,rax
  40163e:	eb 05                	jmp    401645 <strerror@plt+0xae5>
  401640:	bb 78 17 40 00       	mov    ebx,0x401778
  401645:	e8 b6 f3 ff ff       	call   400a00 <__errno_location@plt>
  40164a:	8b 00                	mov    eax,DWORD PTR [rax]
  40164c:	85 c0                	test   eax,eax
  40164e:	74 07                	je     401657 <strerror@plt+0xaf7>
  401650:	b8 79 17 40 00       	mov    eax,0x401779
  401655:	eb 05                	jmp    40165c <strerror@plt+0xafc>
  401657:	b8 78 17 40 00       	mov    eax,0x401778
  40165c:	48 8b 55 e0          	mov    rdx,QWORD PTR [rbp-0x20]
  401660:	48 8b 12             	mov    rdx,QWORD PTR [rdx]
  401663:	48 8b 3d be 0d 20 00 	mov    rdi,QWORD PTR [rip+0x200dbe]        # 602428 <stderr@GLIBC_2.2.5>
  40166a:	4d 89 e1             	mov    r9,r12
  40166d:	49 89 d8             	mov    r8,rbx
  401670:	48 89 c1             	mov    rcx,rax
  401673:	be 7c 17 40 00       	mov    esi,0x40177c
  401678:	b8 00 00 00 00       	mov    eax,0x0
  40167d:	e8 1e f4 ff ff       	call   400aa0 <fprintf@plt>
  401682:	b8 01 00 00 00       	mov    eax,0x1
  401687:	48 83 c4 10          	add    rsp,0x10
  40168b:	5b                   	pop    rbx
  40168c:	41 5c                	pop    r12
  40168e:	5d                   	pop    rbp
  40168f:	c3                   	ret    
  401690:	41 57                	push   r15
  401692:	41 89 ff             	mov    r15d,edi
  401695:	41 56                	push   r14
  401697:	49 89 f6             	mov    r14,rsi
  40169a:	41 55                	push   r13
  40169c:	49 89 d5             	mov    r13,rdx
  40169f:	41 54                	push   r12
  4016a1:	4c 8d 25 68 07 20 00 	lea    r12,[rip+0x200768]        # 601e10 <strerror@plt+0x2012b0>
  4016a8:	55                   	push   rbp
  4016a9:	48 8d 2d 68 07 20 00 	lea    rbp,[rip+0x200768]        # 601e18 <strerror@plt+0x2012b8>
  4016b0:	53                   	push   rbx
  4016b1:	4c 29 e5             	sub    rbp,r12
  4016b4:	31 db                	xor    ebx,ebx
  4016b6:	48 c1 fd 03          	sar    rbp,0x3
  4016ba:	48 83 ec 08          	sub    rsp,0x8
  4016be:	e8 fd f2 ff ff       	call   4009c0 <getenv@plt-0x30>
  4016c3:	48 85 ed             	test   rbp,rbp
  4016c6:	74 1e                	je     4016e6 <strerror@plt+0xb86>
  4016c8:	0f 1f 84 00 00 00 00 	nop    DWORD PTR [rax+rax*1+0x0]
  4016cf:	00 
  4016d0:	4c 89 ea             	mov    rdx,r13
  4016d3:	4c 89 f6             	mov    rsi,r14
  4016d6:	44 89 ff             	mov    edi,r15d
  4016d9:	41 ff 14 dc          	call   QWORD PTR [r12+rbx*8]
  4016dd:	48 83 c3 01          	add    rbx,0x1
  4016e1:	48 39 eb             	cmp    rbx,rbp
  4016e4:	75 ea                	jne    4016d0 <strerror@plt+0xb70>
  4016e6:	48 83 c4 08          	add    rsp,0x8
  4016ea:	5b                   	pop    rbx
  4016eb:	5d                   	pop    rbp
  4016ec:	41 5c                	pop    r12
  4016ee:	41 5d                	pop    r13
  4016f0:	41 5e                	pop    r14
  4016f2:	41 5f                	pop    r15
  4016f4:	c3                   	ret    
  4016f5:	66 66 2e 0f 1f 84 00 	data16 cs nop WORD PTR [rax+rax*1+0x0]
  4016fc:	00 00 00 00 
  401700:	f3 c3                	repz ret 
  401702:	66 2e 0f 1f 84 00 00 	cs nop WORD PTR [rax+rax*1+0x0]
  401709:	00 00 00 
  40170c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
  401710:	48 89 f2             	mov    rdx,rsi
  401713:	48 89 fe             	mov    rsi,rdi
  401716:	bf 01 00 00 00       	mov    edi,0x1
  40171b:	e9 c0 f3 ff ff       	jmp    400ae0 <__xstat@plt>

Disassembly of section .fini:

0000000000401720 <.fini>:
  401720:	48 83 ec 08          	sub    rsp,0x8
  401724:	48 83 c4 08          	add    rsp,0x8
  401728:	c3                   	ret    
