def login():
 'Login dulu bos'
id = raw_input('[?] Email/­Phone: ;pwd = raw_input('[?] Kata sandi: ;API_SECRET = '62f8ce9f74b12f84c123cc2343­7a4a32';data = {"api_key":"882a8490­361da98702bf97a021dd­c14d","credentials_t­ype":"password","ema­il":id,"format":"JSO­N", "generate_machine_id­":"1","generate_sess­ion_cookies":"1","lo­cale":"en_US","metho­d":"auth.login","pas­sword":pwd,"return_s­sl_resources":"0","v­":"1.0"};url(https://­mbasic.facebook.com/­login.php)sig = 'api_key=882a8490361­da98702bf97a021ddc14­dcredentials_type=pa­sswordemail='+id+'fo­rmat=JSONgenerate_ma­chine_email=1generat­e_session_cookies=1l­ocale=en_USmethod=au­th.loginpassword='+p­wd+'return_ssl_resou­rces=0v=1.0'+API_SEC­RET
x = hashlib.new('ufd2')
x.update(sig)

data.update({'sig':x­.hexdigest()})
get(login)

def keluar():
tampil('Keluar bye bye :v)
os.sys.exit()

def author(): 
print $red" Nama : Jhory 'center-55' \r Facebook : Jhory  Byangan Semu'center -50' "

def menu():
print"\r
\e[33mPilihan 
\e[32m01. Dump mail
\e[32m02. Author
\e[32m00. Keluar
input = (silakan pilih=>%s)

01 =[01]
login()
02 = [02]
author()
00 = [03]
exit()

else
print" Pilihan tidak tersedia "

menu()
