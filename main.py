
# Set variables for values which may be subject to change in the future
min_month_rent = 110
max_month_rent = 8660
min_week_rent = 25
max_week_rent = 2000
min_membership_fee = 120
vat = 0.2

# Organisation structure utilizing inheritance of parent class
class Client:
    def __init__(self, name, has_fixed_membership_fee, fixed_membership_fee_amount):
        self.name = name
        self.config = ClientConfig(has_fixed_membership_fee, fixed_membership_fee_amount)

class Division(Client):
    pass

class Area(Division):
    pass

class Branch(Area):
    pass

class Building(Branch):
    pass

class House(Branch):
    pass

class Flat(Building):
    pass

class ClientConfig:
    def __init__(self, has_fixed_membership_fee, fixed_membership_fee_amount):
        self.has_fixed_membership_fee = has_fixed_membership_fee
        self.fixed_membership_fee_amount = fixed_membership_fee_amount


# Function to calculate the membership fee
def calculate_membership_fee(rent_amount, rent_period, organisation_unit):
    if rent_period == 'm':
        membership_fee = (rent_amount / 4.345) * (1 + vat) # 4.345 is the average number of weeks in a month
    else:
        membership_fee = rent_amount * (1 + vat)

    if membership_fee < min_membership_fee * (1 + vat):
        membership_fee = min_membership_fee * (1 + vat)

    if organisation_unit.config.has_fixed_membership_fee == True:
        membership_fee = organisation_unit.config.fixed_membership_fee_amount

    return(int(membership_fee))


# ---------- START of Rent Info input loop ----------
while True:

    # Get user input for rent_amount
    while True:
        # Accept only positive number inputs and handle errors
        try:
            rent_amount = int(input("Enter rent amount (£): "))
            if rent_amount < 1:
                raise ValueError
            break
        except ValueError:
            print(" ► Invalid input. Please enter an amount greater than or equal to 1.\n")

    # Get user input for rent_period
    while True:
        rent_period = (input("Enter rent period, 'm' for monthly, 'w' for weekly: "))
        # Accept only 'm' or 'w' as inputs and handle errors
        if rent_period.lower() not in ['m', 'w']:
            print(" ► Invalid input. Please enter 'm' for month, 'w' for week.\n")
        else:
            break
    
    # Check if the rent amount is within the specified range. If yes, break the Rent Info input loop
    if (rent_period == 'm') and ((rent_amount < min_month_rent) or (rent_amount > max_month_rent)): 
        print(f" ► Invalid input. Monthly rent amount must be between {min_month_rent} and {max_month_rent}.\n")
    elif (rent_period == 'w') and ((rent_amount < min_week_rent) or (rent_amount > max_week_rent)):
        print(f" ► Invalid input. Weekly rent amount must be between {min_week_rent} and {max_week_rent}.\n")
    else:
        break
# ---------- END of Rent Info input loop ----------


# ---------- START of Organisation Unit Info input ----------
orgunit_name_input = input("Enter Organisation Unit name: ")

while True:
    orgunit_hasfixedmem_input = input("Fixed Membership Fee? y/n: ")
    if orgunit_hasfixedmem_input.lower() not in ['y', 'n']:
                print(" ► Invalid input. Please enter 'y' or 'n' only.\n")
    else:
        break

# Convert user input regarding 'has fixed membership fee' into boolean
if orgunit_hasfixedmem_input == 'y':
    orgunit_hasfixedmem_input = True

    # If 'has fixed membership fee' is true, ask for the 'fixed membership fee amount'
    while True:
        try:
            orgunit_fixedmemfee_input = int(input("Enter Fixed Membership Fee amount (£): "))
            if orgunit_fixedmemfee_input < 0:
                raise ValueError
            break
        except ValueError:
            print(" ► Invalid input. Fixed Membership Fee must be greater than or equal to 0.\n")

else:
    orgunit_hasfixedmem_input = False
    orgunit_fixedmemfee_input = 0
# ---------- END of Organisation Unit Info input ----------


# Construct an instance of the House class as an exampple using information obtained from the Organisation Unit Info input section
organisation_unit = House(orgunit_name_input, orgunit_hasfixedmem_input, orgunit_fixedmemfee_input)


print(f" ► The membership fee is £{calculate_membership_fee(rent_amount, rent_period, organisation_unit)}.\n")
