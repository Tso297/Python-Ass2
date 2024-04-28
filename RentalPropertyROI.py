
class RentalProperty:
    def __init__(self, rental, laundry, storage, misc, tax, insurance, utilities, hoa, lawncare, vacancy_rate, 
                 repairs, cap_ex, prop_management_rate, mortgage, down_payment, closing_costs, rehab_budget, misc_investment):
        # Income sources
        self.rental = rental
        self.laundry = laundry
        self.storage = storage
        self.misc_income = misc
        
        # Expenses
        self.tax = tax
        self.insurance = insurance
        self.utilities = utilities
        self.hoa = hoa
        self.lawncare = lawncare
        self.vacancy = vacancy_rate * rental
        self.repairs = repairs
        self.cap_ex = cap_ex
        self.prop_management = prop_management_rate * rental
        self.mortgage = mortgage
        
        # Investment details
        self.down_payment = down_payment
        self.closing_costs = closing_costs
        self.rehab_budget = rehab_budget
        self.misc_investment = misc_investment

    def total_monthly_income(self):
        return self.rental + self.laundry + self.storage + self.misc_income

    def total_monthly_expenses(self):
        return (self.tax + self.insurance + self.utilities + self.hoa + self.lawncare +
                self.vacancy + self.repairs + self.cap_ex + self.prop_management + self.mortgage)

    def monthly_cash_flow(self):
        return self.total_monthly_income() - self.total_monthly_expenses()

    def annual_cash_flow(self):
        return self.monthly_cash_flow() * 12

    def total_investment(self):
        return self.down_payment + self.closing_costs + self.rehab_budget + self.misc_investment

    def cash_on_cash_roi(self):
        return (self.annual_cash_flow() / self.total_investment()) * 100

# Example instantiation and function calls
property1 = RentalProperty(
    rental=2000, laundry=0, storage=0, misc=0, 
    tax=150, insurance=100, utilities=0, hoa=0, lawncare=0, vacancy_rate=0.05, 
    repairs=100, cap_ex=100, prop_management_rate=0.10, mortgage=860, 
    down_payment=40000, closing_costs=3000, rehab_budget=7000, misc_investment=0
)

print("Monthly Cash Flow: $", property1.monthly_cash_flow())
print("Annual Cash Flow: $", property1.annual_cash_flow())
print("Total Investment: $", property1.total_investment())
print("Cash on Cash ROI: ", property1.cash_on_cash_roi(), "%")
