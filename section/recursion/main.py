def format_phone_number(number, digit=0):
    if digit >= len(number):  
        return ""  # Base case: return an empty string if there's nothing left to process
    
    if number[digit].isdigit():  
        return number[digit] + format_phone_number(number,digit +1)  # Keep digits and process the rest recursively
    else:
        return format_phone_number(number, digit+1)  # Skip non-digit characters and continue recursively

# Testing the result
print(format_phone_number("(123) 456-7890"))
print(format_phone_number("  +1-800-555-0199  "))
print(format_phone_number("987.654.3210"))