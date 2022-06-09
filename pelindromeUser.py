"""
Author : Tanmoy
Date : 2021
Purpose : if greater than 10 return pelindrome
"""

def next_peli(n):
    if n > 10:
        while str(n) != str(n)[::-1]:
            n += 1
        return n
    return n


if __name__ == "__main__":
    numbers = []
    result = []
    n = int(input("Enter the number of text cases: "))

    for i in range(n):
        num = int(input("Enter the number : "))
        numbers.append(num)
        result.append(next_peli(num))
    print(f"your inputs : {numbers}")
    print(f" the result is : {result}")

