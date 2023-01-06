import os
webhook = """https://api.telegram.org/bot<BOT-TOKEN>/sendMessage\?chat_id\=<CHAT-ID>\&text\=""" # This is your webhook that ends with text\=
start = input('Do you want to start? Y or N\n') # Check if you want to run
if start.lower() != 'y':
    print("Bye")
    exit()
else: # Gonna run
    print("""Choose out of:
    md5 = 0     
    SHA1 = 100
    NTLM = 1000
          """)
    hashtype = int(input('Enter hash type:\n'))
    hashpath = input('Enter hash path:\n')
    wordlist = input("Enter wordlist path:\n")
    command = f"hashcat -m {hashtype} {hashpath} --wordlist {wordlist}"
    run = input(f'Do you want to run {command}?\nY or N\n')
    if run.lower() != 'y': # Check if you agree with the syntax
        choice = int(input("Make a choice:\n1: More wordlists\n2: Add extension\n3: Benchmark\n"))
        if choice in {1,2,3}:
            if choice == 1:
                wordlist2 = input("Enter second wordlist path\n")
                command1 = f"hashcat -m {hashtype} {hashpath} --wordlist {wordlist},{wordlist2}"
                runnie = input(f"Want to run {command1}?\nY or N\n")
                if runnie == "y":
                    os.system(f'{command1}')
                    os.system(f'curl --noproxy -xPOST {webhook}Done+cracking.')
                else:
                    ext = input("Add syntax\n")
                    command3 = f"{command1} {ext}"
                    run3 = input(f"Run: {command3}?\nY or N\n")
                    if run3 != "Y":
                        exit()
                    else:
                        os.system(f'{command3}')
                        os.system(f'curl --noproxy -xPOST {webhook}Done+cracking.')
            elif choice == 2:
                ext = input("Add syntax\n")
                command4 = f"{command} {ext}"
                run4 = input(f"Run: {command4}?\nY or N\n")
                if run4 != "Y":
                    exit()
                else:
                    os.system(f'{command4}')
                    os.system(f'curl --noproxy -xPOST {webhook}Done+cracking.') 
            elif choice == 3:
                command5 = "hashcat -m 100 -b"
                print(f"{command5}")
                choice2 = input("Want to add more syntax?\nY or N\n")
                if choice2.lower() != "y":
                    os.system(f'{command5}')
                    os.system(f'curl --noproxy -xPOST {webhook}Benchmark+Done.')
                else:
                    syntax2 = input(f"Enter syntax:\n{command5}")
                    print(f"{command5}{syntax}")
                    check = input(f"is this correct?:\nY or N\n")
                    if check.lower() != "y":
                        exit()
                    else:
                        os.system(f'{command5}{syntax2}')
                        os.system(f'curl --noproxy -xPOST {webhook}Benchmark+Done.')
        else:
            print("Does not exist")
    else:
        os.system(f'{command}')
        os.system(f'curl --noproxy -xPOST {webhook}Done+cracking.')
