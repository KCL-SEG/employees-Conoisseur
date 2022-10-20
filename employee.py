"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

import re

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

    def __str__(self):
        returnString = f'{self.name} works on a monthly salary of {self.monthly_salary}'
        if (self.commission.getCommissionType() != 'No Commission'):
            returnString += f'and receives a bonus commission of {self.commission.calculateCommision()}'
        returnString += f'Their total pay is {self.get_pay()}'
        # returnString = "Name: " + self.name + "\n"
        # returnString += "Fixed pay per month: " + str(self.monthly_salary) + "\n"
        # returnString += "Commission Type " + self.commission.getCommissionType() + "\n"
        # returnString += "Total Pay: " + str(self.get_pay())


        return returnString


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

    def __str__(self):
        returnString = f'{self.name} works on a contract of {self.hours_worked} hours at {self.pay_per_hour}/hour'
        if (self.commission.getCommissionType() != 'No Commission'):
            returnString += f' and receives a bonus commission of {self.commission.calculateCommision()} '
        returnString += f'Their total pay is {self.get_pay()}'
        # returnString = "Name: " + self.name + "\n"
        # returnString += "Hours Worked: " + str(self.hours_worked) + "\n"
        # returnString += "Pay per hour: " + str(self.pay_per_hour) + "\n"
        # returnString += "Commission Type " + self.commission.getCommissionType() + "\n"
        # returnString += "Total Pay: " + str(self.get_pay())

        return returnString

class Commission():

    def calculateCommision(self):
        pass

    def getCommissionType(self):
        pass

class FixedCommision(Commission):

    def __init__(self,fixed_value):
        self.fixed_value = fixed_value

    def calculateCommision(self):
        return self.fixed_value

    def getCommissionType(self):
        return "Fixed Commission"

class ContractCommission(Commission):

    def __init__(self,contracts_landed,commission_per_contract):
        self.contracts_landed = contracts_landed
        self.commission_per_contract = commission_per_contract

    def calculateCommision(self):
        return self.contracts_landed * self.commission_per_contract

    def getCommissionType(self):
        return "Contract Commission"

class NoCommission(Commission):
    def calculateCommision(self):
        return 0

    def getCommissionType(self):
        return "No Commission"



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

# print(billie.get_pay())
# print(type(billie.get_pay()))
# print(str(billie))
#
# assert billie.get_pay() == 4000
# string = str(billie)
# print(str(billie))
# regex = '^Billie works on a monthly salary of 4000.\s+Their total pay is 4000.$'
# print(regex)
# assert re.match(regex, string)


