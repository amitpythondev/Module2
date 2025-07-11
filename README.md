# Module2

Task 1: Perform Basic Mathematical Operations

This Python script performs **basic mathematical operations** between two numbers input by the user. Here's a breakdown of its functionality:

---

### 🔢 **Step-by-step Functionality:**

1. **User Input:**

   ```python
   n1 = input("Enter the first number : ")
   n2 = input("Enter the second number : ")
   ```

   * Prompts the user to enter two numbers.
   * The inputs are initially captured as strings.

2. **Convert to Integers:**

   ```python
   n1 = int(n1)
   n2 = int(n2)
   ```

   * Converts the string inputs to integers for performing arithmetic operations.

3. **Mathematical Operations:**

   * **Addition:**

     ```python
     add_val = n1 + n2
     ```

     Adds the two numbers.

   * **Subtraction:**

     ```python
     sub_val = n2 - n1
     ```

     Subtracts the **first number from the second**.

   * **Multiplication:**

     ```python
     multi_val = n1 * n2
     ```

     Multiplies the two numbers.

   * **Division:**

     ```python
     div_val = n2 / n1
     ```

     Divides the **second number by the first** (note: this will raise a `ZeroDivisionError` if `n1` is 0).

4. **Output:**

   ```python
   print("Addition: ", add_val)
   print("\nSubtraction: ", sub_val)
   print("\nMultiplication: ", multi_val)
   print("\nDivision: ", div_val)
   ```

   * Prints the results of each operation with descriptive labels.

---

### 🛠️ **Example Output:**

If the user enters:

```
Enter the first number : 4
Enter the second number : 8
```

Output:

```
Addition:  12
Subtraction:  4
Multiplication:  32
Division:  2.0
```

Task 2: Create a Personalized Greeting

This Python script is designed to create a **personalized greeting** by combining a user's first and last names. Here's a detailed explanation of its functionality:

---

### 🔍 **Step-by-step Description:**

1. **User Input:**

   ```python
   fname = input("Enter the first name : ")
   lname = input("Enter the last name : ")
   ```

   * Prompts the user to input their **first name** and **last name** separately.
   * The values are stored as strings in variables `fname` and `lname`.

2. **Concatenate Full Name:**

   ```python
   full_name = fname + " " + lname
   ```

   * Combines the first name and last name into a single string, separated by a space.
   * Stores the result in the `full_name` variable.

3. **Display Personalized Greeting:**

   ```python
   print(f"Hello, {full_name}! welcome to the Python program.")
   ```

   * Prints a message using an **f-string** (formatted string).
   * The `{full_name}` is replaced by the concatenated name.
   * The final output is a customized greeting.

---

### ✅ **Example Output:**

If the user enters:

```
Enter the first name : Amit
Enter the last name : Gautam
```

Then the program will display:

```
Hello, Amit Gautam! welcome to the Python program.
```
