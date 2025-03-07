def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n ** 0.5) +1):
        if n % i == 0:
            return False
    return True
def count_primes(limit):
    prime_numbers =[num for num in range(limit+1) if is_prime(num)]
    return len(prime_numbers), prime_numbers

num = int(input("Enter a Number"))
prime_count, prime_list = count_primes(num)
print(f"Total prime numbers from 0 to {num} : {prime_count}")
print("prime Numbers:", prime_list)