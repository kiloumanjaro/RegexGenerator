'''I declare, upon my honor, that I did this machine problem assignment by myself
using references from the lecture notes and MPs.'''

import re

def process_regex(input_str):
    input_str = input_str.replace(" ", "")  
    input_str = input_str.replace("+", "|")  

    modified_regex = ""
    prev_char = ""
    
    for char in input_str:
        if char == "*":
            modified_regex += "*"
        else:
            if prev_char and prev_char not in "(|" and char not in "|)*":
                modified_regex += ""
            modified_regex += char
        prev_char = char

    if input_str != "e":
        modified_regex = modified_regex.replace('e', '')
    
    return modified_regex

def main():
    num_cases = int(input()) 
    
    for _ in range(num_cases):
        regex_pattern = input().strip()
        
        if regex_pattern == "e":
            num_tests = int(input())
            test_strings = [input().strip() for _ in range(num_tests)]
            for s in test_strings:
                print("yes" if s == "e" else "no")
            continue

        modified_pattern = process_regex(regex_pattern)
        
        try:
            reg = re.compile(modified_pattern)
        except re.error as e:
            print(f"Invalid regex: {e}")
            continue
        
        num_tests = int(input())
        test_strings = [input().strip() for _ in range(num_tests)]

        for s in test_strings:
            modified_s = s.replace('e', '')
            print("yes" if reg.fullmatch(modified_s) else "no")

if __name__ == "__main__":
    main()
