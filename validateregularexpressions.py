#Python program to validate the regular expressions for the following
# a. Email address
# b. Mobile number of Bangladesh
# c. Telephone number of USA
# d. 16 character aplha numeric password composed of alphabets of upper case, lower case, special character and numbers

# Email address
import re

email_address = "abc12@guvi.in"

def valid_email_address(data):
    pattern = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,6}$"
    if re.match(pattern, data):
        return True
    else:
        return False
print("Valid Email  : ", valid_email_address(email_address))     # Test the function with the provided email address


# Mobile number of Bangladesh
import re

mobile_number = "+8801153067158"  # Corrected to be a string

def valid_mobile_number(data):
    pattern = r"^(\+)?(88)?01[0-9]{9}$"  # Updated regular expression pattern
    if re.match(pattern, data, re.IGNORECASE):
        return True
    else:
        return False
print("Valid Mobile Number of Bangladesh  : ", valid_mobile_number(mobile_number))     # Test the function with the provided mobile number



# Telephone number of USA
import re

mobile_number = "+1-555-905-6836"   # Corrected to be a string

def valid_mobile_number(data):
    pattern = r"^(\+?1-?)?(\([0-9]{3}\)|[0-9]{3})[-.]?([0-9]{3})[-.]?([0-9]{4})$"
    if re.match(pattern, data, re.IGNORECASE):
        return True
    else:
        return False
print("Valid Mobile Number of USA  : ", valid_mobile_number(mobile_number))      # Test the function with the provided mobile number



# 16 character aplha numeric password composed of alphabets of upper case, lower case, special character and numbers
import re

alphanumeric_password = "GUVItest@@@@1234"     # Corrected to be a string

def valid_alphanumeric_password(data):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*()_+{}[\]:;<>,.?/~`'\"\\|-])(?=.*[0-9])[A-Za-z0-9!@#$%^&*()_+{}[\]:;<>,.?/~`'\"\\|-]{16}$"
    if re.match(pattern, data):
        return True
    else:
        return False
print("Valid 16 character alpha numeric password  : ", valid_alphanumeric_password(alphanumeric_password)) # Test the function with the provided 16 character aplha numeric password
