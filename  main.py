import math

def permutation(n, r):
    return math.factorial(n) // math.factorial(n - r)

def combination(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def main():
    print("Permutation and Combination Calculator")
    
    try:
        n = int(input("Enter total items (n): "))
        r = int(input("Enter items to choose/arrange (r): "))
        
        if n < 0 or r < 0:
            print("n and r must be non-negative integers.")
        elif r > n:
            print("r cannot be greater than n.")
        else:
            print(f"P({n}, {r}) = {permutation(n, r)}")
            print(f"C({n}, {r}) = {combination(n, r)}")
    
    except ValueError:
        print("Invalid input. Please enter integers.")

if __name__ == "__main__":
    main()
