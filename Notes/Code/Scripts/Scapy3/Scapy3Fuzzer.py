# exec with (root)  scapy3 -c Scapy3Fuzzer.py

S=input("enter Src(ip): ")
D=input("enter Dst(ip): ")
MSG=input("Enter MSG(txt): ")

send(IP(src=S,dst=D)/ICMP()/MSG)
send(IP(src=S,dst=D)/TCP()/MSG)
