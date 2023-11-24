class Account:
    next_id = 1

    def __init__(self,id, name, balance):
        self.id = Account.next_id
        Account.next_id += 1
        self.name = name
        self.balance = balance

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'balance': self.balance}

    @classmethod
    def from_dict(cls, account_dict):
        account = cls(account_dict['name'], account_dict['balance'])
        account.id = account_dict['id']
        return account
