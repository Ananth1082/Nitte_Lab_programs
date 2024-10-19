import random as rd
msg=input("Enter the message :")
packets = [[i//3,msg[i:(i+3) if i+3 < len(msg) else None]] for i in range(0,len(msg),3)]
print("packets :",packets)
rd.shuffle(packets)
print("shuffled packets: ",packets)
packets.sort(key=lambda a: a[0])
print("sorted packets: ",packets)