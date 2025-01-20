import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    criteria_met = sum([length_criteria, upper_criteria, lower_criteria, number_criteria, special_criteria])
    
    if criteria_met == 5:
        return "Strong password"
    elif 3 <= criteria_met < 5:
        return "Strong password"
    else:
        return "Weak password"

password = input("Enter a password to check its strength: ")
strength = check_password_strength(password)
print(f"Password strength: {strength}")