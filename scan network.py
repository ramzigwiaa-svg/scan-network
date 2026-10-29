import socket
ports=[80,443,22]
for port in ports:
    ip=input("entrer your ip:")
    resultat=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    status=resultat.connect_ex((ip,port))
    if status==0:
        print(f"sucssfull{resultat} {port}")
    else:
        print(f"failed {port}")
    resultat.close()
