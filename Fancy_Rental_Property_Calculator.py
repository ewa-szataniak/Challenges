class Property():
    def __init__(self):
        self.prop_price = 0
        self.income = 0
        self.expenses = 0
        self.cash_flow = 0 
        self.pet_fee = 25
        self.tenant_pet_fee = None 
        self.laundry = 0 
        self.storage = 0 
        self.rent = None

    def prop_val(self):
        print("Hello Friend!")
        self.prop_price = input("Please enter the cost of the property you are planning to purchase.\n")
         

    def tenant(self):
        # self.tenn1 = {}
        print("\n\nLet's check a few things about your tenant.")
        self.name = input("What is your tenant's name? \n").title()
        self.rent_amount = input("The rent amount is currently set at $100. If you would like to change that amount, please enter a different amount. If not, enter 'skip'. \n")
        if self.rent_amount.lower() == 'skip':
            self.rent = int(int(self.prop_price) * 1.00)
        else:
            self.rent = self.rent_amount 
        print(f"Your rent is set at ${self.rent} a month.")     
        self.pets = input("How many lovely pets does your tenant have? For none, please enter 0. \n")
        self.tenant_pet_fee = int(self.pets) * self.pet_fee 
        self.tenn1 = {
            'Name:': self.name,
            'Rent:' : f'${self.rent}',
            'Pets:' : self.pets,
            'Pet Fee:' : f'${self.tenant_pet_fee}',
        }
        print("\n---------------------------\n")
        print("\nHere is a breakdown of your tenant's information:\n")
        # print("\n  Name  ", "  Rent ", "Pets", "Pet Fee")
        for k,v in self.tenn1.items():
            print(k, v)
        print("\n")
        # print("\n")

    def calc_income(self):
        print("\n Let's determine rental payment:\n")
        self.laundry = input("Can you provide laundry on your property? If yes, please enter monthly amount you charge your tenant. If no, please enter 0. \n")
        self.storage = input("Can you provide storage on your property? If yes, please enter monthly amount you charge your tenant. If no, please enter 0. \n")
        self.other = input("Do you receive any additional miscellaneous income from this property or tenant? If so, please enter the monthly amount: if no, please enter 0. \n")

        self.income = (int(self.rent) + int(self.tenant_pet_fee) + int(self.laundry) + int(self.storage) + int(self.other))
        print("\n---------------------------\n")
        print(f"\nYour total monthly income is ${self.income}.\n")




    def calc_expenses(self):
        print("\n\nLet's determine your monthly expenses:\n")
        self.tax = input("How much do you annually pay in taxes for this property?\n")
        self.monthly_tax = int(self.tax) / 12

        self.insurance = input("What is your monthly payment for insurance on this property?n")
        self.utilities = input("What is your monthly payment for utilities on this property? \n")
        self.HOA = input("What is your monthly HOA fee? \n")
        self.vacancy = input("What is the desired monthly amount you would like to set aside for potential vacancy?\n")
        self.repairs = input("What is the desired monthly amount you would like to allocate for potential repairs? \n")
        self.capex = input("What is the desired monthly amount you would like to set aside for future major replacements over time?\n")
        self.prop_man = input("Will you be hiring property manager? If yes, what is the monthly cost? If no, please enter 0. \n")
        self.mortgage = input("What is your monthly mortgage payment for this property? \n")
        self.other = input("Do you receive any other miscellaneous income from this property or tenant? If so, please enter the monthly amount, if no, please enter 0. \n")

        self.expenses = (int(self.monthly_tax) + int(self.insurance) + int(self.utilities) + int(self.HOA) +  int(self.vacancy) + int(self.repairs) + int(self.capex) + int(self.prop_man) + int(self.mortgage) + int(self.other)) 
        
        print("\n---------------\n")
        print(f"\nYour total monthly expenses are ${self.expenses}.\n")

    def cash(self):
        self.cash_flow = int(self.income) - int(self.expenses)

        print("\n----------------\n")
        print(f"\nYour monthly cash flow is${self.cash_flow}.\n")

    
    def ROI(self):
        print("\nLet's determine your total investment in this property:\n")
        self.down = input("What was the amount of your down payment on this property?\n")
        self.closing = input("What was the total amount of your closing costs for this property?\n")
        self.rehab = input("How much did you invest in repairs for this property?\n")
        self.other = input("Did you invest any additional funds after purchasing this property? If yes, please enter the amount. If no, please enter 0. \n")

        self.investment = (int(self.down) + int(self.closing) + int(self.rehab) + int(self.other))

        print(f"\nYour total investment on this property is ${self.investment}.\n")

        self.annual_cash = int(self.cash_flow) * 12

        self.ret_invest = round(((int(self.annual_cash) / int(self.investment)) * 100), 1)
        print("\n---------------------------\n")
        print(f"Your return on investment on this property is {self.ret_invest}%.\n")
        print("If the current calculations are not satisfactory, you may consider adjusting certain figures such as the rent you charge or the amount you are willing to invest in purchasing the property.\n")
        print("Feel free to use this calculator whenever you need it! \n")
        print("ALL THE BEST in your real estate endavours!")



    def run(self):
        print("\nThank you for using Rental Property Calculator! \n")

        self.prop_val()

        self.tenant()

        self.calc_income()

        self.calc_expenses()

        self.cash()

        self.ROI()        


my_prop = Property()

my_prop.run()   
