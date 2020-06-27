import random
import string
import time
import sys

f = open('Nitro Codes.txt', 'a')
print(""" 


███╗   ██╗ █████╗ ████████╗██╗  ██╗ █████╗ ███╗   ██╗    ███╗   ██╗██╗████████╗██████╗  ██████╗ 
████╗  ██║██╔══██╗╚══██╔══╝██║  ██║██╔══██╗████╗  ██║    ████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗
██╔██╗ ██║███████║   ██║   ███████║███████║██╔██╗ ██║    ██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║
██║╚██╗██║██╔══██║   ██║   ██╔══██║██╔══██║██║╚██╗██║    ██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║
██║ ╚████║██║  ██║   ██║   ██║  ██║██║  ██║██║ ╚████║    ██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝
╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ 
                          ================================
                          Made by Nathan||#9965
                          https://github.com/NathanPrivate
                          ================================
                          
""")                        
print ('')
time.sleep(2)
print('How Many codes Should I Generate?')
print ('')
time.sleep(2)
amount = int(input(">"))
print ('')
time.sleep(2.5)
print ('Generating')
time.sleep(2.5)
print ('')

fix = 1
while fix <= amount:
    code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    discord_url = "https://discordapp.com/gifts/"
    f.write( code + '\n')
    discord_code = discord_url + code
    print('++Generated Code: ' + discord_code)
    fix += 1
time.sleep(2)
print ('')
print ('Now Check Codes In A Checker, Enjoy!:)')

