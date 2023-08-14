# ASM-Preprocessor
[![Python](https://img.shields.io/badge/Python-3.7+-brightgreen.svg)]()  
Since its creation, assembly has become the basis of programming languages in the world.  
Compilation is close to the bottom and fast, reducing the runtime of large applications.  
This program makes it easier for you to write ASM code and allows ASM to support #include and #define features.  

Usage:
> asmp.py [ASM File]

If you have two files, main.asm and test.ninc, their contents are:  
main.asm:  
```
#include <test.ninc>
code segment
assume cs:code,ds:data
start:
    mov ax,data
    mov ds,ax
    mov dx,offset string
    mov ah,9
    int 21h
    mov ah,4ch
    int 21h
code ends
end start
```
test.ninc:  
```
data segment
    string db 'Hello,World!$'
data ends
```
ASMP Will change main.asm to:
data segment
    string db 'Hello,World!$'
data ends
code segment
assume cs:code,ds:data
start:
    mov ax,data
    mov ds,ax
    mov dx,offset string
    mov ah,9
    int 21h
    mov ah,4ch
    int 21h
code ends
end start
```
Enjoy!
