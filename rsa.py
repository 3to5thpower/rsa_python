import random
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 2)):
        if n % i == 0:
            return False
    return True

def prime_list(n):
    res = []
    for i in range(2, n):
        if is_prime(i):
            res.append(i)
    return res

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)


def generate_keys(p, q):
    n = p * q
    l = lcm(p - 1, q - 1)

    for i in range(2, l):
        if gcd(i, l) == 1:
            e = i
            break

    for i in range(2, l):
        if (e * i) % l == 1:
            d = i
            break

    return (e, n), (d, n)

def encrypt(plain_text, public_key):
    e, n = public_key

    plain_integers = []
    for c in plain_text:
        plain_integers.append(ord(c))

    encrypted_integers = []
    for i in plain_integers:
        encrypted_integers.append(pow(i, e, n))

    encrypted_text = ''
    for x in encrypted_integers:
        c = chr(x)
        encrypted_text += str(c)
    
    # sanitize
    encrypted_text = encrypted_text.encode('utf-8', 'replace').decode('utf-8')

    return encrypted_text

def decrypt(encrypted_text, private_key):
    d, n = private_key
    encrypted_integers = []
    for c in encrypted_text:
        encrypted_integers.append(ord(c))

    decrypted_integers = []
    for i in encrypted_integers:
        decrypted_integers.append(pow(i, d, n))

    decrypted_text = ''
    for x in decrypted_integers:
        c = chr(x)
        decrypted_text += str(c)

    return decrypted_text

if __name__ == '__main__':
    prime_list = prime_list(100)
    while 1:
        x = prime_list[random.randint(0, len(prime_list) - 1)]
        y = prime_list[random.randint(0, len(prime_list) - 1)]
        if x == y:
            continue

        public_key, private_key = generate_keys(x, y)
        if public_key[0] == private_key[0]:
            continue
        print('input text', end=':')
        s = input()
        if s == "quit":
            break

        print('private_key: {}'.format(private_key))
        print('public_key: {}'.format(public_key))

        encrypted_text = encrypt(s, public_key)
        decrypted_text = decrypt(encrypted_text, private_key)
        encrypted_text = encrypted_text.encode('utf-8', 'backslashreplace').decode('utf-8')
        print('encrypted_text: "{}"'.format(encrypted_text))
        print('decrypted_text: "{}"'.format(decrypted_text))

