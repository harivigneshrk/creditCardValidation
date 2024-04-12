import re

def validateCreditCard(card_number):
    pattern = r'^(4|5|6)\d{3}(-?\d{4}){3}$'
    if re.match(pattern, card_number):
        return 'Valid'
    else:
        return 'Invalid'

# Input processing
n = int(input("Enter the number of credit card numbers: "))
for _ in range(n):
    card = input("Enter the credit card number: ").strip()
    result = validateCreditCard(card)
    print(result)
