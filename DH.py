import math

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to generate a prime number
def generate_prime():
    prime = 0
    while not is_prime(prime):
        prime = int(input("Enter a prime number (q): "))
    return prime

# Function to calculate the primitive root modulo q
def calculate_alpha(q):
    alpha = 0
    while alpha <= 1 or alpha >= q:
        alpha = int(input("Enter a primitive root (alpha): "))
    return alpha

# Function to calculate the public key
def calculate_public_key(q, alpha, x):
    return (alpha ** x) % q

# Function to calculate the shared key
def calculate_shared_key(q, public_key, private_key):
    return (public_key ** private_key) % q

if __name__ == "__main__":
    # Step 1: Generate a prime number
    q = generate_prime()

    # Step 2: Calculate the primitive root modulo q
    alpha = calculate_alpha(q)

    # Step 3: Input private keys for Alice and Bob
    x_a = int(input("Enter private key for Alice (X_A): "))
    x_b = int(input("Enter private key for Bob (X_B): "))

    # Step 4: Calculate public keys for Alice and Bob
    public_key_a = calculate_public_key(q, alpha, x_a)
    public_key_b = calculate_public_key(q, alpha, x_b)

    # Step 5: Calculate shared keys for Alice and Bob
    shared_key_a = calculate_shared_key(q, public_key_b, x_a)
    shared_key_b = calculate_shared_key(q, public_key_a, x_b)

    # Step 6: Print the results
    print("\nPublic Key (Alice):")
    print("q =", q)
    print("alpha =", alpha)
    print("e =", public_key_a)
    print("\nPublic Key (Bob):")
    print("q =", q)
    print("alpha =", alpha)
    print("e =", public_key_b)

    print("\nShared Key (Alice):")
    print("s =", shared_key_a)
    print("\nShared Key (Bob):")
    print("s =", shared_key_b)

