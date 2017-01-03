class CreditCard:

    def __init__(self,customer,bank,account,limit):

    self._customer = customer
    self._balance = 0
    self._bank = bank
    self._limit = limit
    self._account = account

    def get_customer(self):
        return self._customer

    def get_balance(self):
        return self._balance

    def get_bank(self):
        return self._bank

    def get_limit(self):
        return self._limit

    def get_account(self):
        return self._account

    def charge(self,price):
        if price + self._balance >= self._limit :
            return False
        else:
            self._balance += price
            return True

    def make_payment(self,amount):
        self.balance -= amount

class PredatoryCreditCard(CreditCard):

    def __init__(self, customer, bank, account, limit, apr):
        super().__init__(customer, bank, account, limit)
        self._apr = apr

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += 5
        return success

    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1+self._apr,1/12)
            self._balance *= monthly_factor

class Vector:

    def __init__(self,d):
        self._coord = [0]*d

    def __len__(self):
        return len(self._coord)

    def __getitem__(self,j):
        return self._coord[j]

    def __setitem__(self,j,val):
        self._coord[j] = val

    def __add__(self,other):
        if len(self) != len(other):
            raise ValueError("Dimensions must match!")
        result = [0]*len(self)
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self,other):
        return self == other

    def __ne__(self,other):
        return self != other



class Range:

    def __init__(self, start, stop = None, step = 1):
        if step == 0 :
            raise ValueError("Step cannot be 0")
        if stop == None :
            start,stop = 0,start

        self._length = max(0,(stop-start+step-1)//step)

        self._start = start
        self._step = step


    def __len__(self):
        return self._length

    def __getitem__(self,k):
        if k < 0:
            k += len(self)
        if not 0<=k<len(self):
            raise ValueError("Index out of range")

        return self._start + k*self._length




