import sys

# Read the sequence of disks from standard input
disks = []
for line in sys.stdin:
    disk = line.strip()
    if disk in ["D", "L"]:
        disks.append(disk)
    else:
        print(f"Invalid input: {disk}. Only 'D' or 'L' are allowed.", file=sys.stderr)

# Print the original disks
print("Original disks:", disks)

# Perform brute-force swaps to arrange the disks
for i in range(len(disks)):
    for j in range(len(disks) - 1):
        if disks[j] == "D" and disks[j + 1] == "L":
            # Swap the disks
            disks[j], disks[j + 1] = disks[j + 1], disks[j]
            # Print the result after each swap
            print("Swap performed:", disks)

# Print the arranged disks
print("Arranged Disks:", disks)
