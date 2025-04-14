"""

### Rules

Sort the packages using the following criteria:
A package is bulky if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.

A package is heavy when its mass is greater or equal to 20 kg.

You must dispatch the packages in the following stacks:

STANDARD: standard packages (those that are not bulky or heavy) can be handled normally.

SPECIAL: packages that are either heavy or bulky can't be handled automatically.

REJECTED: packages that are both heavy and bulky are rejected.

"""

import math


def sort(width: float, height: float, length: float, mass: float) -> str:
    """Determines the package category based on its size and weight."""

    # Validate input to ensure dimensions and mass are positive, non-null, and numerical
    if any(not isinstance(val, (int, float)) or val <= 0 or math.isnan(val) for val in [width, height, length, mass]):
        return "INVALID INPUT"

    # Calculate volume
    volume = width * height * length

    # Determine bulky status
    bulky = volume >= 1_000_000 or any(dim >= 150 for dim in [width, height, length])

    # Determine heavy status
    heavy = mass >= 20

    # Categorize the package
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


if __name__ == "__main__":
    # Accept user input
    try:
        width = float(input("Enter package width (cm): "))
        height = float(input("Enter package height (cm): "))
        length = float(input("Enter package length (cm): "))
        mass = float(input("Enter package mass (kg): "))

        # Call the sorting function
        result = sort(width, height, length, mass)
        print(f"Package Classification: {result}")

    except ValueError:
        print("Invalid input! Please enter numerical values.")

"""

Extreme values (overflow handling)

    Test cases with huge numbers (e.g., width = 10**6, height = 10**6, etc.) to ensure correct categorization without overflow issues.

Minimal bulky scenario

    A package that is just at the threshold (150 cm) but not above the volume limit.

Minimal heavy scenario

    A package with mass = 19.99 kg (should be STANDARD), then mass = 20 kg (should be SPECIAL).

Floating-point precision anomalies

    Some systems may store floating-point values inconsistently, causing unexpected rounding errors in calculations. Testing 149.999 cm vs 150 cm ensures correct handling.

Unrealistic input values

    What if someone enters a dimension as None, an empty string "", or even NaN? The function should reject invalid inputs safely.
    
Why This Scales Well?

    Still O(1) complexity > No loops, just direct calculations.

    Handles extreme values and invalid input gracefully.
    
"""
