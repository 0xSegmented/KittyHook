import os                   # IMPORTING
from sys import platform    # NEEDED
import requests             # MODULES

# Specify root location for your wordlists | FOR WINDOWS USE double \\ !!
wl = r'C:\\Users\\<EXAMPLE-USER>\\Documents\\wordlists\\'

# Function, checking if you are using Windows or Unix-ish
def machinetype():
    if platform != "win32":
        return 1
    else:
        return 2
if machinetype() != 1:
    ps = "powershell .\\"
    exe = ".exe"
else:
    ps = ""
    exe = ""

# FILL IN THE <BETWEEN>
def webhook(text):
    url = "https://api.telegram.org/bot<BOT-TOKEN>/sendMessage?chat_id=<CHAT-ID>="+text
    req = requests.post(url)
    print(req.text)

# This makes you a valid hacker
print("""
    __ __ _ __  __        __  __            __                                 
   / //_/(_) /_/ /___  __/ / / /___  ____  / /__                               
  / ,<  / / __/ __/ / / / /_/ / __ \/ __ \/ //_/                               
 / /| |/ / /_/ /_/ /_/ / __  / /_/ / /_/ / ,<                                  
/_/ |_/_/\__/\__/\__, /_/ /_/\____/\____/_/|_|                                 
 _______________/____/_______________________________________                  
/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_  __      __  __ 
   / /_  __  ___    /  |/  /___ _/ (_)____(_)___  __  ______| |/ /___ _/ /_/ /_
  / __ \/ / / (_)  / /|_/ / __ `/ / / ___/ / __ \/ / / / ___/   / __ `/ __/ __/
 / /_/ / /_/ /    / /  / / /_/ / / / /__/ / /_/ / /_/ (__  )   / /_/ / /_/ /_  
/_.___/\__, (_)  /_/  /_/\__,_/_/_/\___/_/\____/\__,_/____/_/|_\__,_/\__/\__/  
      /____/                                                                  
      """)

start = input('Do you want to start? Y or N\n') # Check if you want to run
if start.lower() != 'y':
    print("Bye")
    exit()
else: # Gonna run
    print("MAKE SURE THIS PROGRAM IS IN YOUR HASHCAT FILE LOCATION")
    print("""Choose out of:
    md5 = 0     
    SHA1 = 100
    NTLM = 1000
          """)
    hashtype = int(input('Enter hash type:\n'))
    hashpath = input('Enter hash path:\n')
    wordlist = wl+input(f"Enter wordlist path:\n{wl}")
    command = f"hashcat{exe} -m {hashtype} {hashpath} --wordlist {wordlist}"
    run = input(f'Do you want to run {command}?\nY or N\n')
    if run.lower() != 'y': # Check if you agree with the syntax
        choice = int(input("Make a choice:\n1: More wordlists\n2: Add extension\n3: Benchmark\n"))
        if choice in {1,2,3}: # You can finally make choices
            if choice == 1:
                wordlist2 = input("Enter second wordlist path\n")
                command1 = f"hashcat{exe} -m {hashtype} {hashpath} --wordlist {wordlist},{wordlist2}"
                runnie = input(f"Want to run {command1}?\nY or N\n")
                if runnie.lower() == "y":
                    os.system(f'{ps}{command1}')
                    webhook("Done+Cracking") # Returning the webhook, with text
                else:
                    ext = input("Add syntax\n")
                    command3 = f"{command1} {ext}"
                    run3 = input(f"Run: {command3}?\nY or N\n")
                    if run3 != "Y":
                        exit()
                    else:
                        os.system(f'{ps}{command3}')
                        webhook("Done+Cracking")
            elif choice == 2:
                ext = input(f"Add syntax\n{command}")
                command4 = f"{command} {ext}"
                run4 = input(f"Run: {command4}?\nY or N\n")
                if run4.lower() != "y":
                    exit()
                else:
                    os.system(f'{ps}{command4}')
                    webhook("Done+Cracking")
            elif choice == 3:
                command5 = f"hashcat{exe} -m 100 -b"
                print(f"{command5}")
                choice2 = input("Want to add more syntax?\nY or N\n")
                if choice2.lower() != "y":
                    os.system(f'{ps}{command5}')
                    webhook("Benchmark+Done")
                else:
                    syntax2 = input(f"Enter syntax:\n{command5}")
                    print(f"{command5}{syntax}")
                    check = input(f"is this correct?:\nY or N\n")
                    if check.lower() != "y":
                        exit()
                    else:
                        os.system(f'{ps}{command5}{syntax2}')
                        webhook("Benchmark+Done")
        else:
            print("Does not exist") # You did something wrong!
    else:
        os.system(f'{ps}{command}')
        webhook("Done+Cracking.")

print("""
♡ ♡ ♡ ♡ ♡ ♡ ♡
      """)
