import math

def calculate_phi(p, q):
    return (p - 1) * (q - 1)

# Part A
print("Part A:")
e_a = int(input("Enter the public key 'e' value for party A: "))
n_a = int(input("Enter the public key 'n' value for party A: "))
print("Public key for party A:", e_a, n_a)

# Find prime factors of n_a
p_a, q_a = None, None
for p in range(2, n_a):
    if n_a % p == 0:
        p_a = p
        q_a = n_a // p
        break
print("Prime factors of n_a:", p_a, q_a)

phi_n_a = calculate_phi(p_a, q_a)
print("Phi(n) for party A:", phi_n_a)

d_a = pow(e_a, -1, phi_n_a)
print("Private key for A:", d_a)
print()

# Part B
print("Part B:")
e_b = int(input("Enter the public key 'e' value for party B: "))
n_b = int(input("Enter the public key 'n' value for party B: "))
print("Public key for party B:", e_b, n_b)

# Find prime factors of n_b
p_b, q_b = None, None
for p in range(2, n_b):
    if n_b % p == 0:
        p_b = p
        q_b = n_b // p
        break
print("Prime factors of n_b:", p_b, q_b)

phi_n_b = calculate_phi(p_b, q_b)
print("Phi(n) for party B:", phi_n_b)

d_b = pow(e_b, -1, phi_n_b)
print("Private key for B:", d_b)
print()

# Encryption and Decryption - A TO B
M_a_to_b = int(input("Enter the plaintext message (A to B): "))
C_a_to_b = pow(M_a_to_b, e_a, n_a)
print("Cipher-text sent by A to B:", C_a_to_b)
M_decrypted_b = pow(C_a_to_b, d_a, n_a)
print("Decrypted message by B:", M_decrypted_b)

# Encryption and Decryption - B TO A
M_b_to_a = int(input("Enter the plaintext message (B to A): "))
C_b_to_a = pow(M_b_to_a, e_b, n_b)
print("Cipher-text sent by B to A:", C_b_to_a)
M_decrypted_a = pow(C_b_to_a, d_b, n_b)
print("Decrypted message by A:", M_decrypted_a)