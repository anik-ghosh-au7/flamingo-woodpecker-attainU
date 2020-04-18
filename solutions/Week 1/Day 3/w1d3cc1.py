# Solution


def temp_converter(temp, f):
    if f == 'F':
        result = int((int(temp) - 32) / 9 * 5)
        return '%s°F is %d in Celsius' % (temp, result)
    elif f == 'C':
        result = int((int(temp) / 5 * 9) + 32)
        return '%s°C is %d in Fahrenheit' % (temp, result)
    else:
        return 'Invalid Input!!!'


temperature, flag = input('Enter the temperature in this format 60°C or 45°F : ').split('°')

print(temp_converter(temperature, flag))

# -------------------------------------------------------------------------------------------------------------------------

# Input 1 :
# Enter the temperature in this format 60°C or 45°F : 140°C

# Output 1 :
# 140°C is 284 in Fahrenheit

# Input 2 :
# Enter the temperature in this format 60°C or 45°F : 60°F

# Output 2 :
# 60°F is 15 in Celsius
