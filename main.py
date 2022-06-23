class Account:
    def __init__(self):
        self.account = [{"account":"","password":"", "balance":0}]
    def signup(self,name,password):
        for obj in self.account:
            if name == obj["account"]:
                return False     
        self.account.append({"account":name,"password":password, "balance":0})
        return True
    def signin(self,name,password):
        for objs in self.account:
            if name == objs["account"] and password == objs["password"]:
                return True
        return False
    def balance(self,name):
        for c in self.account:
            if name == c["account"]:
                return c["balance"]
        return "noperson"
    def deposit(self,named,valued):
        for a in self.account:
            if named == a["account"]:
                a["balance"]=a["balance"]+int(valued)
                return a["account"]
        return False
    def withdrawal(self,value):
        for b in self.account:
            if name == b["account"] and int(value) <= b["balance"]:
                b["balance"]=b["balance"]-int(value)
                return b["balance"]
        return "no"
process=True
accounts=Account()
while process==True:
    options1=input("主選單，請選擇-1(註冊)/2(登入):")
    if options1=="1":
        name = input("註冊新帳號, 請輸入你的名稱：")
        password = input("註冊新帳號, 請輸入你的密碼：")
        if accounts.signup(name,password)==False:
            print("這個帳號已經被註冊,請重新輸入!")
        else:
            print("註冊完成，請重新登入!")
    elif options1=="2":
        sign=False
        name = input("登入, 請輸入你的名稱：")
        password = input("登入, 請輸入你的密碼：")
        if accounts.signin(name,password)==True:
            sign=True
            while sign==True:
                options2 = input("請選擇功能-1(存款)/2(提款)/3(結束):")
                if options2=="1":
                    named = input("請輸入轉入帳號,限本行帳戶:")
                    valued = input("請輸入存款金額：")
                    try:
                        if int(valued) > 0 :
                            if accounts.deposit(named,valued)==False:
                                print("帳號不存在,請重新輸入。")
                            else:
                                print("存入:"+valued+"元至帳戶:"+named)
                                print("存款完成,謝謝。已自動登出。")
                                sign=False
                        else:
                            print("金額有誤,如欲提款請選擇-2(提款)")
                    except:
                        print("金額有誤,請存入正整數金額。")
                elif options2=="2":
                    print("帳戶餘額:",accounts.balance(name),"元")
                    value = input("請輸入提款金額：")
                    try:
                        if int(value) > 0:
                            result=accounts.withdrawal(value)
                            if result=="no":
                                print("餘額不足。")
                            else:
                                print("提領:"+value+"元,餘額:"+str(result)+"元")
                                print("提款完成,謝謝。已自動登出。")
                                sign=False
                        else:
                            print("金額有誤,如欲存款請選擇-1(存款)")
                    except:
                        print("金額有誤,請提領正整數金額。")
                elif options2=="3":
                    sign=False
                    print("很高興為你服務,已登出。")
                else:
                    print("輸入錯誤,請重新輸入!")
        else:
            print("帳號或密碼有誤，請重新登入!")
    else:
        print("輸入錯誤,請重新輸入!")
