#Problem Statement
"""Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius."""


def main():
    # Ask the user for temperature in Fahrenheit
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert to Celsius using the formula
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

    # Print the result
    print("Temperature:", str(degrees_fahrenheit) + "F =", str(degrees_celsius) + "C")



# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()