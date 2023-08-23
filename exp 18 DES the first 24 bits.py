def left_shift(bits, n):
    return (bits << n) & 0xFFFFFFF | (bits >> (28 - n))

def generate_subkeys(initial_key):
    subkeys = []
    left_part = (initial_key >> 28) & 0xFFFFFFF
    right_part = initial_key & 0xFFFFFFF
    
    for i in range(16):
        left_part = left_shift(left_part, 1)
        right_part = left_shift(right_part, 1)
        
        subkey = (left_part << 28) | right_part
        subkeys.append(subkey)
    
    return subkeys

def main():
    initial_key = 0x123456789ABC  # 48-bit initial key
    subkeys = generate_subkeys(initial_key)
    
    for i, subkey in enumerate(subkeys):
        print(f"Subkey {i+1}: {subkey:012X}")

if __name__ == "__main__":
    main()

Subkey 1: 2468ACF13578
Subkey 2: 48D149E26AF1
Subkey 3: 91A283C4D5E3
Subkey 4: 123450789ABC6
Subkey 5: 2468A0F13578C
Subkey 6: 48D140E26AF19
Subkey 7: 91A280C4D5E33
Subkey 8: 123450089ABC67
Subkey 9: 2468A0013578CF
Subkey 10: 48D140026AF19E
Subkey 11: 91A28004D5E33C
Subkey 12: 23450019ABC678
Subkey 13: 468A0023578CF1
Subkey 14: 8D140046AF19E2
Subkey 15: 1A28009D5E33C4
Subkey 16: 3450012ABC6789
