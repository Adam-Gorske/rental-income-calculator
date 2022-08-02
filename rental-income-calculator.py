from IPython.display import clear_output


class RentalIncomeCalculator():

    '''
        The RentalIncomeCalculator has a few methods:

        - totalMonthlyIncome:
            Takes inputs of the following monthly incomes, adds them together, and stores them in a variable:
                Laundry Income
                Storage Income
                Misc Income

        - totalMonthlyExpenses:
            Takes inputs of the following monthly expenses, adds them together, and stores them in a variable:
                Taxes
                Insurance
                Water / Sewage
                Garbage
                Electric
                Gas
                HOA Fees
                Lawn / Snow
                Vacancy
                Repairs
                CapEx
                Prop. Management
                Mortgage

        - annualCashFlow:
            (totalMonthlyIncome - totalMonthlyExpenses) * 12

        - totalInvestment:
            Takes inputs of the following expenses, adds them together, and stores them in a variable:
                Down Payment
                Closing Costs
                Rehab Budget
                Misc Other

        - CashOnCashReturn:
            (annualCashFlow / totalInvestment) * 100


        Expected Attributes:
        - income: integer
        - expenses: integer
        - annual cash flow: integer
        - total investment: integer
        - cash on cash return: integer
    '''

    def __init__(self, income, expenses, annual_cash_flow, total_investment, cash_on_cash_return):
        self.income = income
        self.expenses = expenses
        self.annual_cash_flow = annual_cash_flow
        self.total_investment = total_investment
        self.cash_on_cash_return = cash_on_cash_return

    def totalMonthlyIncome(self):
        print("\nThe following are monthly incomes.")
        self.income += float(input("Rental income: "))
        self.income += float(input("Storage income: "))
        self.income += float(input("Misc income: "))
        clear_output()
        print(f"Your total income is ${round(self.income, 2)}.")

    def totalMonthlyExpenses(self):
        print("The following are monthly expenses.")
        self.expenses += float(input("Taxes: "))
        self.expenses += float(input("Insurance: "))
        self.expenses += float(input("Water / Sewage: "))
        self.expenses += float(input("Gabage: "))
        self.expenses += float(input("Electric: "))
        self.expenses += float(input("Gas: "))
        self.expenses += float(input("HOA Fees: "))
        self.expenses += float(input("Lawn / Snow: "))
        self.expenses += float(input("Vacancy: "))
        self.expenses += float(input("Repairs: "))
        self.expenses += float(input("Capital Expenditures: "))
        self.expenses += float(input("Property Management: "))
        self.expenses += float(input("Mortgage: "))
        clear_output()
        print(f"Your total expenses are ${round(self.expenses, 2)}.")

    def annualCashFlow(self):
        self.annual_cash_flow = (self.income - self.expenses) * 12
        clear_output()
        print(f"Your annual cash flow is ${round(self.annual_cash_flow, 2)}")

    def totalInvestment(self):
        self.total_investment += float(input("Down Payment: "))
        self.total_investment += float(input("Closing Costs: "))
        self.total_investment += float(input("Rehab Budget: "))
        self.total_investment += float(input("Misc Other: "))
        clear_output()
        print(f"Your total investment was ${round(self.total_investment, 2)}")

    def cashOnCashReturn(self):
        self.cash_on_cash_return = (
            self.annual_cash_flow / self.total_investment) * 100
        clear_output()
        print(
            f"Your cash on cash return is {round(self.cash_on_cash_return, 2)}%")


brandon_calculator = RentalIncomeCalculator(0, 0, 0, 0, 0)


def run():
    while True:
        response = input("Welcome to the Rental Income Calculator! Please enter only whole numbers. Do not use letters or special characters such as $.\nIf one of the options doesn't apply to you, please enter 0.\nType one of the options continue / quit.\n").lower()

        if response == 'continue':
            brandon_calculator.totalMonthlyIncome()
            brandon_calculator.totalMonthlyExpenses()
            brandon_calculator.annualCashFlow()
            brandon_calculator.totalInvestment()
            brandon_calculator.cashOnCashReturn()

        elif response == 'quit':
            print("Thank you for using the Rental Income Calculator!")
            break

        else:
            print("Please try another input!")


run()
