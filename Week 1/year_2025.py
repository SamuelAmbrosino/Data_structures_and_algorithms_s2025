''''
The year 2025 is special because (20+25)^2=2025, i.e., the year is the square of the sum of its first and second halves.
In a file special.py, implement the function check_year that reports if the given year is special. The function should return True or False.
Your function will be tested using many different test cases. In each test case, the year is in the range 1000–9999.
'''

def check_year(year):
    num = str(year)
    mid = len(num) // 2
    return ((int(num[:mid])+int(num[mid:])) ** 2) == year

if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2024)) # False
    print(check_year(2025)) # True
    print(check_year(2026)) # False
    print(check_year(3025)) # True
    print(check_year(5555)) # False

