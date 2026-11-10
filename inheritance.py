"""Simple examples of inheritance in Python."""


# Problem 1: Vehicle, Car and Bicycle.
class Vehicle:
    def drive(self):
        return "Driving a vehicle"


class Car(Vehicle):
    def drive(self):
        return "Driving a car"


class Bicycle(Vehicle):
    def drive(self):
        return "Riding a bicycle"


# Problem 2: Person, Student and Employee.
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def introduce(self):
        return f"My name is {self.name}. I am {self.age} years old."


class Student(Person):
    def __init__(self, name, age, address, field_of_study):
        super().__init__(name, age, address)
        self.field_of_study = field_of_study

    def introduce(self):
        return f"{super().introduce()} I study {self.field_of_study}."


class Employee(Person):
    def __init__(self, name, age, address, company):
        super().__init__(name, age, address)
        self.company = company

    def introduce(self):
        return f"{super().introduce()} I work at {self.company}."


# Problem 3: Bank account and savings account.
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        return True

    def transfer(self, amount, destination):
        if not self.withdraw(amount):
            return False
        destination.deposit(amount)
        return True


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

    def check_balance(self):
        return self.balance


if __name__ == "__main__":
    print("Problem 1:")
    print(Vehicle().drive())
    print(Car().drive())
    print(Bicycle().drive())

    print("Problem 2:")
    print(Student("Anna", 21, "Paris", "Computer Science").introduce())
    print(Employee("Tom", 30, "London", "ABC Company").introduce())

    print("Problem 3:")
    account1 = BankAccount("001", 100)
    account2 = SavingsAccount("002", 50, 0.05)
    print("Transfer successful:", account1.transfer(30, account2))
    account2.add_interest()
    print("Savings balance:", account2.check_balance())
    print("Transfer with low balance:", account1.transfer(1000, account2))
