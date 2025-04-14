# Package Sorter

## Objective
This project is designed for Thoughtful’s robotic automation factory. Your task is to implement a function that **automatically classifies packages** based on their volume and mass.

## Sorting Rules
Packages are sorted into different stacks based on the following criteria:

- **A package is bulky if**:
  - Its volume (`Width × Height × Length`) **≥ 1,000,000 cm³`, OR  
  - Any of its dimensions **≥ 150 cm**.
- **A package is heavy if**:
  - Its mass **≥ 20 kg**.

### **Stack Categories**
| Stack Name  | Condition |
|-------------|----------|
| **STANDARD** | If the package is **neither bulky nor heavy**. |
| **SPECIAL**  | If the package is **either bulky or heavy**. |
| **REJECTED** | If the package is **both bulky and heavy**. |

---

## Implementation

### **Main Script (`package_sorter.py`)**
This script **waits for user input**, processes it, and classifies the package.

#### **How It Works:**
1. The script **prompts** the user for four inputs:
   - Width, Height, Length (in centimeters)
   - Mass (in kilograms)
2. It validates the inputs:
   - Ensures all values are **positive numbers**.
   - Rejects invalid inputs (e.g., negative values, text).
3. It **calculates the package volume** and determines if it is **bulky or heavy**.
4. The package **stack is determined** based on the sorting rules.
5. The result is **displayed on the screen**.

#### **Running the Script**
To execute the script, open a terminal and run:
```bash
python package_sorter.py
