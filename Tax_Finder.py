'''
This is for estimates only. No claims at being accurate for tax purposed. 
'''
states = {
    "AL": {9999999999999999999: 0.0},
    "AK": "",
    "AZ": "",
    "AR": "",
    "CA": {
        20198: 0.01,
        47884: 0.02,
        75576: 0.04,
        104910: 0.06,
        132590: 0.08,
        677278: 0.0930,
        812728: 0.1030,
        1354550: 0.1230,
        2000000: 0.1330,  # greater thank this sky's the limit
    },
    "CO": {9999999999999999999: 0.044},
    "CT": "Connecticut",
    "DC": "District of Columbia",
    "DE": "Delaware",
    "FL": {9999999999999999999: 0.0},
    "GA": "Georgia",
    "HI": "Hawaii",
    "IA": "Iowa",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "MA": "Massachusetts",
    "MD": "Maryland",
    "ME": "Maine",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MO": "Missouri",
    "MS": "Mississippi",
    "MT": "Montana",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "NE": "Nebraska",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NV": {9999999999999999999: 0.0},
    "NY": "New York",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": {9999999999999999999: 0.0},
    "TN": "Tennessee",
    "TX": {9999999999999999999: 0.0},
    "UT": "Utah",
    "VA": "Virginia",
    "VT": "Vermont",
    "WA": {9999999999999999999: 0.0},
    "WI": "Wisconsin",
    "WV": "West Virginia",
    "WY": {9999999999999999999: 0.0},
}


fed_married_joint_tax = {
    20550: 0.10,
    83550: 0.12,
    178150: 0.22,
    431900: 0.24,
    467850: 0.35,
    647850: 0.37,
}

filing_type_array = {
    1: "Single",
    2: "Married filing separately",
    3: "Married filing jointly",
    4: "Head of Household",
}


class Get_income:
    def __init__(self, state, filing_status, income_amount) -> None:
        self.state = state
        #        self.tax_rate = tax_rate
        self.filing_type = filing_status
        self.income_amount = income_amount

    def __str__(self):
        return f"filing state {self.state} and status {self.filing_type}"

    @property
    def income(self):
        return self._income

    @income.setter
    def income(self, income):
        if not income:
            raise ValueError("Invalid state")
        elif income <= 0:
            raise ValueError("Income cannot be negative")
        self._income = income

    # getter for state
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        if not state:
            raise ValueError("Invalid state")
        elif state not in states.keys():
            raise ValueError("Invalid state")
        self._state = state

    @property
    def filing_status(self):
        return self._filing_status

    @state.setter
    def filing_status(self, filing_status):
        if not filing_status:
            raise ValueError("Missing filing status")
        self._filing_status = filing_status

    @property
    def filing_type(self):
        return self.filing_type

    @state.setter
    def filing_type(self, filing_type):
        if not filing_type:
            raise ValueError("Missing filing type")
        self.filing_type = filing_type

    def state_input():
        # income_amount = int(35000)
        state_for_taxes = input(
            "Enter the state where you pay file your taxes (State abbreviation): "
        )
        while True:
            try:
                if state_for_taxes in states.keys():
                    return state_for_taxes
            except:
                state_for_taxes = input(
                    "Enter the state where you pay file your taxes (State abbreviation): "
                )
                continue

    def filing_type(income, state):
        filing_type = int(
            input(
                "Enter your filing type:\n1. Single \n2. Married filing separately\n3. Married filing jointly\n4. Qualifying widow(er)\n"
            )
        )

        match filing_type:
            case 1:
                ca_single_tax = {
                    "$17,618": 1.0,
                }

            case 2:
                ca_married_sep_tax = {}
            case 3:
                fed_income_deductions = income - 27700  # 67300

                # print(income)

                taxable_income_amount = []

                for k, v in fed_married_joint_tax.items():
                    if fed_income_deductions < 27700:
                        print("no taxes owed")
                        break

                    if fed_income_deductions > k:
                        on_going_tax_amount = fed_income_deductions - k  # 46750,
                        combined_taxes = k * v
                        taxable_income_amount.append(combined_taxes)  # 2050
                    elif fed_income_deductions < k:
                        combined_taxes = on_going_tax_amount * v
                        taxable_income_amount.append(combined_taxes)  # 2050
                        break
                    else:
                        print("Error")
                fed_taxes_owed = sum(taxable_income_amount)

                for k, v in states.items():
                    if k == state:
                        for i in v.items():
                            if income < int(i[0]):
                                state_tax_rate = i[1]
                                print(state_tax_rate)
                                break
                        break

                taxable_income_amount = []

                # state_income_deductions = income - (10404 + 280 + fed_taxes_owed)
                # print(state_income_deductions)
                for k, v in states.items():
                    if k == state:
                        for i in v.items():
                            if income < fed_taxes_owed:
                                print("no taxes owed")
                                break
                            if income > i[0]:
                                on_going_tax_amount = income - i[0]
                                # 46750,
                                combined_taxes = (i[0] * i[1]) - sum(
                                    taxable_income_amount
                                )
                                taxable_income_amount.append(combined_taxes)  # 2050
                            elif income < i[0]:
                                combined_taxes = on_going_tax_amount * i[1]
                                taxable_income_amount.append(combined_taxes)  # 2050
                                break
                            else:
                                print("no taxes owed")
                        state_taxes_owed = sum(taxable_income_amount)
                        break

            case 4:
                ca_HoH_tx = {}
        return state_taxes_owed, fed_taxes_owed

    def income_amount():
        while True:
            try:
                income_pre_taxed = int(input("Enter your pre-tax income:"))
                return income_pre_taxed

            except:
                print("error")

    def find_tax(income_amount, state_taxes_owed, fed_amount_owed):
        return f"Income amount: {income_amount} \nFed taxes: {fed_amount_owed} \nState Deductions: {state_taxes_owed}\nTotal taxes paid: {state_taxes_owed+fed_amount_owed}"


def main():
    assumptions = "This calculator takes no assumptions for your taxes, meaning, the only deduction is at the federal level, as it is the one constant. All states are based on no deduction. Additionally, the only states within are CA and CO, and filing status is married, filing jointly. Reasoning: this is what is applicable to me at the moment."
    print(assumptions)
    state = Get_income.state_input()
    income = Get_income.income_amount()
    filing_type = Get_income.filing_type(income, state)
    print(Get_income.find_tax(income, filing_type[0], filing_type[1]))


if __name__ == "__main__":
    main()
