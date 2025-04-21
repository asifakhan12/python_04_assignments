"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""


# Define gravitational constants relative to Earth's gravity
MERCURY_GRAVITY = 0.38
VENUS_GRAVITY = 0.91
MARS_GRAVITY = 0.38
JUPITER_GRAVITY = 2.34
SATURN_GRAVITY = 1.06
URANUS_GRAVITY = 0.92
NEPTUNE_GRAVITY = 1.19

def main():
    # Prompt the user for their weight on Earth
    earth_weight = float(input("Enter your weight on Earth (kg): "))
    
    # Prompt the user for the name of a planet
    planet = input("Enter a planet (first letter uppercase): ")

    # Determine the gravitational constant for the selected planet
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    else:
        # Assume the user typed in one of the valid planets, so "else" is for Neptune
        gravity_constant = NEPTUNE_GRAVITY

    # Calculate the equivalent weight on the selected planet
    planetary_weight = earth_weight * gravity_constant
    rounded_planetary_weight = round(planetary_weight, 2)

    # Print the result
    print("The equivalent weight on " + planet + ": " + str(rounded_planetary_weight) + " kg")

# Python boilerplate to run the program
if __name__ == "__main__":
    main()
