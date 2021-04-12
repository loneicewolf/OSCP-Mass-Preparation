## Basic Scapy3 Usage
OS: Kali

Scapy Version: Version 2.4.4


### scapy3 as root:

"S and D as in Source and Destination"
```
S="127.0.0.1"
D="127.0.0.1"
MSG="Hello World"

send(IP(src=S,dst=D)/ICMP()/MSG)
send(IP(src=S,dst=D)/TCP()/MSG)
```
48656c6c6f20576f726c64 in DATA Captured using Wireshark:
Decode this as hex in bash

```
┌──(user)
└─# echo 48656c6c6f20576f726c64 | xxd -ps -r
Hello World
```

-------------------


[Example - At Stackoverflow](https://stackoverflow.com/questions/17971398/sending-packets-with-scapy-within-python-environment#17982399)

