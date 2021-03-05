class CompoundInterest:
    
    def __init__(self, principal, interest_rate, years, monthly_contribution = 0):
        self.principal = principal
        self.interest_rate = interest_rate/100.00
        self.years = years
        self.monthly_contribution = monthly_contribution

    def compound_interest_calc(self):
        return round(self.principal * (1 + (self.interest_rate/12)) ** (12 * self.years), 2)

    def monthly_contribution_calc(self):
        number_of_months = 12 * self.years
        months_remaining = number_of_months

        total_interest = self.compound_interest_calc()

        while months_remaining > 0:
            running_interest = self.monthly_contribution * (1 + (self.interest_rate/12)) ** (months_remaining)

            total_interest += running_interest
            months_remaining -= 1

        return round(total_interest, 2)
