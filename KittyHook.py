import os                   # IMPORTING
from sys import platform    # NEEDED
import requests             # MODULES

# Specify root location for your wordlists | FOR WINDOWS USE double \\ !!
wl = r'/path/to/your/wordlist/root/directory'
hl = r'/path/to/your/hashlocations/root/directory'
output = " > output.txt"


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

def stat():
    if machinetype() == 2:
        return os.system('powershell type output.txt')
    else:
        return os.system('cat output.txt')

# FILL IN THE <BETWEEN>
def webhook(text):
    url = "https://api.telegram.org/bot<BOT-TOKEN>/sendMessage?chat_id=<CHAT-ID>&text="+text
    req = requests.post(url)
    print(req.text)

# Function to check if status was cracked of exhausted
def status():
    with open("output.txt", "r") as f:
        contents = f.read().strip()
        if "Cracked" in contents:
            return "Cracked"
        elif "Exhausted" in contents:
            return "Exhausted"
        else:
            return "Error"

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
0         = md5
10        = md5($pass.$salt)                                                          
20        = md5($salt.$pass)                                                          
30        = md5(utf16le($pass).$salt)                                                 
40        = md5($salt.utf16le($pass))                                                 
50        = HMAC-MD5 (key = $pass)                                                    
60        = HMAC-MD5 (key = $salt)                                                    
70        = md5(utf16le($pass))                                                       
100       = SHA1                                                                      
110       = sha1($pass.$salt)                                                         
120       = sha1($salt.$pass)                                                         
130       = sha1(utf16le($pass).$salt)                                                
140       = sha1($salt.utf16le($pass))                                                
150       = HMAC-SHA1 (key = $pass)                                                   
160       = HMAC-SHA1 (key = $salt)                                                   
170       = sha1(utf16le($pass))                                                      
200       = MySQL323                                                                  
300       = MySQL4.1/MySQL5                                                           
400       = phpass, WordPress (MD5),  Joomla (MD5)                                    
400       = phpass, phpBB3 (MD5)                                                      
500       = md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5) 2                               
501       = Juniper IVE                                                               
600       = BLAKE2b-512                                                               
610       = BLAKE2b-512($pass.$salt) *                                                
620       = BLAKE2b-512($salt.$pass) *                                                
900       = MD4                                                                       
1000      = NTLM                                                                      
1100      = Domain Cached Credentials (DCC), MS Cache                                 
1300      = SHA2-224                                                                  
1400      = SHA2-256                                                                  
1410      = sha256($pass.$salt)                                                       
1420      = sha256($salt.$pass)                                                       
1430      = sha256(utf16le($pass).$salt)                                              
1440      = sha256($salt.utf16le($pass))                                              
1450      = HMAC-SHA256 (key = $pass)                                                 
1460      = HMAC-SHA256 (key = $salt)                                                 
1470      = sha256(utf16le($pass))                                                    
1500      = descrypt, DES (Unix), Traditional DES                                     
1600      = Apache $apr1$ MD5, md5apr1, MD5 (APR) 2                                   
1700      = SHA2-512                                                                  
1710      = sha512($pass.$salt)                                                       
1720      = sha512($salt.$pass)                                                       
1730      = sha512(utf16le($pass).$salt)                                              
1740      = sha512($salt.utf16le($pass))                                              
1750      = HMAC-SHA512 (key = $pass)                                                 
1760      = HMAC-SHA512 (key = $salt)                                                 
1770      = sha512(utf16le($pass))                                                    
1800      = sha512crypt $6$, SHA512 (Unix) 2                                          
2000      = STDOUT                                                                    
2100      = Domain Cached Credentials 2 (DCC2), MS Cache 2                            
2400      = Cisco-PIX MD5                                                             
2410      = Cisco-ASA MD5                                                             
2500      = WPA-EAPOL-PBKDF2 1                                                        
2501      = WPA-EAPOL-PMK 14                                                          
2600      = md5(md5($pass))                                                           
3000      = LM                                                                        
3100      = Oracle H: Type (Oracle 7+)                                                
3200      = bcrypt $2*$, Blowfish (Unix)                                              
3500      = md5(md5(md5($pass)))                                                      
3710      = md5($salt.md5($pass))                                                     
3800      = md5($salt.$pass.$salt)                                                    
3910      = md5(md5($pass).md5($salt))                                                
4010      = md5($salt.md5($salt.$pass))                                               
4110      = md5($salt.md5($pass.$salt))                                               
4300      = md5(strtoupper(md5($pass)))                                               
4400      = md5(sha1($pass))                                                          
4410      = md5(sha1($pass).$salt) *                                                  
4500      = sha1(sha1($pass))                                                         
4510      = sha1(sha1($pass).$salt)                                                   
4520      = sha1($salt.sha1($pass))                                                   
4700      = sha1(md5($pass))                                                          
4710      = sha1(md5($pass).$salt)                                                    
4800      = iSCSI CHAP authentication, MD5(CHAP) 7                                    
4900      = sha1($salt.$pass.$salt)                                                   
5000      = sha1(sha1($salt.$pass.$salt))                                             
5100      = Half MD5                                                                  
5200      = Password Safe v3                                                          
5300      = IKE-PSK MD5                                                               
5400      = IKE-PSK SHA1                                                              
5500      = NetNTLMv1 / NetNTLMv1+ESS                                                 
5600      = NetNTLMv2                                                                 
5700      = Cisco-IOS type 4 (SHA256)                                                 
5800      = Samsung Android Password/PIN                                              
6000      = RIPEMD-160                                                                
6100      = Whirlpool                                                                 
6211      = TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + AES (legacy)                       
6211      = TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Serpent (legacy)                   
6211      = TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Twofish (legacy)                   
6212      = TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + AES-Twofish (legacy)               
6213      = TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + AES-Twofish-Serpent (legacy)       
6212      = TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Serpent-AES (legacy)               
6213      = TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Serpent-Twofish-AES (legacy)       
6212      = TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Twofish-Serpent (legacy)           
6221      = TrueCrypt 5.0+ SHA512 + AES (legacy)                                      
6221      = TrueCrypt 5.0+ SHA512 + Serpent (legacy)                                  
6221      = TrueCrypt 5.0+ SHA512 + Twofish (legacy)                                  
6222      = TrueCrypt 5.0+ SHA512 + AES-Twofish (legacy)                              
6223      = TrueCrypt 5.0+ SHA512 + AES-Twofish-Serpent (legacy)                      
6222      = TrueCrypt 5.0+ SHA512 + Serpent-AES (legacy)                              
6223      = TrueCrypt 5.0+ SHA512 + Serpent-Twofish-AES (legacy)                      
6222      = TrueCrypt 5.0+ SHA512 + Twofish-Serpent (legacy)                          
6231      = TrueCrypt 5.0+ Whirlpool + AES (legacy)                                   
6231      = TrueCrypt 5.0+ Whirlpool + Serpent (legacy)                               
6231      = TrueCrypt 5.0+ Whirlpool + Twofish (legacy)                               
6232      = TrueCrypt 5.0+ Whirlpool + AES-Twofish (legacy)                           
6233      = TrueCrypt 5.0+ Whirlpool + AES-Twofish-Serpent (legacy)                   
6232      = TrueCrypt 5.0+ Whirlpool + Serpent-AES (legacy)                           
6233      = TrueCrypt 5.0+ Whirlpool + Serpent-Twofish-AES (legacy)                   
6232      = TrueCrypt 5.0+ Whirlpool + Twofish-Serpent (legacy)                       
6241      = TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + AES + boot (legacy)                
6241      = TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Serpent + boot (legacy)            
6241      = TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Twofish + boot (legacy)            
6242      = TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + AES-Twofish + boot (legacy)        
6243      = TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + AES-Twofish-Serpent + boot (legacy)
6242      = TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Serpent-AES + boot (legacy)        
6243      = TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Serpent-Twofish-AES + boot (legacy)
6242      = TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Twofish-Serpent + boot (legacy)    
6300      = AIX {smd5}                                                                
6400      = AIX {ssha256}                                                             
6500      = AIX {ssha512}                                                             
6600      = 1Password, agilekeychain                                                  
6700      = AIX {ssha1}                                                               
6800      = LastPass + LastPass sniffed4                                              
6900      = GOST R 34.11-94                                                           
7000      = FortiGate (FortiOS)                                                       
7200      = GRUB 2                                                                    
7300      = IPMI2 RAKP HMAC-SHA1                                                      
7400      = sha256crypt $5$, SHA256 (Unix) 2                                          
7500      = Kerberos 5, etype 23, AS-REQ Pre-Auth                                     
7700      = SAP CODVN B (BCODE)                                                       
7701      = SAP CODVN B (BCODE) from RFC_READ_TABLE                                   
7800      = SAP CODVN F/G (PASSCODE)                                                  
7801      = SAP CODVN F/G (PASSCODE) from RFC_READ_TABLE                              
7900      = Drupal7                                                                   
8000      = Sybase ASE                                                                
8100      = Citrix NetScaler (SHA1)                                                   
8200      = 1Password, cloudkeychain                                                  
8300      = DNSSEC (NSEC3)                                                            
8400      = WBB3 (Woltlab Burning Board)                                              
8500      = RACF                                                                      
8600      = Lotus Notes/Domino 5                                                      
8700      = Lotus Notes/Domino 6                                                      
8800      = Android FDE <= 4.3                                                        
8900      = scrypt                                                                    
9000      = Password Safe v2                                                          
9100      = Lotus Notes/Domino 8                                                      
9200      = Cisco-IOS $8$ (PBKDF2-SHA256)                                             
9300      = Cisco-IOS $9$ (scrypt)                                                    
9400      = MS Office 2007                                                            
9500      = MS Office 2010                                                            
9600      = MS Office 2013                                                            
9700      = MS Office ⇐ 2003 MD5 + RC4, oldoffice$0, oldoffice$1                      
9710      = MS Office ⇐ 2003 $0/$1, MD5 + RC4, collider #1 23                         
9720      = MS Office ⇐ 2003 $0/$1, MD5 + RC4, collider #2                            
9800      = MS Office ⇐ 2003 SHA1 + RC4, oldoffice$3, oldoffice$4                     
9810      = MS Office ⇐ 2003 $3, SHA1 + RC4, collider #1 24                           
9820      = MS Office ⇐ 2003 $3, SHA1 + RC4, collider #2                              
9900      = Radmin2                                                                   
10000     = Django (PBKDF2-SHA256)                                                    
10100     = SipHash                                                                   
10200     = CRAM-MD5                                                                  
10300     = SAP CODVN H (PWDSALTEDHASH) iSSHA-1                                       
10400     = PDF 1.1 - 1.3 (Acrobat 2 - 4)                                             
10410     = PDF 1.1 - 1.3 (Acrobat 2 - 4), collider #1 25                             
10420     = PDF 1.1 - 1.3 (Acrobat 2 - 4), collider #2                                
10500     = PDF 1.4 - 1.6 (Acrobat 5 - 8)                                             
10600     = PDF 1.7 Level 3 (Acrobat 9)                                               
10700     = PDF 1.7 Level 8 (Acrobat 10 - 11)                                         
10800     = SHA2-384                                                                  
10810     = sha384($pass.$salt)                                                       
10820     = sha384($salt.$pass)                                                       
10830     = sha384(utf16le($pass).$salt)                                              
10840     = sha384($salt.utf16le($pass))                                              
10870     = sha384(utf16le($pass))                                                    
10900     = PBKDF2-HMAC-SHA256                                                        
10901     = RedHat 389-DS LDAP (PBKDF2-HMAC-SHA256)                                   
11000     = PrestaShop                                                                
11100     = PostgreSQL CRAM (MD5)                                                     
11200     = MySQL CRAM (SHA1)                                                         
11300     = Bitcoin/Litecoin wallet.dat                                               
11400     = SIP digest authentication (MD5)                                           
11500     = CRC32 5                                                                   
11600     = 7-Zip                                                                     
11700     = GOST R 34.11-2012 (Streebog) 256-bit, big-endian                          
11750     = HMAC-Streebog-256 (key = $pass), big-endian                               
11760     = HMAC-Streebog-256 (key = $salt), big-endian                               
11800     = GOST R 34.11-2012 (Streebog) 512-bit, big-endian                          
11850     = HMAC-Streebog-512 (key = $pass), big-endian                               
11860     = HMAC-Streebog-512 (key = $salt), big-endian                               
11900     = PBKDF2-HMAC-MD5                                                           
12000     = PBKDF2-HMAC-SHA1                                                          
12100     = PBKDF2-HMAC-SHA512                                                        
12200     = eCryptfs                                                                  
12300     = Oracle T: Type (Oracle 12+)                                               
12400     = BSDi Crypt, Extended DES                                                  
12500     = RAR3-hp                                                                   
12600     = ColdFusion 10+                                                            
12700     = Blockchain, My Wallet                                                     
12800     = MS-AzureSync PBKDF2-HMAC-SHA256                                           
12900     = Android FDE (Samsung DEK)                                                 
13000     = RAR5                                                                      
13100     = Kerberos 5, etype 23, TGS-REP                                             
13200     = AxCrypt 1                                                                 
13300     = AxCrypt 1 in-memory SHA1 13                                               
13400     = KeePass 1 AES / without keyfile                                           
13400     = KeePass 2 AES / without keyfile                                           
13400     = KeePass 1 Twofish / with keyfile                                          
13400     = Keepass 2 AES / with keyfile                                              
13500     = PeopleSoft PS_TOKEN                                                       
13600     = WinZip                                                                    
13711     = VeraCrypt PBKDF2-HMAC-RIPEMD160 + AES (legacy)                            
13712     = VeraCrypt PBKDF2-HMAC-RIPEMD160 + AES-Twofish (legacy)                    
13711     = VeraCrypt PBKDF2-HMAC-RIPEMD160 + Serpent (legacy)                        
13712     = VeraCrypt PBKDF2-HMAC-RIPEMD160 + Serpent-AES (legacy)                    
13713     = VeraCrypt PBKDF2-HMAC-RIPEMD160 + Serpent-Twofish-AES (legacy)            
13711     = VeraCrypt PBKDF2-HMAC-RIPEMD160 + Twofish (legacy)                        
13712     = VeraCrypt PBKDF2-HMAC-RIPEMD160 + Twofish-Serpent (legacy)                
13751     = VeraCrypt PBKDF2-HMAC-SHA256 + AES (legacy)                               
13752     = VeraCrypt PBKDF2-HMAC-SHA256 + AES-Twofish (legacy)                       
13751     = VeraCrypt PBKDF2-HMAC-SHA256 + Serpent (legacy)                           
13752     = VeraCrypt PBKDF2-HMAC-SHA256 + Serpent-AES (legacy)                       
13753     = VeraCrypt PBKDF2-HMAC-SHA256 + Serpent-Twofish-AES (legacy)               
13751     = VeraCrypt PBKDF2-HMAC-SHA256 + Twofish (legacy)                           
13752     = VeraCrypt PBKDF2-HMAC-SHA256 + Twofish-Serpent (legacy)                   
13721     = VeraCrypt PBKDF2-HMAC-SHA512 + AES (legacy)                               
13722     = VeraCrypt PBKDF2-HMAC-SHA512 + AES-Twofish (legacy)                       
13721     = VeraCrypt PBKDF2-HMAC-SHA512 + Serpent (legacy)                           
13722     = VeraCrypt PBKDF2-HMAC-SHA512 + Serpent-AES (legacy)                       
13723     = VeraCrypt PBKDF2-HMAC-SHA512 + Serpent-Twofish-AES (legacy)               
13721     = VeraCrypt PBKDF2-HMAC-SHA512 + Twofish (legacy)                           
13722     = VeraCrypt PBKDF2-HMAC-SHA512 + Twofish-Serpent (legacy)                   
13731     = VeraCrypt PBKDF2-HMAC-Whirlpool + AES (legacy)                            
13732     = VeraCrypt PBKDF2-HMAC-Whirlpool + AES-Twofish (legacy)                    
13731     = VeraCrypt PBKDF2-HMAC-Whirlpool + Serpent (legacy)                        
13732     = VeraCrypt PBKDF2-HMAC-Whirlpool + Serpent-AES (legacy)                    
13733     = VeraCrypt PBKDF2-HMAC-Whirlpool + Serpent-Twofish-AES (legacy)            
13731     = VeraCrypt PBKDF2-HMAC-Whirlpool + Twofish (legacy)                        
13732     = VeraCrypt PBKDF2-HMAC-Whirlpool + Twofish-Serpent (legacy)                
13741     = VeraCrypt PBKDF2-HMAC-RIPEMD160 + boot-mode + AES (legacy)                
13742     = VeraCrypt PBKDF2-HMAC-RIPEMD160 + boot-mode + AES-Twofish (legacy)        
13743     = VeraCrypt PBKDF2-HMAC-RIPEMD160 + boot-mode + AES-Twofish-Serpent (legacy)
13761     = VeraCrypt PBKDF2-HMAC-SHA256 + boot-mode + Twofish (legacy)               
13762     = VeraCrypt PBKDF2-HMAC-SHA256 + boot-mode + Serpent-AES (legacy)           
13763     = VeraCrypt PBKDF2-HMAC-SHA256 + boot-mode + Serpent-Twofish-AES (legacy)   
13761     = VeraCrypt PBKDF2-HMAC-SHA256 + boot-mode + PIM + AES 16 (legacy)          
13771     = VeraCrypt Streebog-512 + XTS 512 bit (legacy)                             
13772     = VeraCrypt Streebog-512 + XTS 1024 bit (legacy)                            
13773     = VeraCrypt Streebog-512 + XTS 1536 bit (legacy)                            
13781     = VeraCrypt Streebog-512 + XTS 512 bit + boot-mode (legacy)                 
13782     = VeraCrypt Streebog-512 + XTS 1024 bit + boot-mode (legacy)                
13783     = VeraCrypt Streebog-512 + XTS 1536 bit + boot-mode (legacy)                
13800     = Windows Phone 8+ PIN/password                                             
13900     = OpenCart                                                                  
14000     = DES (PT = $salt, key = $pass) 8                                           
14100     = 3DES (PT = $salt, key = $pass) 9                                          
14400     = sha1(CX)                                                                  
14500     = Linux Kernel Crypto API (2.4)                                             
14600     = LUKS v1 (legacy) 10                                                       
14700     = iTunes backup < 10.0 11                                                   
14800     = iTunes backup >= 10.0 11                                                  
14900     = Skip32 (PT = $salt, key = $pass) 12                                       
15000     = FileZilla Server >= 0.9.55                                                
15100     = Juniper/NetBSD sha1crypt                                                  
15200     = Blockchain, My Wallet, V2                                                 
15300     = DPAPI masterkey file v1 + local context                                   
15310     = DPAPI masterkey file v1 (context 3) *                                     
15400     = ChaCha20 20                                                               
15500     = JKS Java Key Store Private Keys (SHA1)                                    
15600     = Ethereum Wallet, PBKDF2-HMAC-SHA256                                       
15700     = Ethereum Wallet, SCRYPT                                                   
15900     = DPAPI masterkey file v2 + Active Directory domain context                 
15910     = DPAPI masterkey file v2 (context 3) *                                     
16000     = Tripcode                                                                  
16100     = TACACS+                                                                   
16200     = Apple Secure Notes                                                        
16300     = Ethereum Pre-Sale Wallet, PBKDF2-HMAC-SHA256                              
16400     = CRAM-MD5 Dovecot                                                          
16500     = JWT (JSON Web Token)                                                      
16600     = Electrum Wallet (Salt-Type 1-3)                                           
16700     = FileVault 2                                                               
16800     = WPA-PMKID-PBKDF2 1                                                        
16801     = WPA-PMKID-PMK 15                                                          
16900     = Ansible Vault                                                             
17010     = GPG (AES-128/AES-256 (SHA-1($pass)))                                      
17200     = PKZIP (Compressed)                                                        
17210     = PKZIP (Uncompressed)                                                      
17220     = PKZIP (Compressed Multi-File)                                             
17225     = PKZIP (Mixed Multi-File)                                                  
17230     = PKZIP (Mixed Multi-File Checksum-Only)                                    
17300     = SHA3-224                                                                  
17400     = SHA3-256                                                                  
17500     = SHA3-384                                                                  
17600     = SHA3-512                                                                  
17700     = Keccak-224                                                                
17800     = Keccak-256                                                                
17900     = Keccak-384                                                                
18000     = Keccak-512                                                                
18100     = TOTP (HMAC-SHA1)                                                          
18200     = Kerberos 5, etype 23, AS-REP                                              
18300     = Apple File System (APFS)                                                  
18400     = Open Document Format (ODF) 1.2 (SHA-256, AES)                             
18500     = sha1(md5(md5($pass)))                                                     
18600     = Open Document Format (ODF) 1.1 (SHA-1, Blowfish)                          
18700     = Java Object hashCode()                                                    
18800     = Blockchain, My Wallet, Second Password (SHA256)                           
18900     = Android Backup                                                            
19000     = QNX /etc/shadow (MD5)                                                     
19100     = QNX /etc/shadow (SHA256)                                                  
19200     = QNX /etc/shadow (SHA512)                                                  
19300     = sha1($salt1.$pass.$salt2)                                                 
19500     = Ruby on Rails Restful-Authentication                                      
19600     = Kerberos 5, etype 17, TGS-REP (AES128-CTS-HMAC-SHA1-96)                   
19700     = Kerberos 5, etype 18, TGS-REP (AES256-CTS-HMAC-SHA1-96)                   
19800     = Kerberos 5, etype 17, Pre-Auth                                            
19900     = Kerberos 5, etype 18, Pre-Auth                                            
20011     = DiskCryptor SHA512 + XTS 512 bit (AES)                                    
20011     = DiskCryptor SHA512 + XTS 512 bit (Twofish)                                
20011     = DiskCryptor SHA512 + XTS 512 bit (Serpent)                                
20012     = DiskCryptor SHA512 + XTS 1024 bit (AES-Twofish)                           
20012     = DiskCryptor SHA512 + XTS 1024 bit (Twofish-Serpent)                       
20012     = DiskCryptor SHA512 + XTS 1024 bit (Serpent-AES)                           
20013     = DiskCryptor SHA512 + XTS 1536 bit (AES-Twofish-Serpent)                   
20200     = Python passlib pbkdf2-sha512                                              
20300     = Python passlib pbkdf2-sha256                                              
20400     = Python passlib pbkdf2-sha1                                                
20500     = PKZIP Master Key                                                          
20510     = PKZIP Master Key (6 byte optimization) 17                                 
20600     = Oracle Transportation Management (SHA256)                                 
20710     = sha256(sha256($pass).$salt)                                               
20720     = sha256($salt.sha256($pass))                                               
20800     = sha256(md5($pass))                                                        
20900     = md5(sha1($pass).md5($pass).sha1($pass))                                   
21000     = BitShares v0.x - sha512(sha512_bin(pass))                                 
21100     = sha1(md5($pass.$salt))                                                    
21200     = md5(sha1($salt).md5($pass))                                               
21300     = md5($salt.sha1($salt.$pass))                                              
21400     = sha256(sha256_bin($pass))                                                 
21420     = sha256($salt.sha256_bin($pass)) *                                         
21500     = SolarWinds Orion                                                          
21501     = SolarWinds Orion v2                                                       
21600     = Web2py pbkdf2-sha512                                                      
21700     = Electrum Wallet (Salt-Type 4)                                             
21800     = Electrum Wallet (Salt-Type 5)                                             
22000     = WPA-PBKDF2-PMKID+EAPOL 1                                                  
22000     = WPA-PBKDF2-PMKID+EAPOL 1                                                  
22001     = WPA-PMK-PMKID+EAPOL 18                                                    
22100     = BitLocker                                                                 
22200     = Citrix NetScaler (SHA512)                                                 
22300     = sha256($salt.$pass.$salt)                                                 
22400     = AES Crypt (SHA256)                                                        
22500     = MultiBit Classic .key (MD5)                                               
22600     = Telegram Desktop < v2.1.14 (PBKDF2-HMAC-SHA1)                             
22700     = MultiBit HD (scrypt)                                                      
22911     = RSA/DSA/EC/OpenSSH Private Keys ($0$)                                     
22921     = RSA/DSA/EC/OpenSSH Private Keys ($6$)                                     
22931     = RSA/DSA/EC/OpenSSH Private Keys ($1, $3$)                                 
22941     = RSA/DSA/EC/OpenSSH Private Keys ($4$)                                     
22951     = RSA/DSA/EC/OpenSSH Private Keys ($5$)                                     
23001     = SecureZIP AES-128                                                         
23002     = SecureZIP AES-192                                                         
23003     = SecureZIP AES-256                                                         
23100     = Apple Keychain                                                            
23200     = XMPP SCRAM PBKDF2-SHA1                                                    
23300     = Apple iWork                                                               
23400     = Bitwarden                                                                 
23500     = AxCrypt 2 AES-128                                                         
23600     = AxCrypt 2 AES-256                                                         
23700     = RAR3-p (Uncompressed)                                                     
23800     = RAR3-p (Compressed)                                                       
23900     = BestCrypt v3 Volume Encryption                                            
24100     = MongoDB ServerKey SCRAM-SHA-1                                             
24200     = MongoDB ServerKey SCRAM-SHA-256                                           
24300     = sha1($salt.sha1($pass.$salt))                                             
24410     = PKCS#8 Private Keys (PBKDF2-HMAC-SHA1 + 3DES/AES)                         
24420     = PKCS#8 Private Keys (PBKDF2-HMAC-SHA256 + 3DES/AES)                       
24500     = Telegram Desktop >= v2.1.14 (PBKDF2-HMAC-SHA512)                          
24600     = SQLCipher                                                                 
24700     = Stuffit5                                                                  
24800     = Umbraco HMAC-SHA1                                                         
24900     = Dahua Authentication MD5                                                  
25000     = SNMPv3 HMAC-MD5-96/HMAC-SHA1-96 8                                         
25100     = SNMPv3 HMAC-MD5-96 8                                                      
25200     = SNMPv3 HMAC-SHA1-96 8                                                     
25300     = MS Office 2016 - SheetProtection                                          
25400     = PDF 1.4 - 1.6 (Acrobat 5 - 8) - user and owner pass                       
25500     = Stargazer Stellar Wallet XLM                                              
25600     = bcrypt(md5($pass)) / bcryptmd5                                            
25700     = MurmurHash                                                                
25800     = bcrypt(sha1($pass)) / bcryptsha1                                          
25900     = KNX IP Secure - Device Authentication Code                                
26000     = Mozilla key3.db                                                           
26100     = Mozilla key4.db                                                           
26200     = OpenEdge Progress Encode                                                  
26300     = FortiGate256 (FortiOS256)                                                 
26401     = AES-128-ECB NOKDF (PT = $salt, key = $pass)                               
26402     = AES-192-ECB NOKDF (PT = $salt, key = $pass)                               
26403     = AES-256-ECB NOKDF (PT = $salt, key = $pass)                               
26500     = iPhone passcode (UID key + System Keybag)                                 
26600     = MetaMask Wallet 8                                                         
26700     = SNMPv3 HMAC-SHA224-128 8                                                  
26800     = SNMPv3 HMAC-SHA256-192 8 8                                                
26900     = SNMPv3 HMAC-SHA384-256 8                                                  
27000     = NetNTLMv1 / NetNTLMv1+ESS (NT) 22                                         
27100     = NetNTLMv2 (NT) 22                                                         
27200     = Ruby on Rails Restful Auth (one round, no sitekey)                        
27300     = SNMPv3 HMAC-SHA512-384 8                                                  
27400     = VMware VMX (PBKDF2-HMAC-SHA1 + AES-256-CBC)                               
27500     = VirtualBox (PBKDF2-HMAC-SHA256 & AES-128-XTS)                             
27600     = VirtualBox (PBKDF2-HMAC-SHA256 & AES-256-XTS)                             
27700     = MultiBit Classic .wallet (scrypt)                                         
27800     = MurmurHash3                                                               
27900     = CRC32C                                                                    
28000     = CRC64Jones                                                                
28100     = Windows Hello PIN/Password                                                
28200     = Exodus Desktop Wallet (scrypt) *                                          
28300     = Teamspeak 3 (channel hash) *                                              
28400     = bcrypt(sha512($pass)) / bcryptsha512 *                                    
28501     = Bitcoin WIF private key (P2PKH), compressed 26*                           
28502     = Bitcoin WIF private key (P2PKH), uncompressed 27*                         
28503     = Bitcoin WIF private key (P2WPKH, Bech32), compressed 28*                  
28504     = Bitcoin WIF private key (P2WPKH, Bech32), uncompressed 29*                
28505     = Bitcoin WIF private key (P2SH(P2WPKH)), compressed 30*                    
28506     = Bitcoin WIF private key (P2SH(P2WPKH)), uncompressed 31*                  
28600     = PostgreSQL SCRAM-SHA-256 *                                                
28700     = Amazon AWS4-HMAC-SHA256 *                                                 
28800     = Kerberos 5, etype 17, DB *                                                
28900     = Kerberos 5, etype 18, DB *                                                
29000     = sha1($salt.sha1(utf16le($username).':'.utf16le($pass))) *                 
29100     = Flask Session Cookie ($salt.$salt.$pass) *                                
29200     = Radmin3 *                                                                 
29311     = TrueCrypt RIPEMD160 + XTS 512 bit *                                       
29312     = TrueCrypt RIPEMD160 + XTS 1024 bit *                                      
29313     = TrueCrypt RIPEMD160 + XTS 1536 bit *                                      
29321     = TrueCrypt SHA512 + XTS 512 bit *                                          
29322     = TrueCrypt SHA512 + XTS 1024 bit *                                         
29323     = TrueCrypt SHA512 + XTS 1536 bit *                                         
29331     = TrueCrypt Whirlpool + XTS 512 bit *                                       
29332     = TrueCrypt Whirlpool + XTS 1024 bit *                                      
29333     = TrueCrypt Whirlpool + XTS 1536 bit *                                      
29341     = TrueCrypt RIPEMD160 + XTS 512 bit + boot-mode *                           
29342     = TrueCrypt RIPEMD160 + XTS 1024 bit + boot-mode *                          
29343     = TrueCrypt RIPEMD160 + XTS 1536 bit + boot-mode *                          
29411     = VeraCrypt RIPEMD160 + XTS 512 bit *                                       
29412     = VeraCrypt RIPEMD160 + XTS 1024 bit *                                      
29413     = VeraCrypt RIPEMD160 + XTS 1536 bit *                                      
29421     = VeraCrypt SHA512 + XTS 512 bit *                                          
29422     = VeraCrypt SHA512 + XTS 1024 bit *                                         
29423     = VeraCrypt SHA512 + XTS 1536 bit *                                         
29431     = VeraCrypt Whirlpool + XTS 512 bit *                                       
29432     = VeraCrypt Whirlpool + XTS 1024 bit *                                      
29433     = VeraCrypt Whirlpool + XTS 1536 bit *                                      
29441     = VeraCrypt RIPEMD160 + XTS 512 bit + boot-mode *                           
29442     = VeraCrypt RIPEMD160 + XTS 1024 bit + boot-mode *                          
29443     = VeraCrypt RIPEMD160 + XTS 1536 bit + boot-mode *                          
29451     = VeraCrypt SHA256 + XTS 512 bit *                                          
29452     = VeraCrypt SHA256 + XTS 1024 bit *                                         
29453     = VeraCrypt SHA256 + XTS 1536 bit *                                         
29461     = VeraCrypt SHA256 + XTS 512 bit + boot-mode *                              
29462     = VeraCrypt SHA256 + XTS 1024 bit + boot-mode *                             
29463     = VeraCrypt SHA256 + XTS 1536 bit + boot-mode *                             
29471     = VeraCrypt Streebog-512 + XTS 512 bit *                                    
29472     = VeraCrypt Streebog-512 + XTS 1024 bit *                                   
29473     = VeraCrypt Streebog-512 + XTS 1536 bit *                                   
29481     = VeraCrypt Streebog-512 + XTS 512 bit + boot-mode *                        
29482     = VeraCrypt Streebog-512 + XTS 1024 bit + boot-mode *                       
29483     = VeraCrypt Streebog-512 + XTS 1536 bit + boot-mode *                       
29511     = LUKS v1 SHA-1 + AES *                                                     
29512     = LUKS v1 SHA-1 + Serpent *                                                 
29513     = LUKS v1 SHA-1 + Twofish *                                                 
29521     = LUKS v1 SHA-256 + AES *                                                   
29522     = LUKS v1 SHA-256 + Serpent *                                               
29523     = LUKS v1 SHA-256 + Twofish *                                               
29531     = LUKS v1 SHA-512 + AES *                                                   
29532     = LUKS v1 SHA-512 + Serpent *                                               
29533     = LUKS v1 SHA-512 + Twofish *                                               
29541     = LUKS v1 RIPEMD-160 + AES *                                                
29542     = LUKS v1 RIPEMD-160 + Serpent *                                            
29543     = LUKS v1 RIPEMD-160 + Twofish *                                            
29700     = KeePass 1 (AES/Twofish) and KeePass 2 (AES) - keyfile only mode           
30000     = Python Werkzeug MD5 (HMAC-MD5 (key = $salt)) *                            
30120     = Python Werkzeug SHA256 (HMAC-SHA256 (key = $salt)) *                      
30700     = Anope IRC Services (enc_sha256) *                                         
99999     = Plaintext                                                                                                                                
11        = Joomla < 2.5.18                                                           
12        = PostgreSQL                                                                
21        = osCommerce, xt:Commerce                                                   
22        = Juniper NetScreen/SSG (ScreenOS)                                          
23        = Skype                                                                     
24        = SolarWinds Serv-U                                                         
101       = nsldap, SHA-1(Base64), Netscape LDAP SHA                                  
111       = nsldaps, SSHA-1(Base64), Netscape LDAP SSHA                               
112       = Oracle S: Type (Oracle 11+)                                               
121       = SMF (Simple Machines Forum) > v1.1                                        
122       = macOS v10.4, macOS v10.5, macOS v10.6                                     
124       = Django (SHA-1)                                                            
125       = ArubaOS                                                                   
131       = MSSQL (2000)                                                              
132       = MSSQL (2005)                                                              
133       = PeopleSoft                                                                
141       = Episerver 6.x < .NET 4                                                    
1411      = SSHA-256(Base64), LDAP {SSHA256}                                          
1421      = hMailServer                                                               
1441      = Episerver 6.x >= .NET 4                                                   
1711      = SSHA-512(Base64), LDAP {SSHA512}                                          
1722      = macOS v10.7                                                               
1731      = MSSQL (2012, 2014)                                                        
2611      = vBulletin < v3.8.5                                                        
2612      = PHPS                                                                      
2711      = vBulletin >= v3.8.5                                                       
2811      = MyBB 1.2+, IPB2+ (Invision Power Board)                                   
3711      = MediaWiki B type                                                          
4521      = Redmine                                                                   
4522      = PunBB                                                                     
4711      = Huawei sha1(md5($pass).$salt)                                             
7100      = macOS v10.8+ (PBKDF2-SHA512)                                              
7401      = MySQL $A$ (sha256crypt) 19                                                
12001     = Atlassian (PBKDF2-HMAC-SHA1)                                              
20711     = AuthMe sha256                                                             
22301     = Telegram Mobile App Passcode (SHA256)                                     
Hash-Mode = Hash-Name                                                                 
123       = EPi                                                                       
190       = sha1(LinkedIn) 2                                                          
1431      = base64(sha256(unicode($pass))) 1                                          
3300      = MD5(Sun) 1                                                                
3610      = md5(md5($salt).$pass) 1                                                   
3720      = md5($pass.md5($salt)) 1                                                   
3721      = WebEdition CMS 1                                                          
4210      = md5($username.0.$pass) 1                                                  
4600      = sha1(sha1(sha1($pass))) 1                                                                                                                  
5000      = SHA-3 (Keccak)                                                            
          """)
    hashtype = int(input('Enter hash type:\n'))
    hashpath = hl+input(f'Enter hash path:\n{hl}')
    wordlist = wl+input(f"Enter wordlist path:\n{wl}")
    command = f"hashcat{exe} -m {hashtype} {hashpath} --wordlist {wordlist}"
    run = input(f'Do you want to run {command}?\nY or N\n')
    if run.lower() != 'y': # Check if you agree with the syntax
        choice = int(input("Make a choice:\n1: More wordlists\n2: Add extension\n3: Benchmark\n4: Free Style\n"))
        if choice in {1,2,3}: # You can finally make choices
            if choice == 1:
                wordlist2 = input("Enter second wordlist path\n")
                command1 = f"hashcat{exe} -m {hashtype} {hashpath} --wordlist {wordlist} {wordlist2}"
                runnie = input(f"Want to run {command1}?\nY or N\n")
                if runnie.lower() == "y":
                    os.system(f'{ps}{command1}{output}')
                    webhook("Done.") # Returning the webhook, with text
                    result = status()
                    webhook(f"Status: {result}")
                    stat()
                else:
                    ext = input("Add syntax\n")
                    command3 = f"{command1} {ext}"
                    run3 = input(f"Run: {command3}?\nY or N\n")
                    if run3 != "Y":
                        exit()
                    else:
                        os.system(f'{ps}{command3}{output}')
                        result = status()
                        webhook("Done.")
                        webhook(f"Status: {result}")
                        stat()
            elif choice == 2:
                ext = input(f"Add syntax\n{command}")
                command4 = f"{command} {ext}"
                run4 = input(f"Run: {command4}?\nY or N\n")
                if run4.lower() != "y":
                    exit()
                else:
                    os.system(f'{ps}{command4}{output}')
                    result = status()
                    webhook("Done.")
                    webhook(f"Status: {result}")
                    stat()
            elif choice == 3:
                command5 = f"hashcat{exe} -m 100 -b"
                print(f"{command5}")
                choice2 = input("Want to add more syntax?\nY or N\n")
                if choice2.lower() != "y":
                    os.system(f'{ps}{command5}{output}')
                    webhook("Benchmark+Done")
                    stat()
                else:
                    syntax2 = input(f"Enter syntax:\n{command5}")
                    print(f"{command5}{syntax}")
                    check = input(f"is this correct?:\nY or N\n")
                    if check.lower() != "y":
                        exit()
                    else:
                        os.system(f'{ps}{command5}{syntax2}{output}')
                        webhook("Benchmark+Done")
                        stat()
            elif choice == 4:
                freestyle = input("Write your hashcat syntax:\n")
                choice4 = input(f"Run it?\n{freestyle}\n")
                if choice4.lower() != "y":
                    exit()
                else:
                    os.system(f'{ps}{freestyle}{output}')
                    result = status()
                    webhook("Done.")
                    webhook(f"Status: {result}")
                    stat()
        else:
            print("Does not exist") # You did something wrong!
    else: 
        os.system(f'{ps}{command}{output}')    
        result = status()
        webhook("Done.")
        webhook(f"Status: {result}")
        stat()
        

print("""
♡ ♡ ♡ ♡ ♡ ♡ ♡
      """)
