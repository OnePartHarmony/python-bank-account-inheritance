class BankAccount:
  def __init__(self, balance = 0):
    self.balance = int(balance)
    self.interest_rate = .02

  def __str__(self):
    return f"This bank account has a balance of ${self.balance} with a {self.interest_rate * 100}% interest rate."
  
  def deposit(self, amount):
    if amount < 0:
      return False
    self.balance += int(amount)
    print(f"${amount} was deposited for a total of ${self.balance}")

  def withdraw(self, amount):
    if amount < 0:
      return False
    self.balance -= int(amount)
    print(f"${amount} was withdrawn for a total of ${self.balance}")

  def accumulate_interest(self):
    self.balance += self.balance * self.interest_rate
    print(f"The account balance is now ${self.balance}")
    return self.balance



class ChildrensAccount(BankAccount):
  def __init__(self, balance=0):
    super().__init__(balance)
    self.interest_rate = 0
  
  def accumulate_interest(self):
    self.balance += 10
    print(f"The account balance is now ${self.balance}")
    return self.balance
  

class OverdraftAccount(BankAccount):
  def __init__(self, balance=0):
    super().__init__(balance)
    self.overdraft_penalty = 40
  
  def withdraw(self, amount):
    if amount > self.balance:
      self.balance -= self.overdraft_penalty
      return False
    return super().withdraw(amount)

  def accumulate_interest(self):
    if self.balance <= 0:
      print("No interest accumulated due to insufficient funds.")
      return
    return super().accumulate_interest()




basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))
