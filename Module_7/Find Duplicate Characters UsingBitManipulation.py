n = input().strip()
seen = 0
duplicates = 0
op = []
for ch in n:
    bit = 1 << (ord(ch) - ord('a'))
    if seen & bit:
        if not (duplicates & bit):
            op.append(ch)
            duplicates |= bit
    else:
        seen |= bit
if op:
    print(*op)
else:
    print("No duplicates")
