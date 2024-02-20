import pymysql

db = None
cur = None

def connectDB():
    global db,cur
    db = pymysql.connect(host='localhost',
                     user='root',
                     password='',
                     database='python_8_1')
    cur = db.cursor()

def disconnectDB():
    db.close()
    cur.close()

def NewAccount(Name,address,identity_proof,Mobile_number):
    connectDB()
    query = query = f'insert into account_details (name,address,identity_proof,mobile_number)values("{Name}","{address}",{identity_proof},{Mobile_number})'
    cur.execute(query)
    db.commit()
    disconnectDB()

def depositMoney(Account_Number,recevad_Money):
    connectDB()
    query = query = f'update account_details set account_balance = ifnull(account_balance,0.00) + {recevad_Money} where Account_Number = {Account_Number}'
    cur.execute(query)
    db.commit()
    disconnectDB()

def WithdrawMoney(Account_Number,Withdraw_Money):
    connectDB()
    query = query = f'update account_details set account_balance = ifnull(account_balance,0.00) -{Withdraw_Money} where Account_Number={Account_Number}'
    cur.execute(query)
    db.commit()
    disconnectDB()

def Manage_Transaction(account_number,transaction_Type,Transaction_amount):
    connectDB()
    query = query = f'insert into Transaction_details values({account_number},"{transaction_Type}",{Transaction_amount},curdate())'
    cur.execute(query)
    db.commit()
    disconnectDB()

def Show_Balance(Account_Number):

    connectDB()
    query = query = f'select account_balance from Account_details where Account_Number={Account_Number}'
    cur.execute(query)
    return cur.fetchone()
    db.commit()
    disconnectDB()

def Show_Transaction(Account_Number):
    connectDB()
    query = query = f'select * from Transaction_details where Account_Number={Account_Number}'
    cur.execute(query)
    return cur.fetchall()
    db.commit()
    disconnectDB()

def updatename(Account_Number,name,address):
    connectDB()
    query = f'update Account_details set name="{name}",address="{address}" where Account_Number={Account_Number}'
    cur.execute(query)
    db.commit()
    disconnectDB()

def Show_Account_dtls(Account_Number):
    connectDB()
    query = query = f'select * from Account_details where Account_Number = {Account_Number}'
    cur.execute(query)
    return cur.fetchall()
    db.commit()
    disconnectDB()    

def deleterecord(sid):
    connectDB()
    query = f'delete from account_details where Account_Number={sid}'
    cur.execute(query)
    db.commit()
    disconnectDB()
    
while True:
        print('''Banking Management System
      1.New Account Creation
      2.Deposit Money
      3.Withdraw Money
      4.change the owner Name and address
      5.Display the number of transactions and closing balance
      6.Show Account details
      8.Exit sub-menu
      7.delect account
      '''
      )
        
        choice = int(input('Enter your choice: '))
        if choice==1:
            name = input('Enter the name: ')
            address = input('Enter your address: ')
            identity_proof = input('Enter your identity_proof: ')
            mobile_number = input('Enter your mobile_number: ')
            NewAccount(name,address,identity_proof,mobile_number)
        elif choice==2:
            Account_Number = int(input('Enter the account number for deposit'))
            amount = Show_Balance(Account_Number)
            print('Your opening balance is',amount)
            recevad_Money = int(input('Enter the Money for deposit'))
            depositMoney(Account_Number,recevad_Money)
            transaction_Type = 'DEPOSITE'
            Manage_Transaction(Account_Number,transaction_Type,recevad_Money)
            amount = Show_Balance(Account_Number)
            print('Your Cloasing balance is',amount)
        elif choice==3:
            Account_Number = int(input('Enter the account number for Withdraw'))
            amount = Show_Balance(Account_Number)
            print('Your opening balance is',amount)
            Withdraw_Money = int(input('Enter the Money for Withdraw'))
            WithdrawMoney(Account_Number,Withdraw_Money)
            transaction_Type = 'WITHDRAW'
            Manage_Transaction(Account_Number,transaction_Type,Withdraw_Money)
            amount = Show_Balance(Account_Number)
            print('Your Cloasing balance is',amount)
        elif choice==4:
            Account_Number = int(input('Enter the account number'))

            name = input('Enter the New name: ')
            address = input('Enter your new address: ')
            updatename(Account_Number,name,address)
        elif choice==5:
            Account_Number = int(input('Enter the account number to see transaction details'))
            Tra = Show_Transaction(Account_Number)
            for i in Tra:
                print(f'Account Number: {i[0]}\ntransection_type: {i[1]}\ntransection Amount: {i[2]}\ntransection_Date: {i[3]}')
            amount = Show_Balance(Account_Number)
            print('Your Closing balance is',amount)
        elif choice==6:
            Account_Number = int(input('Enter the account number to see details'))
            ACC = Show_Account_dtls(Account_Number)
            for i in ACC:
                print(f'Account Number: {i[0]}\nName: {i[1]}\nAddress : {i[2]}\nIdentity_proof: {i[3]}\nMobile number: {i[4]}\nBalance: {i[5]}')
               
        elif choice==8:
            break
        
        elif choice==7:
            sid = int(input('Enter the account number: '))
            deleterecord(sid)
        else:
            print('Enter the cerrect option')
