import time

lower_case_alphabet = list(range(ord('a'), ord('z')+1))
upper_case_alphabet = list(range(ord('A'), ord('Z')+1))

# a = 97
# z = 122
# A = 65
# Z = 90

def decrypt(cipher, key):
    return [c^key for c in cipher]

with open('p059_cipher.txt') as f:
    cipher = f.read()
cipher = cipher.split(',')
cipher = [int(n) for n in cipher]

start = time.time()

key = []
total_sum = 0
for k in range(3):
    cipher_k = [cipher[i] for i in range(k, len(cipher), 3)]
    
    best_a = None
    best_ascii_sum = 0
    for a in lower_case_alphabet:
        # print(a)
        s = 0
        for d in decrypt(cipher_k, a):
            s += d in lower_case_alphabet
            s += d in upper_case_alphabet

        if s >= best_ascii_sum:
            best_ascii_sum = s
            best_a = a
            print(a)

    key.append(best_a)

print("Done in ", time.time() - start, " seconds")
print("Key: ", key, " As ASCII: ", ''.join([chr(i) for i in key]))

current_key = 0
total_sum = 0
text = []
for c in cipher:
    e = c^key[current_key]
    total_sum += e
    text.append(chr(e))
    current_key += 1
    current_key %= 3

print("Text: ", ''.join(text))
print("Sum off values: ", total_sum)