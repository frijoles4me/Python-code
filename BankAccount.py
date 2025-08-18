# Write code below 💖

emptyList = []

class BankAccount:
 def __init__(self, first_name, last_name,account_id,account_type,pin,balance):
   self.first_name = first_name
   self.last_name = last_name
   self.account_id = account_id
   self.account_type = account_type
   self.pin = pin
   self.balance = balance

 def deposit(self, amount):
   self.balance = self.balance + amount
   return self.balance
 
 def withdraw(self, amount):
   self.balance = self.balance - amount
   return self.balance
 
 def display_balance(self):
   print(f'{self.first_name} {self.last_name} Current balance. ${self.balance}')
 
 def get_details(self):
   return self.first_name,self.last_name,self.account_id,self.account_type,self.pin,self.balance 
 


bank = BankAccount("John",'Doe',1232423,"Checkings",1234,0)
print(emptyList)



print(vars(bank))
bank.deposit(100)
print(vars(bank))
bank.withdraw(50)
print(vars(bank))
bank.display_balance()
print(emptyList)

for BankAccount in emptyList:
  print(BankAccount.get_details())