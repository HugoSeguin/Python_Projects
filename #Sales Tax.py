#Sales Tax

from decimal import Dicimal

rates = {
    'Chico': Decimal('.5'),
    'Groucho' : Decimal('.7'),
    'Harpo' : Decimal('.5'),
    'Zeppo' : Decimal('.4')
}

def time_percentage(hour):
    return hour/ Deciaml('24.0')
def calculate_tax(amount, state, hour):
    return float(amount + (amount * rates(state) * time_percentage(hour)))

    