from python_mikrotik_login import MikrotikLogin

login = MikrotikLogin("guest","vue234","http://login.vue/login") #you can leave the unique key index empty or set it manually
login.do_login()
print(login) # to see status