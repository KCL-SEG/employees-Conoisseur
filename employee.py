"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

"""
Thoughts:
need to keep track of if worker is salary (paid monthly) or hourly (paid hourly)
    Maybe make subclasses for these?
need to keep track of commision as well, can be fixed or based of the number of contracts 
    calculate with multiplier
    
"""
class Employee:
    def __init__(self, name, commission):
        self.name = name
        self.commission = commission

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class SalaryEmployee(Employee):

    def __init__(self,name,monthly_salary,commission):
        super().__init__(name,commission)
        self.monthly_salary = monthly_salary

    def get_pay(self):
        pay = 0
        pay += self.monthly_salary

        if self.commission:
            pay += self.commission.calculateCommision()

        return pay

class HourlyEmployee(Employee):
    def __init__(self,name,hours_worked,pay_per_hour,commission):
        super().__init__(name,commission)
        self.hours_worked = hours_worked
        self.pay_per_hour = pay_per_hour

    def get_pay(self):
        pay = 0
        pay += (self.hours_worked * self.pay_per_hour)

        if self.commission:
            pay += self.commission.calculateCommision()

        return pay

class Commission():

    def calculateCommision(self):
        pass

class FixedCommision(Commission):

    def __init__(self,fixed_value):
        self.fixed_value = fixed_value

    def calculateCommision(self):
        return self.fixed_value

class ContractCommission(Commission):

    def __init__(self,contracts_landed,commission_per_contract):
        self.contracts_landed = contracts_landed
        self.commission_per_contract = commission_per_contract

    def calculateCommision(self):
        return self.contracts_landed * self.commission_per_contract

class NoCommission(Commission):
    def calculateCommision(self):
        return 0



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
#billie = Employee('Billie')
billie = SalaryEmployee("Billie",4000,NoCommission())

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
#charlie = Employee('Charlie')
charlie = HourlyEmployee("Charlie",100,25,NoCommission())

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
#renee = Employee('Renee')
renee = SalaryEmployee("Renee",3000,ContractCommission(4,200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
#jan = Employee('Jan')
jan = HourlyEmployee("Jan",150,25,ContractCommission(3,220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
#robbie = Employee('Robbie')
robbie = SalaryEmployee("Robbie",2000,FixedCommision(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
#ariel = Employee('Ariel')
ariel = HourlyEmployee("Ariel",120,30,FixedCommision(600))

