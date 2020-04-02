import socket
import sys
import time


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("""FIEK UDP KLIENT
================================================================""")
serverName = input("Host: ")
serverPort = int(input("Port: "))   

print("""================================================================
Jeni lidhur ne serverin me host ""","|",serverName,"|"," ne portin ",serverPort)


while True:
    try:
        print("""================================================================
Shkruani me shkronja te medha komanden qe doni ta perdorni:               
\ IPADDRESS                                      
\ PORT                        
\ COUNT <HAPSIRE> <tekst>      
\ REVERSE <HAPSIRE> <tekst>                                                
\ PALINDROME <HAPSIRE> <tekst>                   
\ TIME                         
\ GAME
\ GCF <HAPSIRE> <NR1> <HAPSIRE> <NR2>   
\ CONVERT <HAPSIRE> Opcioni<cmToFeet,FeetToCm,kmToMiles,MileToKm> <HAPSIRE> <HAPSIRE> <NR>
\ CHANGE <HOST or PORT> <VALUE> ***WARNING YOU WILL BE DISCONNECTED FROM THE CURRENT SERVER*** 
\ MORSE-CODE <HAPSIRE> <ENCODE OR DECODE> <HAPSIRE> <tekst>      
Shkruaj \"EXIT\" per te ndaluar programi!           
               """)
        komandat = ["IPADDRESS","PORT","COUNT","REVERSE","PALINDROME","TIME","GAME","GCF","CONVERT","MORSE-CODE"]
        method = input("KOMANDA \\ ")
        if method.upper() == "EXIT":
            break
        elif method == '':
            print("Shkruani njeren nga komandat me siper!")
        elif method not in komandat:
            print("Komanda jo valide!")          
        else:
            clientSocket.sendto(str.encode(method),(serverName,serverPort))
            serverAnswerByte = clientSocket.recv(128)
            serverAnswer = serverAnswerByte.decode("utf-8")
            print(serverAnswer)
            print("Ju mund te jepni vetem nje komand.Tani serveri dhe klienti do mbyllen!")
            time.sleep(5)  
            sys.exit()     
    except TimeoutError:
        print("Serveri morri shume kohe per tu pergjigjur andaj lidhja u mbyll!")

 