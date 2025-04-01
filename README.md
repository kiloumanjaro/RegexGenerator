
# Regular Expression Matcher (Python)

This project implements a regular expression matcher that checks whether given test strings match specified regular expression patterns. The program supports union, concatenation, and Kleene star operations. It processes input patterns, converts them into a format compatible with Python's regex library, and verifies if test strings conform to the patterns. The implementation includes functionality to handle multiple test cases, validate regular expressions, and provide results for each string tested.
### Overview
This project implements a regular expression matcher that checks if test strings match given patterns. It supports union, concatenation, and Kleene star operations, and processes multiple test cases to verify string matches against the specified regular expression.
### Features

The program verifies the correctness of strings with respect to the following types of regular expression operations:
- Union (denoted by + for OR)
- Concatenation (symbols placed next to each other)
- Kleene Star (denoted by *, allowing 0 or more repetitions of the preceding pattern)

### Constraints
Union (OR): The symbol + denotes a union of two expressions. For example, a + b matches either a or b.

Concatenation: Symbols placed together without any separators represent concatenation. For example, aaabbb matches the string aaabbb.

Kleene Star: The * allows repetition of the preceding expression 0 or more times. For example, a* matches any sequence of as, including the empty string.
### Input Format
- The alphabet used for the regular expressions consists of a, b, and the empty string e.
- The first line of the input file specifies the number of test cases.
- Each test case consists of:

        1. A regular expression.

        2. A number representing how many strings need to be verified.

        3. A list of strings to verify.
    


### Input Example

    cpp
    4
    1
    1 5 7 8
    10 -2 4 5
    3
    1 1 8
    1 2 7
    3
    4
    hello abcd wxyz
    world wxyz abcd lmno
    4
    1 1 world
    2 2 world
    5
    7 2
    5 1
    {1,2,3} {1,2} {7,8,9}
    {1,2} {1,2,5} {7,8,9,10}
    2
    2 2 {7,8,9,10}
    7 2

### Expected Output

For each string to be tested, the program outputs either "yes" if the string matches the regular expression or "no" if it does not.

```
yes
yes
no
yes
yes
yes
no
yes
no
no
no
```
### Compilation and Execution
#### Compilation
To run the Python program, simply execute it with Python:
```
python regex_checker.py
```


### Future Improvements
- Handle edge cases with more complex regular expressions.

- Optimize regex pattern processing for larger inputs.

- Implement an interactive mode for dynamic regex testing.
## Authors

- [@kiloumanjaro](https://github.com/kiloumanjaro)

