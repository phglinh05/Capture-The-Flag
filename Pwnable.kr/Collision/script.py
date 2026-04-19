
import struct, random, time, sys

# target decimal
target = 568_134_124   # = 0x21DD09EC

# printable ASCII range: '!' (0x21) .. '~' (0x7e)
PRINT_MIN, PRINT_MAX = 0x21, 0x7e
printable_range = list(range(PRINT_MIN, PRINT_MAX+1))

def u32_le_from_bytes(b4):
    return struct.unpack('<I', bytes(b4))[0]

def pack_u32_le(x):
    return list(struct.pack('<I', x & 0xFFFFFFFF))

random.seed(int(time.time()) ^ 0xC0FFEE)

start = time.time()
trials = 0
found = None
max_trials = 2_000_000

while trials < max_trials:
    trials += 1
    parts = []
    all_bytes = []
    # pick 4 blocks (16 bytes) randomly from printable bytes
    for _ in range(4):
        block = [random.choice(printable_range) for __ in range(4)]
        all_bytes.extend(block)
        parts.append(u32_le_from_bytes(block))
    s = sum(parts) & 0xFFFFFFFF
    need = (target - s) & 0xFFFFFFFF
    need_bytes = pack_u32_le(need)
    # require printable bytes for the final block as well
    if all(PRINT_MIN <= x <= PRINT_MAX for x in need_bytes):
        all_bytes.extend(need_bytes)
        # verify
        ints = [u32_le_from_bytes(all_bytes[i*4:(i+1)*4]) for i in range(5)]
        if sum(ints) & 0xFFFFFFFF == target:
            found = bytes(all_bytes)
            break
    if trials % 100000 == 0:
        print(f"trials={trials} elapsed={time.time()-start:.1f}s", file=sys.stderr)

if not found:
    print("No printable pass found in", trials, "trials", file=sys.stderr)
    sys.exit(2)

# Print results / run suggestion
hex_bytes = ''.join(f"\\x{b:02x}" for b in found)
try:
    printable_str = found.decode('ascii')
except:
    printable_str = repr(found)

print("Found after trials:", trials)
print("Printable string:")
print(printable_str)
print("\nHex bytes:")
print(' '.join(f"{b:02x}" for b in found))
print("\nCommand to run (copy & paste):")
print(f"./col \"$(printf '{hex_bytes}')\"")
print("\nIntegers (little-endian):")
for i,v in enumerate([u32_le_from_bytes(found[i*4:(i+1)*4]) for i in range(5)]):
    print(f" ip[{i}] = {v} (0x{v:08x})")
print(f"\nSum = 0x{sum([u32_le_from_bytes(found[i*4:(i+1)*4]) for i in range(5)]) & 0xFFFFFFFF:08x}")
