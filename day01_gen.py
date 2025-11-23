import pandas as pd
import numpy as np

# Data for 30 MCQs
mcq_data = [
    # -----------------------------------------------------
    # Programming Concepts (5 Qs)
    # -----------------------------------------------------
    {
        'Question': "What is the primary difference between a **compiler** and an **interpreter**?",
        'A': "A compiler translates the entire program before execution; an interpreter translates and executes line-by-line.",
        'B': "A compiler is used for high-level languages; an interpreter is used for low-level languages.",
        'C': "A compiler finds errors during runtime; an interpreter finds errors during translation.",
        'D': "A compiler only supports object-oriented programming; an interpreter only supports procedural programming.",
        'Correct': 'A',
        'Explanation': 'A compiler translates the whole program into machine code at once (ahead-of-time), while an interpreter executes code one statement at a time.'
    },
    {
        'Question': "Which of the following refers to the **syntax** of a programming language?",
        'A': "The meaning of the program and its instructions.",
        'B': "The rules that govern the structure and arrangement of code elements.",
        'C': "The set of all possible valid words in the language.",
        'D': "The memory allocation strategy used by the language.",
        'Correct': 'B',
        'Explanation': 'Syntax defines the formal rules for writing structurally correct programs. Semantics is the meaning, and Lexis refers to the vocabulary/tokens.'
    },
    {
        'Question': "A Python program fails with a `SyntaxError`. Which aspect of the language has been violated?",
        'A': "Semantics",
        'B': "Lexis",
        'C': "Syntax",
        'D': "Logic",
        'Correct': 'C',
        'Explanation': "A `SyntaxError` indicates a violation of the language's grammar or structural rules."
    },
    {
        'Question': "What is the term for the set of valid characters and tokens (like keywords, identifiers) that can be used in a programming language?",
        'A': "Semantics",
        'B': "Syntax",
        'C': "Lexis",
        'D': "Orthography",
        'Correct': 'C',
        'Explanation': 'Lexis refers to the vocabulary of the language—the valid tokens and characters.'
    },
    {
        'Question': "Which programming language is typically compiled and known for its performance, compared to Python which is interpreted (in CPython)?",
        'A': "JavaScript",
        'B': "PHP",
        'C': "C++",
        'D': "Ruby",
        'Correct': 'C',
        'Explanation': 'C++ is a compiled language, often leading to faster execution speed than interpreted languages like CPython, which is the most common Python implementation.'
    },
    # -----------------------------------------------------
    # Environment Setup (3 Qs)
    # -----------------------------------------------------
    {
        'Question': "Which of these is NOT typically considered an Integrated Development Environment (IDE) or a popular code editor for Python?",
        'A': "Visual Studio Code (VS Code)",
        'B': "PyCharm",
        'C': "Jupyter Notebook",
        'D': "Google Chrome",
        'Correct': 'D',
        'Explanation': 'Google Chrome is a web browser. VS Code, PyCharm, and Jupyter are all common tools for writing and running Python code.'
    },
    {
        'Question': "What file extension is traditionally used for a standard Python script?",
        'A': ".pyc",
        'B': ".txt",
        'C': ".py",
        'D': ".exe",
        'Correct': 'C',
        'Explanation': 'The `.py` extension is used for Python source code files. `.pyc` are compiled bytecode files.'
    },
    {
        'Question': "What is the role of `pip` in the Python ecosystem?",
        'A': "It is the main command for running a Python script.",
        'B': "It is the package installer for Python.",
        'C': "It is a built-in function for printing output.",
        'D': "It is a type-hinting library.",
        'Correct': 'B',
        'Explanation': '`pip` is the standard package manager used to install and manage software packages from the Python Package Index (PyPI).'
    },
    # -----------------------------------------------------
    # Data Types & Literals (7 Qs)
    # -----------------------------------------------------
    {
        'Question': "What is the Python data type for the literal `3.14159`?",
        'A': "int",
        'B': "float",
        'C': "decimal",
        'D': "str",
        'Correct': 'B',
        'Explanation': 'A literal with a decimal point is automatically inferred as a floating-point number (`float`) in Python.'
    },
    {
        'Question': "Which of the following literals represents a **Boolean** value in Python?",
        'A': "True and False",
        'B': "1 and 0",
        'C': "'True' and 'False'",
        'D': "True or False",
        'Correct': 'D',
        'Explanation': '`True` and `False` (with capital T and F) are the two literals of the Python `bool` (Boolean) type.'
    },
    {
        'Question': "How is the number 10 represented in **binary**?",
        'A': "0b10",
        'B': "0o12",
        'C': "0xa",
        'D': "1010",
        'Correct': 'D',
        'Explanation': '$10$ in decimal is $1010$ in binary. $0b$ is the Python prefix for binary literals.'
    },
    {
        'Question': "What is the decimal equivalent of the **hexadecimal** number `0x1A`?",
        'A': "16",
        'B': "26",
        'C': "10",
        'D': "20",
        'Correct': 'B',
        'Explanation': 'In hexadecimal, $1$ is $1 \times 16^1 = 16$ and $A$ is $10 \times 16^0 = 10$. $16 + 10 = 26$.'
    },
    {
        'Question': "Which Python literal uses the **octal** base system?",
        'A': "0b101",
        'B': "0o52",
        'C': "0xAB",
        'D': "52",
        'Correct': 'B',
        'Explanation': 'The prefix `0o` denotes an octal (base 8) number in Python.'
    },
    {
        'Question': "What does the **scientific notation** literal `1.2e-5` represent?",
        'A': "1.2 multiplied by 5",
        'B': "1.2 multiplied by 10 to the power of 5",
        'C': "1.2 multiplied by 10 to the power of -5",
        'D': "1.2 divided by 5",
        'Correct': 'C',
        'Explanation': 'The `e` (or `E`) in scientific notation means "times 10 to the power of". So, $1.2e-5$ is $1.2 \times 10^{-5}$.'
    },
    {
        'Question': "What is the Python data type for the literal `5`?",
        'A': "float",
        'B': "str",
        'C': "int",
        'D': "bool",
        'Correct': 'C',
        'Explanation': 'A whole number without a decimal point is an integer (`int`).'
    },
    # -----------------------------------------------------
    # Variables & Naming (3 Qs)
    # -----------------------------------------------------
    {
        'Question': "According to **PEP-8**, which variable name follows the recommended convention for a local variable?",
        'A': "Total_Count",
        'B': "totalCount",
        'C': "total_count",
        'D': "TOTAL_COUNT",
        'Correct': 'C',
        'Explanation': 'PEP-8 recommends using **lowercase with words separated by underscores** (snake\_case) for function and variable names.'
    },
    {
        'Question': "Which of the following is an **invalid** Python variable name?",
        'A': "my_variable_1",
        'B': "_secret_data",
        'C': "1st_place",
        'D': "calculateTotal",
        'Correct': 'C',
        'Explanation': 'Variable names cannot begin with a number. They must start with a letter or an underscore.'
    },
    {
        'Question': "According to PEP-8, what is the recommended naming convention for a **constant** variable (e.g., a fixed value)?",
        'A': "camelCase",
        'B': "snake_case",
        'C': "PascalCase",
        'D': "UPPERCASE_SNAKE_CASE",
        'Correct': 'D',
        'Explanation': 'Constants are typically named using all capital letters with words separated by underscores (UPPERCASE\_SNAKE\_CASE).'
    },
    # -----------------------------------------------------
    # Console I/O (6 Qs)
    # -----------------------------------------------------
    {
        'Question': "Which function is used to get **user input** from the console in Python?",
        'A': "print()",
        'B': "output()",
        'C': "input()",
        'D': "read()",
        'Correct': 'C',
        'Explanation': 'The `input()` function prompts the user to enter data and returns it as a string.'
    },
    {
        'Question': "What is the data type of the value returned by the `input()` function?",
        'A': "int",
        'B': "float",
        'C': "bool",
        'D': "str",
        'Correct': 'D',
        'Explanation': 'The `input()` function always returns a string (`str`), even if the user types numbers. Type casting is required for arithmetic operations.'
    },
    {
        'Question': "If `x = 10` and you execute `y = str(x)`, what is the data type of `y`?",
        'A': "int",
        'B': "float",
        'C': "str",
        'D': "bool",
        'Correct': 'C',
        'Explanation': 'The `str()` function is used for **type casting**, converting the integer `x` into a string.'
    },
    {
        'Question': "What is the output of the Python expression `len(\"PCEP Practice\")`?",
        'A': "11",
        'B': "12",
        'C': "13",
        'D': "14",
        'Correct': 'C',
        'Explanation': 'The string "PCEP Practice" has $11$ letters and $1$ space, totaling $12$ characters. Wait, I miscounted: P C E P   P r a c t i c e $\rightarrow 12$ characters (P, C, E, P, , P, r, a, c, t, i, c, e). The space counts. Let me count again: P-1, C-2, E-3, P-4, $\text{space}$-5, P-6, r-7, a-8, c-9, t-10, i-11, c-12, e-13. The length is 13. Re-evaluating options: A-11, B-12, C-13, D-14. The correct answer is 13 (C).'
    },
    {
        'Question': "Which character is typically used by the `print()` function to separate arguments by default?",
        'A': "Comma (`,`)",
        'B': "Semicolon (`;`)",
        'C': "Space (` `)",
        'D': "Newline (`\\n`)",
        'Correct': 'C',
        'Explanation': 'The `print()` function uses the `sep` argument, which defaults to a single space, to separate multiple items.'
    },
    {
        'Question': "How do you correctly convert the string variable `s = \"50\"` into an integer?",
        'A': "int(s)",
        'B': "integer(s)",
        'C': "s.to_int()",
        'D': "str_to_int(s)",
        'Correct': 'A',
        'Explanation': 'The built-in function `int()` is used to cast a compatible value (like a string of digits) to an integer.'
    },
    # -----------------------------------------------------
    # Operators (6 Qs)
    # -----------------------------------------------------
    {
        'Question': "What is the result of the Python expression `7 // 3`?",
        'A': "2.333...",
        'B': "2",
        'C': "1",
        'D': "2.0",
        'Correct': 'B',
        'Explanation': 'The `//` operator performs **floor division**, which returns the integer part of the quotient. $7 / 3 \approx 2.333$, so the floor is $2$.'
    },
    {
        'Question': "Which of the following is the **exponentiation** operator in Python?",
        'A': "^",
        'B': "**",
        'C': "//",
        'D': "$$",
        'Correct': 'B',
        'Explanation': 'The `**` operator is used for exponentiation (raising a number to a power). For example, $2**3$ is $8$.'
    },
    {
        'Question': "If `x = 5`, what is the value of `x` after the operation `x &= 3` is performed?",
        'A': "1",
        'B': "3",
        'C': "5",
        'D': "15",
        'Correct': 'A',
        'Explanation': '`x &= 3` is a **bitwise assignment** operator, equivalent to `x = x & 3`. Binary $5$ is $0101$ and binary $3$ is $0011$. $0101 \text{ AND } 0011$ is $0001$, which is $1$ in decimal.'
    },
    {
        'Question': "What is the result of the Boolean expression `(5 < 10) and (10 == 10)`?",
        'A': "5",
        'B': "False",
        'C': "True",
        'D': "SyntaxError",
        'Correct': 'C',
        'Explanation': 'Both relational expressions are true: $5 < 10$ is `True` and $10 == 10$ is `True`. `True and True` is `True`.'
    },
    {
        'Question': "Which of these is the **relational** operator that checks for **not equal to**?",
        'A': "!=",
        'B': "==",
        'C': "=<",
        'D': "not=",
        'Correct': 'A',
        'Explanation': 'The `!=` operator checks if two values are not equal. The `==` operator checks for equality.'
    },
    {
        'Question': "What is the result of the expression `12 % 5`?",
        'A': "2",
        'B': "2.4",
        'C': "7",
        'D': "3",
        'Correct': 'A',
        'Explanation': 'The `%` operator is the **modulo** (remainder) operator. $12$ divided by $5$ is $2$ with a remainder of $2$.'
    },
    # -----------------------------------------------------
    # Padding the questions to reach 30
    # -----------------------------------------------------
    {
        'Question': "Which of the following is a key component of the Python **virtual environment** concept?",
        'A': "Allows simultaneous execution of multiple Python versions on the same machine.",
        'B': "It is a physical server hosting Python applications.",
        'C': "Isolates project-specific dependencies from the system-wide Python installation.",
        'D': "It is a graphical user interface for Python.",
        'Correct': 'C',
        'Explanation': 'A virtual environment isolates packages and dependencies for a specific project, preventing conflicts between different projects.'
    },
    {
        'Question': "If a number is represented in **octal** as $0o20$, what is its value in decimal?",
        'A': "16",
        'B': "20",
        'C': "8",
        'D': "14",
        'Correct': 'A',
        'Explanation': 'The octal number $0o20$ is calculated as $(2 \times 8^1) + (0 \times 8^0) = 16 + 0 = 16$ in decimal.'
    },
    {
        'Question': "Which operator has the **lowest precedence** in the following list: `+`, `*`, `or`, `==`?",
        'A': "+",
        'B': "*",
        'C': "or",
        'D': "==",
        'Correct': 'C',
        'Explanation': 'Logical operators like `or` have a lower precedence than arithmetic (`+`, `*`) and relational (`==`) operators.'
    },
    {
        'Question': "Which statement correctly demonstrates **type casting** in Python?",
        'A': "int(5.5) results in 6",
        'B': "float('3') results in '3.0'",
        'C': "bool(0) results in True",
        'D': "int('hello') results in 0",
        'Correct': 'B',
        'Explanation': "The `float()` function successfully converts the string '3' into the floating-point number $3.0$."
    }
]

# Create the DataFrame for the quiz data
# Columns 0-25
data_rows = []
for q_data in mcq_data:
    # 26 columns in total (0 to 25)
    row = ['Multiple choice', q_data['Question'], q_data['A'], q_data['B'], q_data['C'], q_data['D'], '']
    # Add 4 blank spacer columns (Index 7 to 10)
    row.extend([''] * 4)
    # Correct Answer (Index 11)
    row.append(q_data['Correct'])
    # Explanation (Index 12)
    row.append(q_data['Explanation'])
    # Add 13 blank spacer columns (Index 13 to 25)
    row.extend([''] * 13)
    data_rows.append(row)

df_quiz = pd.DataFrame(data_rows)


# --- Recreate the Socrative Header Rows (Rows 0-5) ---

# Reconstructing Header Row 0 (Instructions)
header_row_0 = ['Instructions:', 'Please fill in the below quiz according to the 5 steps below. You may then import the quiz into your Socrative account by selecting "My Quizzes" --> "Import Quiz" --> and selecting the relevant quiz to import. Please use only alphanumeric characters in the template.  You can use the \'Example Sheet\' as a reference.'] + [''] * 24

# Reconstructing Header Row 1 (Open-ended, A)
header_row_1 = [''] * 24 + ['Open-ended', 'A']

# Reconstructing Header Row 2 (Quiz Name, Multiple choice, B)
header_row_2 = ['1. Quiz Name:', 'PCEP Practice Quiz - 30 MCQs'] + [''] * 21 + ['Multiple choice', 'B']

# Reconstructing Header Row 3 (C)
header_row_3 = [''] * 24 + ['C']

# Reconstructing Header Row 4 (Multiple choice instruction, D)
header_row_4 = ['']
# The next cell is where '4. If you selected...' starts, but it spans a few columns
header_row_4.extend(['"4. If you selected multiple choice question, enter answers below each column:"', '', '', '', '']) # Cells 1 to 5
header_row_4.extend(['"5. Optional (Choose correct answer - you may leave this blank, or choose one or more correct answers. Students must select all the correct answers to be scored correct.)"']) # Cell 6, which appears to span up to Cell 11 based on the explanation cell at 12
header_row_4.extend([''] * 17) # Fill the rest
# The '5. Optional' cell is complex. The raw data showed:
# nan | nan | 4. If you selected multiple choice question, enter answers below each column: | nan | nan | nan | nan | 5. Optional...
# I'll simplify based on what matters for the import: the data rows. For the header rows, I will use a simplified set of column labels that align with the structure.
# Let's re-use the raw data for the header which is less error prone than hand-crafting it.
file_name = "socrativeQuizTemplate.xlsx - Quick Quiz.csv"
try:
    # Read the first 6 rows (header)
    df_raw_header = pd.read_csv(file_name, header=None, nrows=6, keep_default_na=False)
except Exception as e:
    print(f"Error reading header rows: {e}")
    # Fallback plan: use the manually constructed header if file reading fails or is malformed
    df_header_list = [
        ['Instructions:', 'Please fill in the below quiz according to the 5 steps below. You may then import the quiz into your Socrative account by selecting "My Quizzes" --> "Import Quiz" --> and selecting the relevant quiz to import. Please use only alphanumeric characters in the template.  You can use the \'Example Sheet\' as a reference.'] + [''] * 24,
        [''] * 24 + ['Open-ended', 'A'],
        ['1. Quiz Name:', 'PCEP Practice Quiz - 30 MCQs'] + [''] * 21 + ['Multiple choice', 'B'],
        [''] * 24 + ['C'],
        ['', '', '"4. If you selected multiple choice question, enter answers below each column:"', '', '', '', '', '"5. Optional (Choose correct answer - you may leave this blank, or choose one or more correct answers.  Students must select all the correct answers to be scored correct.)"', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'D'],
        ['2. Question Type:', '3. Question:', 'Answer A:', 'Answer B:', 'Answer C:', 'Answer D:', 'Answer E:', '', '', '', '', '', '6. Explanation (Optional):'] + [''] * 13
    ]
    # Standardize column count to 26
    df_header = pd.DataFrame(df_header_list)
    # Need to check the column size of the raw data. The raw data has 26 columns (0 to 25).
    # Since I cannot guarantee the raw data is easily read and merged, I will stick to the simplified manual construction which is what matters for the Socrative import.
    # The crucial row is the last one (index 5) as it defines the data columns.

# Reconstructing the header with the column names that matter for the CSV import tool:
# The header row at index 5 has 26 columns, so I'll pad the manually created rows to 26 columns.
df_header_list = [
    # Row 0: Instructions
    ['Instructions:', 'Please fill in the below quiz according to the 5 steps below. You may then import the quiz into your Socrative account by selecting "My Quizzes" --> "Import Quiz" --> and selecting the relevant quiz to import. Please use only alphanumeric characters in the template.  You can use the \'Example Sheet\' as a reference.'] + [''] * 24,
    # Row 1: Open-ended, A
    [''] * 24 + ['Open-ended', 'A'],
    # Row 2: Quiz Name, Multiple choice, B
    ['1. Quiz Name:', 'PCEP Practice Quiz - 30 MCQs'] + [''] * 21 + ['Multiple choice', 'B'],
    # Row 3: C
    [''] * 24 + ['C'],
    # Row 4: Multiple choice instruction, D
    ['', '', '"4. If you selected multiple choice question, enter answers below each column:"', '', '', '', '', '"5. Optional (Choose correct answer - you may leave this blank, or choose one or more correct answers.  Students must select all the correct answers to be scored correct.)"', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'D'],
    # Row 5: Column Headers for the data
    ['2. Question Type:', '3. Question:', 'Answer A:', 'Answer B:', 'Answer C:', 'Answer D:', 'Answer E:', '', '', '', '', '', '6. Explanation (Optional):'] + [''] * 13
]

# Ensure all rows have 26 columns
df_header_list = [row[:26] + [''] * (26 - len(row)) if len(row) < 26 else row[:26] for row in df_header_list]


df_header = pd.DataFrame(df_header_list)
df_full = pd.concat([df_header, df_quiz], ignore_index=True)

# Export the final DataFrame to CSV
output_file_name = "PCEP_30_MCQs.csv"
df_full.to_csv(output_file_name, index=False, header=False)

print(f"Successfully generated {len(mcq_data)} MCQs and saved to {output_file_name}")

x = int('0x1A')
print(x)