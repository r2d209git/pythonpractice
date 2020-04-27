class Account:
    num_accounts = 0

    def __init__(self, name):
        self.name = name
        Account.num_accounts += 1

    def __del__(self):
        Account.num_accounts -= 1

    def print_num(self):
        print(self.name)



kim = Account("kim")
lee = Account("lee")
kim.num_accounts += 1
#print(kim.num_accounts)
Account.print_num(Account("bae"))
lee.print_num()


#kim.print_num()